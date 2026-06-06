---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/i-know-what-sdd-means.txt
raw_sha256: edff356687a337deb4b86f285fff0e700c2a92d620b36b4541df1dc0d4cbd4df
compiled_at: 2026-04-15T00:36:29.985Z
---
# 子代理驱动开发任务请求记录
## 摘要
这是一份开发者发起的，基于已有的身份验证系统实现方案，使用子代理驱动开发模式执行该方案的任务请求文档。

## 关键要点
1. 开发者已完成身份验证系统的实现方案，方案存储路径为`docs/plans/auth-system.md`
2. 请求采用子代理驱动开发（subagent-driven-development）模式执行该实现方案
3. 子代理驱动开发的执行要求：
   - 为方案中的每一个任务单独分派一个全新子代理
   - 任务与任务之间需要对输出内容进行审核
   - 在当前对话中保持快速迭代

## 任务起始要求
请求先读取实现方案，然后开始为每个任务分派对应子代理启动工作。
