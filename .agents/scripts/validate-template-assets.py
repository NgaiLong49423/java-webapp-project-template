#!/usr/bin/env python3
"""Validate selected template documentation and Agent assets safely."""

from __future__ import annotations

import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT_FILES = (
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    ".gitignore",
    ".agents/POLICY.md",
    ".agents/repo-contract.yml",
    ".github/pull_request_template.md",
    ".github/labels.yml",
    "docs/README.md",
    "docs/template-maintenance.md",
    "database/README.md",
)
SCOPED_DIRECTORIES = (
    "app",
    "database",
    ".agents/skills",
    ".agents/workflows",
    ".agents/scripts",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "docs/requirements",
    "docs/reports",
)
DOCUMENTS_WITH_METADATA = {
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    ".agents/POLICY.md",
    "app/README.md",
    "database/README.md",
    "docs/README.md",
    "docs/template-maintenance.md",
    "docs/reports/README.md",
    "docs/requirements/PRD.md",
    "docs/requirements/SRS.md",
}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKILL_NAME = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
LEGACY_APP_PATH = "A" + "pp" + "/"
LEGACY_AGENT_PATH = "." + "agent" + "/"
OLD_PATHS = (
    (re.compile(r"(?<![A-Za-z0-9_.])" + re.escape(LEGACY_APP_PATH)), "legacy application casing"),
    (re.compile(r"(?<![A-Za-z0-9_.])" + re.escape(LEGACY_AGENT_PATH)), "legacy Agent directory"),
)
PROTECTED_PARTS = ("docs", "diagrams")


def is_protected_relative(path: str) -> bool:
    normalized = posixpath.normpath(path).replace("\\", "/")
    parts = tuple(part.lower() for part in normalized.split("/"))
    return any(parts[index : index + 2] == PROTECTED_PARTS for index in range(max(0, len(parts) - 1)))


def collect_selected_files(root: Path) -> list[Path]:
    """Walk only explicitly allowed roots; never walk the general docs root."""
    selected: set[Path] = set()
    for item in ROOT_FILES:
        path = root / item
        if path.is_symlink():
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            selected.add(path)

    for relative_root in SCOPED_DIRECTORIES:
        start = root / relative_root
        if start.is_symlink() or not start.is_dir():
            continue
        for current, directories, filenames in os.walk(start, topdown=True, followlinks=False):
            current_path = Path(current)
            directories[:] = sorted(
                name for name in directories if not (current_path / name).is_symlink()
            )
            for filename in filenames:
                path = current_path / filename
                if path.is_symlink() or path.suffix.lower() not in TEXT_SUFFIXES:
                    continue
                selected.add(path)
    return sorted(selected, key=lambda path: path.relative_to(root).as_posix().lower())


def check_document_metadata(relative: str, content: str, errors: list[str]) -> None:
    if relative not in DOCUMENTS_WITH_METADATA:
        return
    header = "\n".join(content.splitlines()[:8])
    required = ("Document:", "File:", "Version:", "Created:", "Last Updated:", "Status:")
    missing = [field for field in required if f"**{field}**" not in header]
    if missing:
        errors.append(f"{relative}: missing document metadata fields: {', '.join(missing)}")
    if f"`{relative}`" not in header:
        errors.append(f"{relative}: metadata File field must use its repository-relative path")


def check_links(root: Path, relative: str, content: str, errors: list[str]) -> None:
    if not relative.endswith(".md"):
        return
    parent = posixpath.dirname(relative)
    for raw in MARKDOWN_LINK.findall(content):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme == "file":
            errors.append(f"{relative}: local file links are not portable: {target}")
            continue
        if parsed.scheme or target.startswith("#") or not parsed.path:
            continue
        link_path = unquote(parsed.path)
        if link_path.startswith("/"):
            errors.append(f"{relative}: use a relative link, not {target}")
            continue
        normalized = posixpath.normpath(posixpath.join(parent, link_path))
        # Do not stat, open, or otherwise inspect protected link targets.
        if is_protected_relative(normalized):
            continue
        if not (root / Path(*normalized.split("/"))).exists():
            errors.append(f"{relative}: broken relative link: {target}")


def check_local_outputs(root: Path, errors: list[str]) -> None:
    ignored = subprocess.run(
        ["git", "check-ignore", "--quiet", ".agents/outputs/.template-ignore-probe"],
        cwd=root,
        check=False,
    )
    if ignored.returncode != 0:
        errors.append(".agents/outputs/ must be ignored by Git")
    tracked = subprocess.run(
        ["git", "ls-files", "--", ".agents/outputs/"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if tracked.returncode != 0:
        errors.append("could not verify the local-only Agent outputs path")
    elif tracked.stdout.strip():
        errors.append(".agents/outputs/ contains Git-tracked paths; keep local outputs out of Git")


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    errors: list[str] = []
    files = collect_selected_files(root)

    for path in files:
        relative = path.relative_to(root).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{relative}: cannot read selected text file: {error}")
            continue
        for pattern, old_path in OLD_PATHS:
            if pattern.search(content):
                errors.append(f"{relative}: obsolete repository path reference ({old_path})")
        check_document_metadata(relative, content, errors)
        check_links(root, relative, content, errors)

    skill_root = root / ".agents/skills"
    if skill_root.is_dir() and not skill_root.is_symlink():
        for directory in sorted(skill_root.iterdir(), key=lambda path: path.name.lower()):
            if directory.is_symlink() or not directory.is_dir():
                continue
            skill_file = directory / "SKILL.md"
            if skill_file.is_symlink() or not skill_file.is_file():
                errors.append(f".agents/skills/{directory.name}: missing SKILL.md")
                continue
            frontmatter = skill_file.read_text(encoding="utf-8").split("---", 2)
            if len(frontmatter) != 3:
                errors.append(f"{skill_file.relative_to(root).as_posix()}: missing YAML frontmatter")
                continue
            match = SKILL_NAME.search(frontmatter[1])
            if not match:
                errors.append(f"{skill_file.relative_to(root).as_posix()}: missing valid name field")
            elif match.group(1) != directory.name:
                errors.append(
                    f"{skill_file.relative_to(root).as_posix()}: name {match.group(1)!r} "
                    f"does not match folder {directory.name!r}"
                )
            if not re.search(r"^description:\s*\S", frontmatter[1], re.MULTILINE):
                errors.append(f"{skill_file.relative_to(root).as_posix()}: missing description field")

    check_local_outputs(root, errors)
    if errors:
        print("Template asset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Template asset validation passed ({len(files)} selected text files).")
    print("Protected, local-only, generated, and unselected project content was excluded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
