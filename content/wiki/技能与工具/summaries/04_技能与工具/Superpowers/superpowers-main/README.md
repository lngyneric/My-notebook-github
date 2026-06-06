---
source: raw/04_技能与工具/Superpowers/superpowers-main/README.md
raw_sha256: 0f2b0a3dcf43fc34961f615d5379e105a382bb24ba9ebcd90a25a7a8d6edbb80
compiled_at: 2026-04-24T06:55:48.361Z
---
# Superpowers
## Summary
Superpowers is a complete software development workflow for coding agents, built on top of a set of composable "skills" and initial instructions that ensure agents utilize the system properly. It enforces structured, test-driven development practices and enables autonomous agent operation with built-in guardrails.

## How It Works
1. Upon activating a coding agent, the system does not immediately generate code. Instead, it first elicits clear project requirements from the user through conversation.
2. It presents the derived specification in short, digestible chunks for user review and sign-off.
3. After design approval, the agent creates a detailed, low-level implementation plan suitable for inexperienced engineers to follow, emphasizing red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY principles.
4. Once the user approves the plan, the system launches a subagent-driven-development process: agents work through individual engineering tasks, with work inspected and reviewed at each stage. Claude-based implementations often operate autonomously for multiple hours without deviating from the agreed plan.
5. All skills trigger automatically, requiring no special user action to activate.

## Installation
Installation procedures vary by platform:
### Claude Code (via Plugin Marketplace)
1. Register the official marketplace first:
   ```bash
   /plugin marketplace add obra/superpowers-marketplace
   ```
2. Install the plugin from the registered marketplace:
   ```bash
   /plugin install superpowers@superpowers-marketplace
   ```
### Verify Installation
Run the help command to confirm core commands are available:
```bash
/help
```
Expected output includes:
- `/superpowers:brainstorm` - Interactive design refinement
- `/superpowers:write-plan` - Create implementation plan
- `/superpowers:execute-plan` - Execute plan in batches

### Codex
Instruct Codex to fetch and follow official setup instructions:
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```
Detailed platform documentation: [docs/README.codex.md](docs/README.codex.md)

### OpenCode
Instruct OpenCode to fetch and follow official setup instructions:
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```
Detailed platform documentation: [docs/README.opencode.md](docs/README.opencode.md)

## Basic Workflow
All workflows are mandatory (not suggestions) and agents automatically check for relevant skills before starting any task:
1. **brainstorming**: Activates before writing code. Refines rough ideas through targeted questions, explores alternative approaches, presents design in segmented sections for user validation, and saves a formal design document.
2. **using-git-worktrees**: Activates after design approval. Creates an isolated workspace on a new dedicated branch, runs project dependency setup, and verifies a clean test baseline before implementation begins.
3. **writing-plans**: Activates with a fully approved design. Breaks work into 2-5 minute bite-sized tasks, each with exact file paths, complete code specifications, and explicit verification steps.
4. **subagent-driven-development / executing-plans**: Activates with a finalized plan. Dispatches a fresh subagent per task with two-stage review (spec compliance first, then code quality), or executes tasks in batches with scheduled human checkpoints.
5. **test-driven-development**: Activates during implementation. Enforces the RED-GREEN-REFACTOR cycle: write a failing test, confirm the test fails as expected, write minimal code to pass the test, confirm the test passes, commit changes. Automatically deletes any code written before corresponding tests.
6. **requesting-code-review**: Activates between task completions. Reviews completed work against the official plan, reports issues by severity level, and blocks further progress for critical compliance issues.
7. **finishing-a-development-branch**: Activates when all planned tasks are complete. Verifies full test suite status, presents workflow options (merge/PR/keep/discard), and cleans up the temporary development worktree.

## Skills Library
The system includes a composable library of pre-built skills organized by functional category:
### Testing
- **test-driven-development**: Implements the RED-GREEN-REFACTOR cycle, including a reference for common testing anti-patterns.
### Debugging
- **systematic-debugging**: 4-phase root cause identification process, including root-cause-tracing, defense-in-depth, and condition-based-waiting techniques.
- **verification-before-completion**: Ensures bugs are actually resolved before marking work as complete.
### Collaboration
- **brainstorming**: Socratic method-based design refinement.
- **writing-plans**: Generates detailed, low-level implementation plans.
- **executing-plans**: Batch task execution with structured human checkpoints.
- **dispatching-parallel-agents**: Concurrent subagent workflow management.
- **requesting-code-review**: Pre-review compliance checklist against project plans.
- **receiving-code-review**: Structured workflow for responding to code review feedback.
- **using-git-worktrees**: Manages isolated parallel development branches.
- **finishing-a-development-branch**: Structured workflow for merge/PR decision making.
- **subagent-driven-development**: Fast iteration with two-stage review (spec compliance first, then code quality).
### Meta
- **writing-skills**: Official guide to creating new Superpowers skills following established best practices, including skill testing methodology.
- **using-superpowers**: Introduction to the Superpowers skills system for new users and agents.

## Philosophy
The system is built on four core guiding principles:
1. **Test-Driven Development**: Write tests first, without exception.
2. **Systematic over ad-hoc**: Prioritize structured process over guesswork.
3. **Complexity reduction**: Treat simplicity as the primary design goal.
4. **Evidence over claims**: Verify outcomes with concrete proof before declaring success.

Additional background reading: [Superpowers for Claude Code](https://blog.fsck.com/2025/10/09/superpowers/)

## Contributing
All skills are hosted directly in the main public repository. To contribute new skills or improvements:
1. Fork the official repository.
2. Create a dedicated branch for your new skill or improvement.
3. Follow the `writing-skills` skill guidelines for creating and testing new Superpowers skills.
4. Submit a pull request for review.

Full skill creation guide: `skills/writing-skills/SKILL.md`

## Updating
All skills update automatically when the core plugin is updated via Claude Code:
```bash
/plugin update superpowers
```

## License
Released under the MIT License. See the LICENSE file in the repository for full terms.

## Support
- Official issue tracker: https://github.com/obra/superpowers/issues
- Official plugin marketplace: https://github.com/obra/superpowers-marketplace

## Sponsorship
If Superpowers has enabled commercial work, consider sponsoring the open source maintainer: [sponsor obra's opensource work](https://github.com/sponsors/obra)
