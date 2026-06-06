---
source: raw/05_代码与项目/skills/skills/skills/skill-creator/references/workflows.md
raw_sha256: ef4846877d5dab47511a01a6cf31476ad64f5bc5945635459295794575338980
compiled_at: 2026-04-14T05:19:26.359Z
---
# 工作流模式
> 来源路径：`raw/05_代码与项目/skills/skills/skills/skill-creator/references/workflows.md`

---

## TL;DR
针对不同复杂度和逻辑类型的任务，有两种通用工作流编写模式可以引导Skill Creator处理任务：顺序工作流适用于无分支的复杂任务，条件工作流适用于带有分支逻辑的任务，都需要在`SKILL.md`开头明确声明给Claude。

---

## 要点
1. **顺序工作流（Sequential Workflows）**
   - 适用场景：无分支逻辑的复杂任务
   - 使用方式：将操作拆解为清晰的连续步骤，在`SKILL.md`开头向Claude提供流程总览
2. **条件工作流（Conditional Workflows）**
   - 适用场景：带有分支决策逻辑的任务
   - 使用方式：在决策点明确分支判断规则，分别定义不同分支对应的工作步骤

---

## 引用证据片段
### 原始完整内容
# Workflow Patterns

## Sequential Workflows

For complex tasks, break operations into clear, sequential steps. It is often helpful to give Claude an overview of the process towards the beginning of SKILL.md:

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

## Conditional Workflows

For tasks with branching logic, guide Claude through decision points:

```markdown
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```
---

> [!WARNING] 冲突：本页面暂未收录其他来源内容，未发现冲突
