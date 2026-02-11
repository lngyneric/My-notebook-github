---
title: Obsidian 笔记本高级教程
tags: [Obsidian, 教程, 效率, GitHub, AI]
date: 2026-01-12
---

# Obsidian 笔记本高级教程

> [!SUMMARY] 教程简介
> 本教程涵盖了从云同步、图片存储、手机端使用到 AI 玩法等 Obsidian 高级使用技巧。方案特点：全套工具免费，偏向极客与程序员风格，旨在解决数据安全、多端同步与 AI 辅助创作需求。

## 为什么选择 Obsidian？

我有三个必须使用 Obsidian 的理由：

1.  **数据安全**：笔记本质上是本地电脑上的独立 Markdown 文件。即使软件开发者跑路，笔记也不会丢失，换个编辑器即可。
2.  **丝滑流畅**：UI 响应速度极快，没有白屏和卡顿，保护工作心流。
3.  **AI 工具绝配**：Claude Code、Gemini CLI 等 AI 编程工具天生擅长处理本地 Markdown 文件，可以实现查找笔记、整理文件夹、仿写文风等神奇用法。

---

## 一、云同步方案：GitHub

相比云笔记软件，Obsidian 最缺的是云同步。我选择 **GitHub** 作为同步方案，因为它免费、稳定且安全。

### 1. 创建 GitHub 仓库
1.  登录 GitHub，创建一个新的 Repository（存储库），例如命名为 `shrimp_vault`。
2.  **注意**：Visibility（可见性）选择 **Private**（私有），保护隐私。

### 2. 克隆到本地
1.  使用 **GitHub Desktop**（推荐新手）或命令行。
2.  在 GitHub Desktop 中点击 `File -> Clone repository`。
3.  选择刚才创建的仓库，克隆到本地电脑。
4.  在 Obsidian 中选择“打开本地仓库”，指向克隆下来的文件夹。

### 3. 配置忽略文件 (.gitignore)
为了避免冲突，需要排除工作区状态文件。
1.  在仓库根目录创建 `.gitignore` 文件。
2.  添加以下内容：
    ```text
    .obsidian/workspace.json
    .obsidian/workspace-mobile.json
    ```
3.  在 GitHub Desktop 中提交（Commit）并发布（Publish）。

### 4. 自动化同步插件
手动提交太麻烦，可以使用 **Obsidian Git** 插件实现自动同步。
1.  关闭安全模式，在社区插件市场搜索并安装 `git` 插件。
2.  **推荐设置**：
    *   `Auto commit and sync after stopping file edits`：开启。
    *   时间间隔：建议设置为 **1** 分钟。
    *   `Pull on startup`：开启（启动时自动拉取最新改动）。

---

## 二、AI 玩法：Gemini CLI 实战

Obsidian 本身没有 AI，但可以通过 AI 编程工具（如 Gemini CLI）来赋能。

### 1. 环境准备
*   安装 **Node.js**。
*   安装 **Gemini CLI**：`npm install -g @google/gemini-cli` (具体命令请参考官网)。
*   初始化：运行 `gemini` 并选择 `login with google` 进行授权。

### 2. 实战案例
*   **选题生成**：让 AI 读取历史脚本，分析风格与观众喜好，生成新选题并输出为 Markdown 文件。
*   **批量整理**：让 AI 根据选题大纲，自动创建子文件夹结构，将大纲文件归档。
*   **脚本仿写**：让 AI 搜索网络热点文章，并模仿你过去的笔记文风编写视频脚本。

> [!TIP] 数据安全
> 使用 Git 管理笔记的好处是，如果 AI 改乱了文件，可以随时 `Discard changes` 回滚到修改前的状态。

---

## 三、Markdown 基础语法复习

*   **标题**：`# 一级标题`，`## 二级标题`
*   **加粗**：`****` 包裹，如 `**加粗**`
*   **删除线**：`~~~~` 包裹，如 `~~删除~~`
*   **高亮**：`====` 包裹，如 `==高亮==`
*   **代码块**：```` ```语言名称 ```` 包裹
*   **引用**：`> 引用内容`
*   **无序列表**：`- 列表项`
*   **有序列表**：`1. 列表项`
*   **插入元素**：右键可插入表格、分割线、数学公式（LaTeX）。

---

## 四、图片存储优化

Obsidian 默认的图片存储方式容易导致目录混乱，且链接格式不通用。

### 1. 痛点解决
*   **问题**：图片默认混在笔记目录中；链接格式非标准 Markdown，GitHub 无法预览。
*   **方案**：使用 **Custom Attachment Location** 插件。

### 2. 插件配置
1.  安装 `Custom Attachment Location` 插件。
2.  **设置**：
    *   `Location for new attachments`: `In subfolder under current folder` (或者指定 assets 目录)
    *   `Markdown URL format`: `![${name}](${path})` (确保生成标准 Markdown 链接)
    *   `Auto-rename attachments`: 开启。
3.  **Obsidian 设置**：
    *   `文件与链接` -> `内部链接类型`：选择 **基于当前笔记的相对路径**。
    *   关闭 `使用 Wiki 链接`。

### 3. 效果
*   图片自动存入指定文件夹（如 `assets`）。
*   移动笔记时，附件自动跟随移动。
*   生成标准 Markdown 链接，GitHub 和 VS Code 均可正常预览。
*   **调整大小**：`![image|300](path.png)` (在管道符后加数字调整宽度)。

---

## 五、手机端同步

1.  **物理传输**：通过数据线将电脑上的仓库文件夹复制到手机（推荐 `Documents` 目录）。
2.  **打开仓库**：Obsidian 手机版选择 `Open folder as vault`。
3.  **配置 Git 同步**：
    *   安装/启用 Git 插件。
    *   填写 GitHub 用户名和邮箱。
    *   **关键点**：填写 **Personal Access Token** (在 GitHub 网页端 `Settings -> Developer settings -> Personal access tokens` 生成，勾选 repo 权限)。
4.  **注意**：避免多端同时编辑同一文件以减少冲突。

---

## 六、导出与知识图谱

### 1. 导出为 Word/HTML
*   安装 **Enhancing Export** 插件。
*   下载并配置 **Pandoc**（通用文档转换工具）。
*   在插件设置中填入 Pandoc 路径。
*   右键笔记即可导出为 Word 等格式。

### 2. 双向链接与图谱
*   **链接**：使用 `[[笔记标题]]` 创建双链。
*   **图谱**：点击“查看关系图谱”，可视化展示笔记间的关联，帮助发现隐性联系和激发灵感。

---

## 七、相关资源

![[Obsidian_Notes.base]]

