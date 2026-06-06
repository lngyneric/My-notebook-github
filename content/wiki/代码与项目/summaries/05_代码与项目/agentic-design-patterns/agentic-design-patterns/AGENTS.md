---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/AGENTS.md
raw_sha256: 47bd2a7fc39e246d6277e6dd47661264a2594a9acb9611eed4a73510f97048bb
compiled_at: 2026-04-24T08:18:49.700Z
---
# Repository Guidelines (Agentic Design Patterns Documentation Repository)
## Summary
This document formalizes end-to-end contribution and maintenance rules for the Agentic Design Patterns documentation repository, covering content organization, development workflows, formatting standards, testing requirements, commit/pull request protocols, and specialized rules for automated agent contributors. All rules are aligned with `rules.md`, the designated single source of truth for translation and formatting requirements.

## Core Guidelines
### 1. Project Structure & Module Organization
- All content is stored as sequentially numbered Markdown files at the repository root (e.g., `00-Table-of-Contents.md`, `07-Chapter-01.md`)
- Bilingual layout, chapter numbering, and content order must strictly follow specifications in `rules.md`
- New folders are prohibited unless pre-approved via discussion; images must use inline external links, or an `images/` folder may be proposed in pull requests (PRs) if required

### 2. Build, Test, and Development Commands
- Markdown preview: Use native editor preview (e.g., VS Code) for rapid content checks
- Optional link validation: Run `npx markdown-link-check [edited-file-path] -q` for each modified file
- Optional linting: Run `npx markdownlint-cli2 .` to resolve heading, list, and spacing inconsistencies
- Local server for image embedding: Run `python3 -m http.server` and access content at `http://localhost:8000/`

### 3. Coding Style & Naming Conventions
- `rules.md` is the single authoritative source for all translation rules
- File naming follows the `NN-Title.md` format, where `NN` is a 2-digit sequence number (e.g., `06-What-Makes-Agent.md`, `21-Chapter-15.md`)
- Bilingual formatting: Each English paragraph is immediately followed by its Chinese translation; short chapters may use separate dedicated English and Chinese sections
- Formatting requirements for Chinese content: Wrap Chinese text in `<mark>…</mark>` tags, and add spaces between Chinese text and English content/numbers
- Markdown standard: Use GitHub-flavored Markdown; apply 2-space indentation for lists; avoid unnecessary bold formatting

### 4. Pre-Submission Testing Requirements
- Mandatory pre-submission checks: No broken links, consistent terminology, matched English/Chinese paragraph pairs, valid Markdown rendering
- Tooling requirements: Run `markdownlint` and `markdown-link-check` on all modified files, with zero errors allowed
- Diff requirements: Keep changes focused; do not reflow unmodified original English source text

### 5. Commit & Pull Request (PR) Guidelines
- Commit messages must be written in English, following standardized prefixes:
  - `Add: [chapter] translation` for new translation work
  - `Update: [chapter] formatting` for formatting adjustments
  - `Fix: [issue] in [chapter]` for error resolution
- PR requirements: Include clear scope/intent, a list of modified files, rationale for any formatting decisions, and links to related issues; screenshots are recommended for complex formatting changes

### 6. Agent-Specific Contribution Rules
- Only modify explicitly targeted chapters; do not renumber any files
- Preserve original English text exactly without paraphrasing; apply all translations and formatting per `rules.md` specifications
- Keep contributions minimal and fully reversible; do not add tooling or configuration files without prior discussion and approval
