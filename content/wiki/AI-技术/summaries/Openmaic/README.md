---
source: raw/Openmaic/README.md
raw_sha256: e10f772a6f8390b9c72a2d44f6a105f53dd9a0a77944ecb8a5402ff460d57278
compiled_at: 2026-04-24T05:14:02.003Z
---
# OpenMAIC-Feishu-Lab: AI 互动课堂与飞书多维表格融合平台
## 摘要
OpenMAIC-Feishu-Lab 是专为中国大陆企业环境设计的 AI 教育解决方案，通过深度整合清华大学开源的 OpenMAIC（多智能体互动课堂）与飞书多维表格（Bitable），零成本替代 Google Classroom，实现“教、学、测、管、统”全链路自动化。

## 核心价值
- **国产化适配**: 彻底解决 Google Classroom 访问限制，完全运行在飞书/企微生态内。
- **自动化教务**: 利用 Bitable 低代码能力，自动处理报名、邀请、成绩同步。
- **沉浸式学习**: 支持AI老师实时讲授、互动H5模拟实验、自动批改测验。
- **数据闭环**: 所有学习行为和成绩数据自动汇总至 Bitable，生成可视化报表。

## 功能模块
- **AI 课堂引擎**: 基于 OpenMAIC 开发，支持豆包（Doubao）模型。
- **飞书连接器**: 基于 OpenClaw Gateway 开发，负责处理消息转发与工具调用。
- **教务统计后台**: 基于飞书多维表格搭建，用于存储学生档案与成绩数据。

## 快速开始
### 外网访问地址
[https://tool.sysmex.com.cn/hr](https://tool.sysmex.com.cn/hr)

### 项目规范参考
- 详细技术规格：[spec.md](./spec/spec.md)
- 任务实施进度：[tasks.md](./spec/tasks.md)
- 验证核对表：[checklist.md](./spec/checklist.md)

### 部署指南参考
- 环境搭建：[DEPLOYMENT.md](raw/Openmaic/DEPLOYMENT.md)
- 飞书多维表格配置：[BITABLE_GUIDE.md](raw/Openmaic/BITABLE_GUIDE.md)
