---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/claude-suggested-it.txt
raw_sha256: 6756c2c9f7f5de21d21f2371526032386bf69c6d9684b108e8df0d622eb65d54
compiled_at: 2026-04-15T00:36:21.486Z
---
# Claude 项目执行方案对话示例
## 摘要
本页面记录了一次身份验证系统开发计划完成后，用户选择子代理驱动开发作为执行方案的对话过程，展示了开发计划落地前对执行方式的选择场景。

## 对话流程
1. 前序助手输出：计划已完成并保存至`docs/plans/auth-system.md`，提供两种执行方案供选择
2. 用户确认选择：子代理驱动开发方式

## 关键执行方案说明
| 方案名称 | 核心特点 |
| --- | --- |
| 子代理驱动（当前会话） | 每个任务分配全新子agent，任务间需审核，当前对话内可快速迭代 |
| 并行会话（独立会话） | 开启新的Claude Code会话使用执行计划技能，批量执行并设置审核检查点 |
