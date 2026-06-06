---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/brainstorming/SKILL.md
raw_sha256: 206c63e80d38c57e6afc657296332b1d0ff75572435d75c079e7407b26762ecd
compiled_at: 2026-04-14T16:52:09.802Z
---
# 头脑风暴（Brainstorming）
## 摘要
头脑风暴（Brainstorming）是一项用于在任何创造性工作（功能开发、组件搭建、功能新增、行为修改等）开展前，通过协作对话将想法转化为完整设计与规范的技能，核心目标是在开发前梳理清楚用户意图、需求与设计方向，遵循一次一问、优先多选、探索备选等核心原则推进。

## 关键要点
### 适用场景
所有创造性工作开展前必须使用，包括创建功能、搭建组件、新增功能、修改行为等场景，用于在落地实施前探索用户意图、需求与设计方向。

### 完整流程
1. **理解想法阶段**
   - 先查看当前项目状态（文件、文档、最近提交）
   - 一次只提一个问题来细化想法，优先使用选择题，开放式问题也可
   - 重点聚焦理解目标、约束和成功标准
2. **探索方案阶段**
   - 提出2-3种不同方案并说明各自的权衡
   - 以对话形式呈现选项，给出推荐方案并说明理由，优先展示推荐选项
3. **提交设计阶段**
   - 理清需求后分模块展示设计，每个模块控制在200-300字
   - 每个模块展示完成后确认方案是否符合要求，需覆盖架构、组件、数据流、错误处理、测试等内容
   - 随时准备根据反馈回溯澄清

### 设计完成后续工作
1. **文档留存**：将验证通过的设计写入`docs/plans/YYYY-MM-DD-<topic>-design.md`，可使用清晰写作技能优化，提交到git
2. **开发准备**：确认是否进入开发阶段，使用git worktree创建隔离工作区，生成详细实施计划

### 核心原则
- 一次只提一个问题，避免信息过载
- 条件允许时优先使用选择题，更易获得回答
- 严格遵循YAGNI原则，从设计中移除不必要功能
- 敲定方案前必须提出2-3种备选方案
- 分模块展示设计，逐模块验证确认
- 保持灵活，遇到歧义及时回溯澄清

## 证据片段
> "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."

> "Propose 2-3 different approaches with trade-offs, Present options conversationally with your recommendation and reasoning, Lead with your recommended option and explain why"

> "Once you believe you understand what you're building, present the design, Break it into sections of 200-300 words, Ask after each section whether it looks right so far"
