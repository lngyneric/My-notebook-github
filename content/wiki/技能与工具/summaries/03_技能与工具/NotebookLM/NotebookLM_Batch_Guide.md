---
source: raw/03_技能与工具/NotebookLM/NotebookLM_Batch_Guide.md
raw_sha256: 75288d23776093053b0d9ffd78a7e7976c6b30cce00401c45cd8993f02bd9213
compiled_at: 2026-04-24T05:42:12.555Z
---
# NotebookLM 批量操作指南
## 摘要
本指南用于说明NotebookLM知识库的信息收集方法，以及基于脚本的批量笔记本创建、管理与定向提问的完整操作流程，适用于需要一次性创建多学科/多项目独立NotebookLM空间的场景。

## 1. 信息收集
### 1.1 账号信息
NotebookLM账号认证状态存储于本地指定路径，相关信息如下：
- 认证状态：已认证 (Authenticated)
- 上次认证时间：2026-01-13 14:21:59
- 存储位置：`.claude/skills/notebooklm/data/auth_info.json`

### 1.2 笔记本信息查询
提供两种笔记本信息查询方式：
#### A. 本地已记录笔记本查询
执行以下命令查看本地存储的笔记本记录：
```bash
python .claude/skills/notebooklm/scripts/run.py notebook_manager.py list
```
*当前本地记录*：`Physics` (ID: `physics`)

#### B. 在线远程笔记本扫描
执行以下命令扫描账号下的在线笔记本：
```bash
python .claude/skills/notebooklm/scripts/run.py list_remote_notebooks.py
```
*最近扫描结果*：0 个在线笔记本。

## 2. 批量创建操作流程
### 2.1 准备工作
1. 已完成账号认证（执行`auth_manager.py setup`）
2. 提前整理好待创建的笔记本标题列表

### 2.2 批量创建方法
#### 方法一：命令行直接创建
通过`--titles`参数直接传入多个笔记本标题（空格分隔）：
```bash
# 示例：创建3个新笔记本
python .claude/skills/notebooklm/scripts/run.py batch_creator.py --titles "Project Alpha" "Team Meeting Notes" "Research 2024"
```

#### 方法二：文本文件批量导入
1. 创建纯文本文件（如`notebooks_to_create.txt`），每行填写一个笔记本标题，示例内容：
```text
HR Training Resources
Product Roadmap
Competitor Analysis
Q1 Financials
```
2. 执行命令导入文件批量创建：
```bash
python .claude/skills/notebooklm/scripts/run.py batch_creator.py --file notebooks_to_create.txt
```

### 2.3 批量创建脚本执行逻辑
1. 自动启动浏览器（默认无头模式，可通过`--headless`参数控制模式）
2. 自动登录NotebookLM管理面板
3. 自动点击「New Notebook」创建新笔记本
4. 自动将新建笔记本重命名为指定标题
5. 抓取新生成的笔记本URL并保存至本地库`library.json`
6. 循环执行上述步骤直至所有标题对应的笔记本创建完成

## 3. 后续操作：定向提问
笔记本创建完成后，可通过`ask_question.py`脚本向指定笔记本发起提问，支持两种指定笔记本的方式：
```bash
# 方式1：通过笔记本名称提问
python .claude/skills/notebooklm/scripts/run.py ask_question.py --question "总结核心观点" --notebook-name "HR Training Resources"

# 方式2：通过笔记本ID提问（ID可通过list命令查询）
python .claude/skills/notebooklm/scripts/run.py ask_question.py --question "总结核心观点" --notebook-id hr-training-resources
```

## 4. 注意事项
- **网络延迟适配**：脚本已在操作间隙设置自动等待机制，避免被Google识别为机器人，执行过程中无需手动干预，需等待脚本自动完成。
- **重命名失败处理**：若因网络卡顿导致自动重命名失败，笔记本将保留为「Untitled notebook」，可后续在网页端手动修改，本地库记录可通过`notebook_manager.py`脚本修正。
