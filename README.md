# EL-Notepad — 多领域个人维基

Karpathy LLM Wiki 模式的多领域个人知识库。

## 内容结构

| 领域 | raw | wiki | 说明 |
|---|---|---|---|
| HR-培训 | 128 | 122 | 人资资源管理与培训体系 |
| AI-技术 | 12 | 441 | AI/LLM/RAG/Agent 技术 |
| 代码与项目 | 483 | 331 | 代码项目、脚本工具 |
| 技能与工具 | 163 | 221 | 工具使用指南、工作流 |
| 阅读-Books | 14 | 102 | 图书笔记、阅读记录 |
| 工作记录 | 7 | 28 | 每日报表、工作日志 |

总计: raw 807 文件, wiki 1245 页面

## 工作流程

INGEST  → raw/<领域>/
COMPILE → wiki/<领域>/
QUERY   → index.md 查找
LINT    → 检查矛盾/孤立

## 部署

Quartz v5 → Cloudflare Pages