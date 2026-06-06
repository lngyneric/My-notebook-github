---
source: raw/04_技能与工具/Superpowers/superpowers-main/RELEASE-NOTES.md
raw_sha256: f3e59420f1f1b19c464bfd798d6f90438c2145b80943ba9d06bd1a8bbf854936
compiled_at: 2026-04-24T06:58:22.434Z
---
<wiki>
# Superpowers Release Notes
## Summary
This document tracks all public releases of the **Superpowers** skill framework, a plugin for LLM development environments (Claude Code, Codex, OpenCode.ai) that provides standardized, reusable workflows for software engineering, problem-solving, research, and agent collaboration. All releases from v2.0.0 (October 2025) to v4.0.3 (December 2025) are documented below, organized in reverse chronological order.

---

## v4.0.3 (2025-12-26)
### Improvements
#### Strengthened using-superpowers skill for explicit skill requests
Resolved a failure mode where Claude would directly execute work instead of invoking a skill when explicitly requested by name (e.g., "subagent-driven-development, please"). Changes include:
- Updated core rule wording from "Check for skills" to "Invoke relevant or requested skills" to emphasize active invocation
- Added "BEFORE any response or action" requirement to prevent unprompted direct action
- Added reassurance that incorrect skill invocation is acceptable to reduce agent hesitation
- Added new red flag rule: "I know what that means" → Knowledge of a concept does not equal proper skill usage

#### Added explicit skill request tests
New test suite located at `tests/explicit-skill-requests/` that verifies Claude correctly invokes named skills across both single-turn and multi-turn interaction scenarios.

---

## v4.0.2 (2025-12-23)
### Fixes
#### Slash commands now user-only
Added `disable-model-invocation: true` to all three slash commands (`/brainstorm`, `/execute-plan`, `/write-plan`). These commands are now restricted to manual user invocation only, and cannot be triggered by Claude via the Skill tool. The underlying skills (`superpowers:brainstorming`, `superpowers:executing-plans`, `superpowers:writing-plans`) remain available for autonomous Claude invocation, eliminating confusion from redundant command-to-skill redirects.

---

## v4.0.1 (2025-12-23)
### Fixes
#### Clarified how to access skills in Claude Code
Fixed a pattern where Claude would invoke a skill via the Skill tool then separately read the skill file. The `using-superpowers` skill now explicitly states the Skill tool loads skill content directly, with no separate file read required. Additional changes:
- Added dedicated "How to Access Skills" section to `using-superpowers`
- Updated instruction wording from "read the skill" to "invoke the skill"
- Updated slash commands to use fully qualified skill names (e.g., `superpowers:brainstorming`)

#### Other Fixes
- Added GitHub thread reply guidance to `receiving-code-review` (h/t @ralphbean), instructing users to reply to inline review comments in their original thread rather than as top-level PR comments
- Added automation-over-documentation guidance to `writing-skills` (h/t @EthanJStark), specifying that mechanical constraints should be automated rather than documented, with skills reserved for judgment calls.

---

## v4.0.0 (2025-12-17)
### New Features
#### Two-stage code review in subagent-driven-development
Subagent workflows now implement two sequential, looping review stages after each task:
1. **Spec compliance review**: Skeptical reviewer verifies implementation matches exact requirements by reading actual code (not trusting implementer reports) to catch missing requirements and over-building.
2. **Code quality review**: Runs only after spec compliance passes, evaluating for clean code, test coverage, and maintainability.

Reviews are iterative, not one-shot: implementers fix identified issues, then reviewers re-validate. Additional subagent workflow improvements:
- Controller provides full task text to workers instead of only file references
- Workers may ask clarifying questions both before and during work
- Required self-review checklist before work completion reporting
- Plan read once at workflow start and extracted to TodoWrite

New supporting prompt templates in `skills/subagent-driven-development/`:
- `implementer-prompt.md` (includes self-review checklist, encourages clarifying questions)
- `spec-reviewer-prompt.md` (skeptical requirement verification)
- `code-quality-reviewer-prompt.md` (standard code review framework)

