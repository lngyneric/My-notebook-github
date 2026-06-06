---
source: raw/05_代码与项目/skills/skills/skills/internal-comms/examples/3p-updates.md
raw_sha256: 087e4363c0f3513728a7e695eeb9ead5c3ecd12a4681b59340691180e65b68fc
compiled_at: 2026-04-14T05:19:41.411Z
---
# 3P 更新（Progress, Plans, Problems）写作指南

> [!NOTE] TL;DR
> 3P 更新是面向管理层、团队成员的极简同步文档，要求30-60秒内读完，结构固定为「已完成进展/下一步计划/阻塞问题」三部分，通常按周更新，覆盖一个团队/全公司的工作。

---

## 要点

### 基本定义与受众
- 全称是 **Progress（进展）、Plans（计划）、Problems（问题）**，是团队状态同步文档
- 核心受众：高管、领导层、跨团队协作同事，受众对团队工作仅有基础背景了解
- 要求：极其简洁，阅读时间控制在30-60秒以内
- 适用范围：覆盖任意规模的团队（从小组到全公司），团队规模越大，内容颗粒度越粗

### 核心结构
固定包含三个模块，覆盖周期通常为一周：
1. **Progress（进展）**：总结周期内（一般为过去一周）团队完成的工作，聚焦交付成果、达成的里程碑
2. **Plans（计划）**：规划下一个周期（一般为未来一周）的工作，聚焦团队最高优先级事项
3. **Problems（问题）**：列出当前阻碍团队推进的问题，例如人员不足、外部阻塞、项目失败等

### 前置准备
写作前需要确认信息：
- 必须明确**团队名称**，未指定时需要主动询问
- 确认更新覆盖的时间范围

### 信息收集规则
优先从已有公开渠道拉取信息：
- Slack：团队成员发布的更新（优先选择大频道、高互动的内容）
- Google Drive：核心成员撰写的高访问量文档
- Email：高互动、内容相关的邮件
- Calendar：重要的非重复会议（例如产品评审会）

收集范围匹配对应模块的时间要求：
- Progress：收集一周前到今日的信息
- Plans：收集今日到未来一周的信息
- Problems：收集一周前到今日的信息
- 无访问权限时，可以直接询问需求方获取内容，仅需做格式整理

### 标准工作流
1. 澄清范围：确认团队名称和时间范围
2. 收集信息：通过可用工具获取或直接向用户询问
3. 撰写初稿：严格遵循格式规范
4. 审核确认：确保符合长度要求（30-60秒阅读）、内容数据化

### 强制格式规范
格式固定，不允许使用额外格式，必须遵循以下结构：
```
[选择匹配团队氛围的emoji] [团队名称] (覆盖日期，通常为一周)
Progress: [1-3句话内容]
Plans: [1-3句话内容]
Problems: [1-3句话内容]
```
格式要求补充：
- 每个模块最多1-3句话，要求清晰直给
- 优先使用数据、量化指标支撑内容
- 语气客观平实，避免冗余描述

---

## 引用原始证据片段
> 来源：`raw/05_代码与项目/skills/skills/skills/internal-comms/examples/3p-updates.md`
>
> ## Instructions
> You are being asked to write a 3P update. 3P updates stand for "Progress, Plans, Problems." The main audience is for executives, leadership, other teammates, etc. They're meant to be very succinct and to-the-point: think something you can read in 30-60sec or less. They're also for people with some, but not a lot of context on what the team does.
>
> 3Ps can cover a team of any size, ranging all the way up to the entire company. The bigger the team, the less granular the tasks should be. For example, "mobile team" might have "shipped feature" or "fixed bugs," whereas the company might have really meaty 3Ps, like "hired 20 new people" or "closed 10 new deals." 
>
> They represent the work of the team across a time period, almost always one week. They include three sections:
> 1) Progress: what the team has accomplished over the next time period. Focus mainly on things shipped, milestones achieved, tasks created, etc.
> 2) Plans: what the team plans to do over the next time period. Focus on what things are top-of-mind, really high priority, etc. for the team.
> 3) Problems: anything that is slowing the team down. This could be things like too few people, bugs or blockers that are preventing the team from moving forward, some deal that fell through, etc.
>
> Before writing them, make sure that you know the team name. If it's not specified, you can ask explicitly what the team name you're writing for is.
>
>
> ## Tools Available
> Whenever possible, try to pull from available sources to get the information you need:
> - Slack: posts from team members with their updates - ideally look for posts in large channels with lots of reactions
> - Google Drive: docs written from critical team members with lots of views
> - Email: emails with lots of responses of lots of content that seems relevant
> - Calendar: non-recurring meetings that have a lot of importance, like product reviews, etc.
>
>
> Try to gather as much context as you can, focusing on the things that covered the time period you're writing for:
> - Progress: anything between a week ago and today
> - Plans: anything from today to the next week
> - Problems: anything between a week ago and today
>
>
> If you don't have access, you can ask the user for things they want to cover. They might also include these things to you directly, in which case you're mostly just formatting for this particular format.
>
> ## Workflow
>
> 1. **Clarify scope**: Confirm the team name and time period (usually past week for Progress/Problems, next
> week for Plans)
> 2. **Gather information**: Use available tools or ask the user directly
> 3. **Draft the update**: Follow the strict formatting guidelines
> 4. **Review**: Ensure it's concise (30-60 seconds to read) and data-driven
>
> ## Formatting
>
> The format is always the same, very strict formatting. Never use any formatting other than this. Pick an emoji that is fun and captures the vibe of the team and update.
>
> [pick an emoji] [Team Name] (Dates Covered, usually a week)
> Progress: [1-3 sentences of content]
> Plans: [1-3 sentences of content]
> Problems: [1-3 sentences of content]
>
> Each section should be no more than 1-3 sentences: clear, to the point. It should be data-driven, and generally include metrics where possible. The tone should be very matter-of-fact, not super prose-heavy.

---

> [!WARNING] 冲突：原始文本中Progress模块描述存在笔误，原文写为`what the team has accomplished over the next time period`，与后文时间范围规则（Progress对应过去一周）矛盾，此处已在要点部分按照上下文逻辑修正，保留原始笔误在引用证据中。
