# NotebookLM 批量操作指南

本文档介绍了如何收集 NotebookLM 知识库信息，以及如何使用脚本进行批量创建和管理操作。

## 1. 信息收集

### 1.1 账号信息
您的账号认证状态存储在本地。
- **状态**: 已认证 (Authenticated)
- **上次认证时间**: 2026-01-13 14:21:59
- **存储位置**: `.claude/skills/notebooklm/data/auth_info.json`

### 1.2 笔记本信息 (Notebooks)
我们提供了两种方式查看笔记本信息：

**A. 查看本地已记录的笔记本**
```bash
python .claude/skills/notebooklm/scripts/run.py notebook_manager.py list
```
*目前本地记录*: `Physics` (ID: `physics`)

**B. 扫描在线笔记本 (Remote)**
```bash
python .claude/skills/notebooklm/scripts/run.py list_remote_notebooks.py
```
*最近扫描结果*: 0 个在线笔记本。

---

## 2. 批量创建操作流程

如果您需要一次性创建多个笔记本（例如为不同学科或项目创建独立空间），可以使用我们开发的批量创建工具。

### 准备工作
1. 确保已完成认证 (`auth_manager.py setup`)。
2. 准备好要创建的笔记本标题列表。

### 方法一：命令行直接创建
使用 `--titles` 参数直接指定名称（用空格分隔）。

```bash
# 示例：创建三个新笔记本
python .claude/skills/notebooklm/scripts/run.py batch_creator.py --titles "Project Alpha" "Team Meeting Notes" "Research 2024"
```

### 方法二：通过文件批量导入
创建一个文本文件（例如 `notebooks_to_create.txt`），每行一个标题。

**notebooks_to_create.txt**:
```text
HR Training Resources
Product Roadmap
Competitor Analysis
Q1 Financials
```

运行命令：
```bash
python .claude/skills/notebooklm/scripts/run.py batch_creator.py --file notebooks_to_create.txt
```

### 脚本执行逻辑
1. 自动打开浏览器（默认无头模式，可添加 `--headless` 参数控制）。
2. 登录 NotebookLM 面板。
3. 点击 "New Notebook"。
4. 自动重命名为指定标题。
5. 获取新生成的 URL 并保存到本地库 (`library.json`)。
6. 对列表中的下一个标题重复此过程。

---

## 3. 后续操作：向笔记本提问

创建完成后，您可以使用 `ask_question.py` 向特定笔记本提问。

```bash
# 使用笔记本名称提问
python .claude/skills/notebooklm/scripts/run.py ask_question.py --question "总结核心观点" --notebook-name "HR Training Resources"

# 或者使用 ID (在 list 命令中查看)
python .claude/skills/notebooklm/scripts/run.py ask_question.py --question "总结核心观点" --notebook-id hr-training-resources
```

## 注意事项
- **网络延迟**: 脚本在操作间隙设置了自动等待，以防止被 Google 识别为机器人，请耐心等待脚本执行完毕。
- **重命名失败**: 如果网络卡顿导致重命名失败，笔记本可能会保留为 "Untitled notebook"，您可以稍后在网页端手动修改，本地库可以通过 `notebook_manager.py` 进行修正。
