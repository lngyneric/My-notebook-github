---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/mid-conversation-execute-plan.txt
raw_sha256: 6706967cca9423cf9efa8e45e1034c336204061fa5d24c1aef0402d254d6cb05
compiled_at: 2026-04-15T00:36:39.871Z
---
# Mid-conversation Execute Plan Prompt
## 摘要
该文本是一段在对话中间发起的技能调用请求，请求子代理驱动开发工具执行预编写好的计划文档。
## 关键要点
1. 已经完成计划编写，计划文档存放路径为`docs/plans/auth-system.md`
2. 需要实现该认证系统计划
3. 调用的技能为`subagent-driven-development`（子代理驱动开发）
## 请求内容
请求文本：`I have a plan at docs/plans/auth-system.md that's ready to implement. subagent-driven-development, please`