#### Debugging techniques consolidated with tools
The `systematic-debugging` skill now bundles all supporting techniques and utility tools:
- `root-cause-tracing.md` (backward call stack bug tracing)
- `defense-in-depth.md` (multi-layer validation)
- `condition-based-waiting.md` (replacement for arbitrary timeouts with condition polling)
- `find-polluter.sh` (bisection script to identify test pollution sources)
- `condition-based-waiting-example.ts` (production implementation from real debugging sessions)

#### Testing anti-patterns reference
The `test-driven-development` skill now includes `testing-anti-patterns.md` covering common bad practices:
- Testing mock behavior instead of real system behavior
- Adding test-only methods to production classes
- Mocking dependencies without full understanding
- Incomplete mocks that hide structural assumptions

#### Skill test infrastructure
Three dedicated test frameworks for validating skill behavior:
1. `tests/skill-triggering/`: Validates skills activate from naive prompts without explicit naming, testing 6 core skills to confirm description-only triggering works.
2. `tests/claude-code/`: Headless integration tests using `claude -p`, with transcript (JSONL) analysis to verify skill usage, plus `analyze-token-usage.py` for cost tracking.
3. `tests/subagent-driven-dev/`: End-to-end workflow validation with two complete test projects:
   - `go-fractals/`: CLI tool with Sierpinski/Mandelbrot fractal generation (10 tasks)
   - `svelte-todo/`: CRUD app with localStorage and Playwright testing (12 tasks)

### Major Changes
#### DOT flowcharts as executable specifications
Key skills rewritten to use DOT/GraphViz flowcharts as the authoritative process definition, with prose as supporting content only.
##### The Description Trap
Documented in `writing-skills`: Skill descriptions that include workflow summaries override detailed flowchart content, as Claude prioritizes short descriptions over full documentation. Fix: skill descriptions must be trigger-only ("Use when X") with no process details.

#### Skill priority logic updated
In `using-superpowers`, process skills (brainstorming, debugging) now explicitly take priority over implementation skills when multiple skills apply. For example, a "Build X" request triggers brainstorming first, then relevant domain-specific implementation skills.

#### Strengthened brainstorming trigger
Brainstorming skill description updated to imperative language: "You MUST use this before any creative work—creating features, building components, adding functionality, or modifying behavior."

### Breaking Changes
#### Skill consolidation
Six standalone skills merged into parent skills to reduce fragmentation:
- `root-cause-tracing`, `defense-in-depth`, `condition-based-waiting` → bundled into `systematic-debugging/`
- `testing-skills-with-subagents` → bundled into `writing-skills/`
- `testing-anti-patterns` → bundled into `test-driven-development/`
- `sharing-skills` removed (marked obsolete)

### Other Improvements
- Added `render-graphs.js` tool to extract DOT diagrams from skills and render to SVG
- Added scannable Rationalizations table in `using-superpowers` with new evasion pattern entries: "I need more context first", "Let me explore first", "This feels productive"
- Added `docs/testing.md` guide for running skill integration tests with Claude Code

---

## v3.6.2 (2025-12-03)
### Fixed
#### Linux Compatibility
Fixed polyglot hook wrapper (`run-hook.cmd`) to use POSIX-compliant syntax:
- Replaced bash-specific `${BASH_SOURCE[0]:-$0}` with standard `$0` on line 16
- Resolves "Bad substitution" error on Ubuntu/Debian systems where `/bin/sh` defaults to dash
- Fixes issue #141

---

## v3.5.1 (2025-11-24)
### Changed
#### OpenCode Bootstrap Refactor
Switched from `chat.message` hook to `session.created` event for bootstrap injection:
- Bootstrap injected at session creation via `session.prompt()` with `noReply: true`
- Explicitly notifies the model that `using-superpowers` is pre-loaded to prevent redundant skill loading
- Consolidated bootstrap content generation into shared `getBootstrapContent()` helper
- Replaced fallback pattern with clean single-implementation approach

---

## v3.5.0 (2025-11-23)
### Added
#### OpenCode Support
Native JavaScript plugin for OpenCode.ai, including:
- Custom tools: `use_skill` and `find_skills`
- Message insertion pattern for skill persistence across context compaction
- Automatic context injection via `chat.message` hook
- Auto
