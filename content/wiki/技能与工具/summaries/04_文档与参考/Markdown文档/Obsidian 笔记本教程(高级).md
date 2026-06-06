---
source: raw/04_文档与参考/Markdown文档/Obsidian 笔记本教程(高级).md
raw_sha256: 8f822bc8411c920bbf68c83477ac96da895e736545e6ec7872072cea2ee0862f
compiled_at: 2026-04-24T06:07:33.022Z
---
# Obsidian 笔记本高级教程

> [!SUMMARY] 教程简介
> 本教程涵盖Obsidian云同步、图片存储优化、手机端使用、AI辅助玩法、导出与知识图谱等高级使用技巧，全套方案工具免费，偏向极客与程序员风格，旨在解决用户的数据安全、多端同步与AI辅助创作需求。

## 核心优势（为什么选择Obsidian）
本教程总结了Obsidian的三大不可替代优势：
1.  **数据安全**：笔记以独立Markdown文件存储在本地，不依赖软件服务商，即使软件停止运营也可通过其他编辑器打开，不会丢失数据。
2.  **运行流畅**：UI响应速度极快，无白屏、卡顿问题，可保护工作心流。
3.  **AI工具适配性强**：Claude Code、Gemini CLI等AI编程工具天然支持处理本地Markdown文件，可实现查找笔记、整理文件夹、仿写文风等拓展功能。

---

## 一、云同步方案：GitHub
Obsidian本身无内置免费云同步功能，本教程推荐使用GitHub作为同步方案，具备免费、稳定、安全、支持版本回滚的特点。

### 1. 创建GitHub私有仓库
1.  登录GitHub，创建新的Repository（存储库），可自定义命名（例如`shrimp_vault`）
2.  **关键设置**：Visibility（可见性）必须选择「Private（私有）」，避免笔记内容泄露。

### 2. 克隆仓库到本地
1.  推荐新手使用GitHub Desktop操作，也可使用Git命令行
2.  在GitHub Desktop中点击`File -> Clone repository`
3.  选择刚创建的私有仓库，克隆到本地指定目录
4.  打开Obsidian，选择「打开本地仓库」，指向刚克隆的文件夹作为笔记库（Vault）

### 3. 配置.gitignore忽略文件
作用：排除工作区状态文件，避免多端同步时产生冲突
1.  在仓库根目录创建`.gitignore`文件
2.  添加以下忽略规则：
    ```text
    .obsidian/workspace.json
    .obsidian/workspace-mobile.json
    ```
3.  在GitHub Desktop中提交（Commit）并发布（Publish）配置

### 4. 配置自动化同步插件
使用「Obsidian Git」社区插件实现自动同步，避免手动提交的繁琐操作
1.  关闭Obsidian安全模式，在社区插件市场搜索并安装`Obsidian Git`插件
2.  **推荐配置**：
    *   开启`Auto commit and sync after stopping file edits`（停止编辑后自动提交同步）
    *   自动同步时间间隔建议设置为**1分钟**
    *   开启`Pull on startup`（启动时自动拉取最新改动）

---

## 二、AI玩法：Gemini CLI 实战
Obsidian本身无内置AI功能，可通过AI编程工具（以Gemini CLI为例）赋能，实现自动化创作与整理。

### 1. 环境准备
1.  安装Node.js运行环境
2.  安装Gemini CLI：执行命令`npm install -g @google/gemini-cli`（具体命令以官方文档为准）
3.  初始化授权：运行`gemini`命令，选择`login with google`完成谷歌账号授权

### 2. 实战应用场景
*   **选题生成**：让AI读取历史笔记/脚本，分析内容风格与受众偏好，生成新选题并直接输出为Markdown文件
*   **批量整理**：让AI根据选题大纲自动创建子文件夹结构，将对应大纲文件归档分类
*   **脚本仿写**：让AI搜索网络热点内容，模仿用户过往笔记的文风编写内容/视频脚本

> [!TIP] 数据安全提示
> 由于使用Git管理笔记版本，若AI修改文件出错，可随时通过`Discard changes`操作回滚到修改前的状态。

---

## 三、Markdown基础语法复习
Obsidian基于标准Markdown语法，核心常用语法如下：
*   **标题**：`# 一级标题`、`## 二级标题`，以此类推
*   **加粗**：使用`**`包裹，例：`**加粗内容**`
*   **删除线**：使用`~~`包裹，例：`~~删除内容~~`
*   **高亮**：使用`==`包裹，例：`==高亮内容==`
*   **代码块**：使用```` ```语言名称 ```` 包裹，支持语法高亮
*   **引用**：使用`> 引用内容`格式
*   **无序列表**：使用`- 列表项`格式
*   **有序列表**：使用`1. 列表项`格式
*   **其他元素**：右键编辑区可插入表格、分割线、LaTeX数学公式等元素

---

## 四、图片存储优化
### 1. 痛点说明
Obsidian默认图片存储方式存在两大问题：
*   图片默认混放在笔记目录中，容易导致文件结构混乱
*   默认链接格式非标准Markdown语法，在GitHub、VS Code等平台无法正常预览

### 2. 解决方案：Custom Attachment Location插件
通过社区插件`Custom Attachment Location`统一管理附件存储，生成标准链接
#### 插件配置步骤
1.  安装`Custom Attachment Location`社区插件
2.  插件核心设置：
    *   `Location for new attachments`：选择`In subfolder under current folder`，或指定统一的`assets`目录存储附件
    *   `Markdown URL format`：设置为`![${name}](${path})`，确保生成标准Markdown链接
    *   开启`Auto-rename attachments`（自动重命名附件）
3.  Obsidian全局设置调整：
    *   进入「文件与链接」设置，将「内部链接类型」设置为**基于当前笔记的相对路径**
    *   关闭「使用Wiki链接」选项

### 3. 优化效果
*   图片/附件自动存入指定文件夹，目录结构清晰
*   移动笔记时，关联附件自动跟随移动
*   生成标准Markdown链接，GitHub、VS Code等平台均可正常预览
*   图片大小调整语法：`![图片描述|300](图片路径.png)`，在管道符后添加数字即可调整显示宽度

---

## 五、手机端同步配置
实现Obsidian电脑端与手机端的Git同步，步骤如下：
1.  **物理传输仓库**：通过数据线将电脑上的笔记仓库文件夹复制到手机，推荐存放于手机`Documents`目录
2.  **打开笔记库**：打开Obsidian手机版，选择`Open folder as vault`，选择刚传输的仓库文件夹
3.  **配置Git同步**：
    *   安装/启用Obsidian Git插件
    *   填写GitHub用户名与邮箱
    *   **核心配置**：填写GitHub Personal Access Token（个人访问令牌，在GitHub网页端`Settings -> Developer settings -> Personal access tokens`生成，需勾选`repo`权限）
4.  **注意事项**：避免多端同时编辑同一文件，减少同步冲突概率

---

## 六、导出与知识图谱
### 1. 多格式导出（Word/HTML等）
通过插件实现Obsidian笔记多格式导出：
1.  安装`Enhancing Export`社区插件
2.  下载并安装通用文档转换工具`Pandoc`
3.  在插件设置中填入Pandoc的本地安装路径
4.  右键目标笔记，即可选择导出为Word、HTML等多种格式

### 2. 双向链接与知识图谱
*   **双向链接创建**：使用`[[笔记标题]]`语法创建笔记间的双向关联，支持反向链接查询
*   **知识图谱**：点击「查看关系图谱」功能，可可视化展示所有笔记间的关联关系，帮助发现内容间的隐性联系，激发创作灵感

---

## 相关资源
![[Obsidian_Notes.base]]
