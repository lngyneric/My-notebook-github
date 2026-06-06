---
source: raw/04_技能与工具/Superpowers/superpowers-main/commands/brainstorm.md
raw_sha256: abda7c079ddd59e3a856cc933b83460f9d0bc02a8aba09a4650d67f75338bf02
compiled_at: 2026-04-24T08:44:15.995Z
---
# superpowers: brainstorm Command
## Summary
This is a mandatory pre-implementation superpower command, required to be executed before any creative work including feature creation, component building, functionality addition, or behavior modification. It is designed for pre-implementation requirement and design exploration, and requires exact adherence to the `superpowers:brainstorming` skill upon invocation.

## Core Specifications & Rules
1. **Mandatory Usage Trigger**: Must be used before all creative development or behavior modification work, with no exceptions for the defined work categories.
2. **Core Function**: Conduct structured exploration of requirements and design specifications prior to any implementation activity.
3. **Invocation Requirement**: Must explicitly invoke the `superpowers:brainstorming` skill and follow its presented specifications exactly.
4. **Base Configuration**: Has the `disable-model-invocation` flag set to `true` in its default configuration.

## Raw Source Snippet
```markdown
---
description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores requirements and design before implementation."
disable-model-invocation: true
---

Invoke the superpowers:brainstorming skill and follow it exactly as presented to you
```
