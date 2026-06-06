---
source: raw/05_代码与项目/skills/skills/template/SKILL.md
raw_sha256: eb685d91de039ed864fbd790cddf31684b017fd4a34ee1a55760d8d7cdbadefa
compiled_at: 2026-04-24T09:24:24.512Z
---
# SKILL.md Template (template-skill)
## Summary
This is a standard template file for building custom Claude-compatible skills, located at the source path `raw/05_代码与项目/skills/skills/template/SKILL.md`. It provides a pre-formatted scaffold for skill creators to define skill metadata and specific execution instructions.

## Template Structure & Placeholders
1. YAML Front Matter Metadata Block
   - `name`: A field for the unique identifier of the custom skill, with the default placeholder value `template-skill`
   - `description`: A field for explaining the skill's purpose and the conditions under which Claude should invoke the skill, intended to be replaced with custom descriptive content
2. Instruction Definition Section
   - A dedicated editable section marked with the heading `# Insert instructions below`, used to add detailed execution rules, workflow requirements, and operational constraints for the custom skill

## Raw Template Snippet
```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```
