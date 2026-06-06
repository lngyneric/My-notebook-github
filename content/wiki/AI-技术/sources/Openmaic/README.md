---
source: raw/Openmaic/README.md
raw_sha256: e10f772a6f8390b9c72a2d44f6a105f53dd9a0a77944ecb8a5402ff460d57278
compiled_at: 2026-04-14T03:48:39.417Z
---
# OpenMAIC-Feishu-Lab
> [!NOTE] TL;DR
> OpenMAIC-Feishu-Lab 是适配中国大陆企业环境的AI教育解决方案，深度整合清华大学开源OpenMAIC多智能体互动课堂与飞书多维表格，可零成本替代Google Classroom，实现教、学、测、管、统计全链路自动化。

## 基础信息
| 项目 | 说明 |
|------|------|
| 定位 | 中国大陆企业环境AI互动课堂与飞书多维表格融合平台 |
| 核心能力 | 国产化替代Google Classroom，全链路教务自动化 |

---

## 核心要点
### 核心价值
1. **国产化适配**：彻底解决Google Classroom访问限制，完全运行在飞书/企业微信生态内
2. **自动化教务**：依托飞书多维表格低代码能力，自动处理报名、邀请、成绩同步流程
3. **沉浸式学习**：支持AI老师实时讲授、互动H5模拟实验、自动批改测验
4. **数据闭环**：所有学习行为和成绩数据自动汇总至飞书多维表格，可生成可视化报表

### 功能模块
- AI课堂引擎：基于OpenMAIC，支持豆包(Doubao)模型
- 飞书连接器：基于OpenClaw Gateway，处理消息转发与工具调用
- 教务统计后台：基于飞书多维表格，存储学生档案与成绩

### 访问与文档
- 外网公开访问地址：[https://tool.sysmex.com.cn/hr](https://tool.sysmex.com.cn/hr)
- 技术规格：`./spec/spec.md`
- 任务实施进度：`./spec/tasks.md`
- 验证核对表：`./spec/checklist.md`
- 环境搭建部署指南：[DEPLOYMENT.md](raw/Openmaic/DEPLOYMENT.md)
- 飞书多维表格配置指南：[BITABLE_GUIDE.md](raw/Openmaic/BITABLE_GUIDE.md)

---

## 引用原始证据
> 来源路径：`raw/Openmaic/README.md`
> ```raw
# OpenMAIC-Feishu-Lab: AI 互动课堂与飞书多维表格融合平台

## 1. 项目简介
OpenMAIC-Feishu-Lab 是一个专为中国大陆企业环境设计的 AI 教育解决方案。它将清华大学开源的 **OpenMAIC**（多智能体互动课堂）与 **飞书多维表格 (Bitable)** 深度整合，旨在零成本替代 Google Classroom，实现“教、学、测、管、统”全链路自动化。

## 2. 核心价值
- **国产化适配**: 彻底解决 Google Classroom 访问限制，完全运行在飞书/企微生态内。
- **自动化教务**: 利用 Bitable 低代码能力，自动处理报名、邀请、成绩同步。
- **沉浸式学习**: AI 老师实时讲授、互动 H5 模拟实验、自动批改测验。
- **数据闭环**: 所有的学习行为和成绩数据自动汇总至 Bitable，生成可视化报表。

## 3. 功能模块
- **AI 课堂引擎**: 基于 OpenMAIC，支持豆包 (Doubao) 模型。
- **飞书连接器**: 基于 OpenClaw Gateway，处理消息转发与工具调用。
- **教务统计后台**: 基于飞书多维表格，存储学生档案与成绩。

## 4. 快速开始
外网访问地址: [https://tool.sysmex.com.cn/hr](https://tool.sysmex.com.cn/hr)

### 4.1 项目规范 (Project Specs)
参考 [spec.md](./spec/spec.md) 查看详细技术规格。
参考 [tasks.md](./spec/tasks.md) 查看任务实施进度。
参考 [checklist.md](./spec/checklist.md) 查看验证核对表。

### 4.2 部署指南
参考 [DEPLOYMENT.md](raw/Openmaic/DEPLOYMENT.md) 进行环境搭建。
参考 [BITABLE_GUIDE.md](raw/Openmaic/BITABLE_GUIDE.md) 配置飞书多维表格。
> ```

## 冲突标注
当前无已知与其他来源的矛盾冲突。
