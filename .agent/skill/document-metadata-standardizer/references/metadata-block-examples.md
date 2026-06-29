# Metadata Block Examples

This reference file provides standard metadata examples for common repository documentation files.

Use these examples only when the main `SKILL.md` needs a concrete metadata pattern.

## General Rules

- Put the metadata block before the first main heading.
- Use repository-relative paths only.
- Do not use local absolute paths such as `D:\...` or `file:///d:/...`.
- Do not force all documents to share the same document version.
- `v0.x.x` means the document is still draft or under review.
- `v0.x.x` documents should usually use `Status: Draft` or `Status: Under Review`.
- Use `Status: Active` only for documents that are stable enough to guide work.

## README.md

```markdown
> **Document:** Project README  
> **File:** `README.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Project Name
```

Use this for the root project overview document.

## SRS.md

```markdown
> **Document:** Software Requirements Specification  
> **File:** `docs/requirements/SRS.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Software Requirements Specification
```

Use this when the SRS is stable enough to guide coding, issue decomposition, testing, or planning.

## Draft SRS.md

```markdown
> **Document:** Software Requirements Specification  
> **File:** `docs/requirements/SRS.md`  
> **Version:** v0.3.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Under Review  

# Software Requirements Specification
```

Use this when the SRS is still being reviewed.

Do not treat this document as final unless the user explicitly confirms.

## PRD.md

```markdown
> **Document:** Product Requirements Document  
> **File:** `docs/requirements/PRD.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Product Requirements Document
```

PRD and SRS may have different document versions.

Example:

```text
PRD.md: v1.0.0
SRS.md: v1.0.2
```

This is valid if both are document versions.

## Project Requirements

```markdown
> **Document:** Project Requirements  
> **File:** `docs/requirements/project-requirements.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Project Requirements
```

Use this for high-level requirements that summarize or support PRD/SRS.

## CHANGELOG.md

```markdown
> **Document:** Changelog  
> **File:** `CHANGELOG.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Changelog
```

The changelog document version is not the same as project release versions listed inside the changelog.

Example:

```markdown
> **Version:** v1.0.0

# Changelog

## [Unreleased]

## [0.2.0] - 2026-06-29
```

The metadata version tracks the changelog file itself.

The entries inside the changelog track project or release versions.

## CONTRIBUTING.md

```markdown
> **Document:** Contribution Guide  
> **File:** `CONTRIBUTING.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Contributing Guide
```

Use this for branch, commit, PR, review, and collaboration rules.

## AGENTS.md

```markdown
> **Document:** Agent Instructions  
> **File:** `AGENTS.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Agent Instructions
```

Keep AGENTS.md short. Do not paste full SRS, README, or workflow explanations into it.

## Database README

```markdown
> **Document:** Database Documentation  
> **File:** `database/README.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Active  

# Database Documentation
```

Use this for database setup, schema notes, seed data, and query usage.

Do not add this Markdown metadata block to `.sql` files unless the user explicitly asks.

## Skill Document

```markdown
---
name: document-metadata-standardizer
description: Use this skill when the user asks to standardize document metadata.
risk: low
source: self
version: v1.0.0
created_date: 2026-06-29
last_updated_date: 2026-06-29
---

# Document Metadata Standardizer
```

For `SKILL.md`, use YAML frontmatter metadata instead of the Markdown quote block.

## Template Document

```markdown
> **Document:** README Template  
> **File:** `docs/templates/README_TEMPLATE.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Template  

# README Template
```

Use `Status: Template` for reusable template files that are not real project documents.

## Archived Document

```markdown
> **Document:** Software Requirements Specification Archive  
> **File:** `docs/archive/SRS_v1.0.0.md`  
> **Version:** v1.0.0  
> **Created:** 2026-06-29  
> **Last Updated:** 2026-06-29  
> **Status:** Archived  

# Software Requirements Specification Archive
```

Use `Status: Archived` for historical copies.

Do not edit archived documents unless the user explicitly asks.

## Deprecated Document

```markdown
> **Document:** Legacy Project Requirements  
> **File:** `docs/requirements/legacy-project-requirements.md`  
> **Version:** v1.2.0  
> **Created:** 2026-06-20  
> **Last Updated:** 2026-06-29  
> **Status:** Deprecated  

# Legacy Project Requirements
```

Use `Status: Deprecated` when the document still exists but should not be treated as the main source.

## Optional Fields Example

```markdown
> **Document:** Software Requirements Specification  
> **File:** `docs/requirements/SRS.md`  
> **Version:** v1.0.2  
> **Created:** 2026-06-27  
> **Last Updated:** 2026-06-29  
> **Status:** Active  
> **Owner:** Group 6  
> **Related Docs:** `README.md`, `docs/requirements/PRD.md`, `CHANGELOG.md`  
> **Project Version:** v0.2.0  
> **Baseline:** Project Baseline v0.2.0  

# Software Requirements Specification
```

Use optional fields only when they clarify the document relationship.

Do not add optional fields if they create noise.
