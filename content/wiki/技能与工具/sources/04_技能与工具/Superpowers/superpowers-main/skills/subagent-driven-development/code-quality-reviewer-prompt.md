---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/subagent-driven-development/code-quality-reviewer-prompt.md
raw_sha256: 11de35dba7990f9def49b90039f1f2d8e7f546ae42ca8e1105d308f09456803e
compiled_at: 2026-04-14T16:53:49.052Z
---
# Code Quality Reviewer Prompt Template
## 摘要
Code Quality Reviewer Prompt Template 是在智能代理开发流程中，用于调度代码质量审查子代理的模板，用于验证代码实现的质量，仅在规范合规性审查通过后才可调度。

## 关键要点
- 该模板用于在子代理驱动开发流程中分派代码质量审查子代理
- 用途为验证代码实现是否结构清晰、经过测试、可维护
- 必须在规范合规性审查通过之后才能分派该任务
- 代码质量审查子代理完成工作后需要返回：代码优势、问题（按严重程度分为关键/重要/次要）、整体评估

## 任务参数模板
调用代码质量审查子代理需要填充以下任务参数：
```
Task tool (superpowers:code-reviewer):
  Use template at requesting-code-review/code-reviewer.md

  WHAT_WAS_IMPLEMENTED: [来自实现者的报告]
  PLAN_OR_REQUIREMENTS: 任务N来自[计划文件]
  BASE_SHA: [任务开始前的提交哈希]
  HEAD_SHA: [当前提交哈希]
  DESCRIPTION: [任务摘要]
```
