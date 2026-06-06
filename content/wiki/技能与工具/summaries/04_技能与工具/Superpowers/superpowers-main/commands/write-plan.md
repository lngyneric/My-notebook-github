---
source: raw/04_技能与工具/Superpowers/superpowers-main/commands/write-plan.md
raw_sha256: 4da2b0643834f3adaacb23d5ce2f3ee71cf191f0ab8d06f83893aed752912384
compiled_at: 2026-04-24T08:45:04.465Z
---
# write-plan Command
## Summary
The `write-plan` command is a Superpowers utility designed to generate detailed implementation plans composed of small, manageable bite-sized tasks.

## Core Configuration
This command has a fixed enabled configuration setting:
- `disable-model-invocation: true`: Prevents additional model invocation during the execution of this command.

## Execution Rule
When activated, the `write-plan` command strictly invokes the `superpowers:writing-plans` skill, and must follow the specifications of that skill exactly for all related output.
