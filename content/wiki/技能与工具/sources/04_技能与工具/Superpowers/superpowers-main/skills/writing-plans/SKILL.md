---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/writing-plans/SKILL.md
raw_sha256: 2046e5b955aa16c288f9c7290c58f237628dfb6ba6d4817fad3da0fa830b46c2
compiled_at: 2026-04-15T00:36:00.035Z
---
# Writing Plans
## 摘要
Writing Plans 是一种面向无代码库上下文开发者的多步骤开发任务实现规划技能，用于拿到需求规范后开发代码前编写完整的落地计划，遵循TDD、小步提交等原则，将开发拆解为颗粒度极小的任务，明确所有所需信息后提供两种执行方式选择。

## 关键要点
- **使用时机**：拿到多步骤任务的规范/需求后，开发代码前使用
- **适用对象**：假设执行者是熟练开发者，但对当前工具集、问题域几乎不了解，且不熟悉良好的测试设计
- **存储位置**：计划文件需保存至 `docs/plans/YYYY-MM-DD-<feature-name>.md`
- **任务颗粒度要求**：每个步骤仅对应一个2-5分钟可完成的操作
- **强制规范**：计划必须包含指定格式的开头头信息，每个任务需要明确涉及的精确文件路径、完整代码、执行命令与预期结果
- **核心原则**：遵循DRY（不要重复自己）、YAGNI（你不会需要它）、TDD（测试驱动开发）、频繁提交

## 使用规则
1. 使用时需要在开头声明："I'm using the writing-plans skill to create the implementation plan."
2. 需要在通过brainstorming技能创建的独立工作树中运行本技能

## 文档结构规范
### 强制开头Header
所有计划必须以以下格式开头：
```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

### 单任务结构规范
每个任务需要明确组件名称、涉及文件，再按TDD流程拆解为五个标准小步骤：
1. 编写失败的测试，提供完整测试代码
2. 运行测试验证失败，给出精确执行命令与预期失败结果
3. 编写最简实现代码，提供完整代码
4. 运行测试验证通过，给出精确执行命令与预期结果
5. 提交代码，给出精确git命令

## 执行交付流程
计划保存完成后，需要提供两种执行方案供选择：
1. **子代理驱动（当前会话）**：每个任务分派一个新的子代理，任务间进行评审，使用 `superpowers:subagent-driven-development` 子技能
2. **并行会话（独立会话）**：在工作树中打开新会话，使用 `superpowers:executing-plans` 子技能批量执行
