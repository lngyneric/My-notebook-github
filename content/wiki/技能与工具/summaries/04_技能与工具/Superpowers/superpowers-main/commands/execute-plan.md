---
source: raw/04_技能与工具/Superpowers/superpowers-main/commands/execute-plan.md
raw_sha256: f9a7c251381f9a0466a3e67b9000ec59c5bd9665419b248d1c3887a9212d70ad
compiled_at: 2026-04-24T08:44:37.289Z
---
# execute-plan Command (Superpowers)
## Summary
This is a dedicated command under the Superpowers framework, configured to execute plans in batches with review checkpoints, disable model invocation by default, and require strict compliance with the specified skill during execution.
## Key Points
1. **Core Function**: Execute plans in batches with review checkpoints
2. **Built-in Configuration**: Has `disable-model-invocation` set to `true`
3. **Execution Requirement**: Must invoke the `superpowers:executing-plans` skill and follow it exactly as specified
## Evidence Fragment
```
---
description: Execute plan in batches with review checkpoints
disable-model-invocation: true
---

Invoke the superpowers:executing-plans skill and follow it exactly as presented to you
```
