---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/requesting-code-review/SKILL.md
raw_sha256: 2da31af22a58938ab78f3ee6d5b4687fcca062b923b646459eb52ba72117ef97
compiled_at: 2026-04-14T16:53:42.213Z
---
# Requesting Code Review
## 摘要
Requesting Code Review是Superpowers开发框架中的一项技能，用于在开发流程中通过调度`code-reviewer`子代理提前发现代码问题，核心原则为**早审查，常审查**，明确了申请代码审查的时机、操作流程、使用示例以及工作流整合规则和禁忌。

## 核心原则
Review early, review often（早审查，常审查），通过提前审查避免问题累积扩大。

## 申请时机
### 强制申请场景
- 子代理驱动开发完成每个任务后
- 完成主要功能开发后
- 合并到主分支前

### 可选推荐申请场景
- 开发卡住时（可提供全新视角）
- 重构前（进行基线检查）
- 修复复杂Bug后

## 操作流程
1. **获取Git提交哈希**
   通过Git命令获取基准提交哈希和当前提交哈希，示例命令：
   ```bash
   BASE_SHA=$(git rev-parse HEAD~1)  # 也可使用origin/main
   HEAD_SHA=$(git rev-parse HEAD)
   ```
2. **调度code-reviewer子代理**
   使用Task工具选择`superpowers:code-reviewer`类型，填写`code-reviewer.md`模板，模板占位说明：
   | 占位符 | 说明 |
   |--------|------|
   | `{WHAT_WAS_IMPLEMENTED}` | 本次完成的开发内容 |
   | `{PLAN_OR_REQUIREMENTS}` | 需求或开发计划 |
   | `{BASE_SHA}` | 起始提交哈希 |
   | `{HEAD_SHA}` | 结束提交哈希 |
   | `{DESCRIPTION}` | 变更简要说明 |
3. **根据反馈处理**
   - 严重问题（Critical）：立即修复
   - 重要问题（Important）：继续开发前必须修复
   - 次要问题（Minor）：可后续处理
   - 评审者出错：可带着合理依据反驳

## 使用示例
```
[Just completed Task 2: Add verification function]

You: Let me request code review before proceeding.

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[Dispatch superpowers:code-reviewer subagent]
  WHAT_WAS_IMPLEMENTED: Verification and repair functions for conversation index
  PLAN_OR_REQUIREMENTS: Task 2 from docs/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types

[Subagent returns]:
  Strengths: Clean architecture, real tests
  Issues:
    Important: Missing progress indicators
    Minor: Magic number (100) for reporting interval
  Assessment: Ready to proceed

You: [Fix progress indicators]
[Continue to Task 3]
```

## 与开发工作流的整合
- **子代理驱动开发**：每个任务完成后都进行审查，在问题累积前发现并修复，再进入下一个任务
- **计划执行**：每完成一批（3个任务）进行审查，获取并应用反馈后再继续
- **临时开发**：合并前审查、卡住时审查

## 禁忌与注意事项
### 绝对禁止
- 以"代码简单"为由跳过审查
- 忽略严重问题
- 带着未修复的重要问题继续开发
- 对合理的技术反馈无意义争论

### 评审者出错的处理方式
- 带着技术依据反驳
- 展示能证明代码可用的代码或测试
- 请求评审者澄清

## 相关资源
审查模板见：`requesting-code-review/code-reviewer.md`
