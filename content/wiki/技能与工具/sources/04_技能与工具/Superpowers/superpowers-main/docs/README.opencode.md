---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/README.opencode.md
raw_sha256: 62c1f6619d632d07a3c29c21758a15c3ecc97210a5baa65d41cba2d4a930c536
compiled_at: 2026-04-14T16:50:20.900Z
---
# Superpowers for OpenCode
Superpowers for OpenCode是一个适用于OpenCode.ai的插件，为OpenCode提供可加载的自定义技能扩展能力。本文档是该插件的完整使用与安装指南。

## 摘要
Superpowers是OpenCode的技能扩展插件，支持全局安装、项目本地安装两种方式，提供技能查找、加载能力，支持用户创建个人自定义技能与项目专属技能，具备上下文压缩抗性、自动上下文注入等特性，兼容适配Claude Code编写的技能。

## 安装方式
### 快速安装
向OpenCode发送如下指令即可完成安装：
```
Clone https://github.com/obra/superpowers to ~/.config/opencode/superpowers, then create directory ~/.config/opencode/plugin, then symlink ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js to ~/.config/opencode/plugin/superpowers.js, then restart opencode.
```

### 手动安装
#### 前置依赖
- 已安装[OpenCode.ai](https://opencode.ai)
- 已安装Node.js
- 已安装Git

#### 安装步骤
1. 拉取Superpowers代码到指定目录
```bash
mkdir -p ~/.config/opencode/superpowers
git clone https://github.com/obra/superpowers.git ~/.config/opencode/superpowers
```

2. 注册插件
OpenCode从`~/.config/opencode/plugin/`发现插件，创建符号链接完成注册：
```bash
mkdir -p ~/.config/opencode/plugin
ln -sf ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js ~/.config/opencode/plugin/superpowers.js
```
也支持项目本地安装（在OpenCode项目根目录执行）：
```bash
mkdir -p .opencode/plugin
ln -sf ~/.config/opencode/superpowers/.opencode/plugin/superpowers.js .opencode/plugin/superpowers.js
```

3. 重启OpenCode，插件会自动激活。

## 使用方法
### 查找技能
使用`find_skills`工具列出所有可用技能：
```
use find_skills tool
```

### 加载技能
使用`use_skill`工具加载指定技能：
```
use use_skill tool with skill_name: "superpowers:brainstorming"
```
加载的技能会自动插入对话，在上下文压缩后仍会保留。

### 创建个人技能
用户可在`~/.config/opencode/skills/`目录创建自定义个人技能：
1. 创建技能目录：`mkdir -p ~/.config/opencode/skills/my-skill`
2. 创建`SKILL.md`文件，包含前置元数据与技能内容即可。

### 创建项目技能
可在OpenCode项目内创建项目专属技能：
1. 在项目根目录创建技能目录：`mkdir -p .opencode/skills/my-project-skill`
2. 创建符合格式要求的`SKILL.md`文件即可。

## 技能优先级
技能按以下优先级解析，高优先级技能会覆盖低优先级的同名技能：
1. 项目技能（`.opencode/skills/`）- 最高优先级
2. 个人技能（`~/.config/opencode/skills/`）
3. Superpowers内置技能（`~/.config/opencode/superpowers/skills/`）

也可通过命名前缀强制指定解析层级：
- `project:skill-name`：强制使用项目技能
- `skill-name`：按项目→个人→Superpowers内置的顺序搜索
- `superpowers:skill-name`：强制使用Superpowers内置技能

## 核心特性
1. **自动上下文注入**：插件通过`chat.message`钩子在每个会话自动注入Superpowers上下文，无需手动配置。
2. **消息插入模式**：加载的技能会以`noReply: true`的用户消息插入，保证长对话上下文压缩后技能仍保留。
3. **压缩抗性**：插件监听`session.compacted`事件，会在上下文压缩后自动重新注入核心引导内容，维持插件功能。
4. **工具映射**：自动适配为Claude Code编写的技能，将Claude Code工具映射为OpenCode原生工具。

## 架构
### 插件结构
插件主体位置：`~/.config/opencode/superpowers/.opencode/plugin/superpowers.js`
包含组件：
- 两个自定义工具：`use_skill`、`find_skills`
- 用于初始上下文注入的`chat.message`钩子
- 用于上下文压缩后重新注入的`session.compacted`事件处理器
- 依赖共享核心模块`lib/skills-core.js`

### 共享核心模块
位置：`~/.config/opencode/superpowers/lib/skills-core.js`
提供技能处理核心能力，包括解析元数据、搜索技能、解析技能路径、检查更新等功能，该模块在OpenCode和Codex实现间共享，用于代码复用。

## 更新
执行以下命令更新插件：
```bash
cd ~/.config/opencode/superpowers
git pull
```
更新后重启OpenCode加载新版本即可。

## 故障排查
### 插件无法加载
1. 检查插件文件是否存在
2. 检查符号链接是否正确
3. 开启DEBUG日志查看OpenCode运行日志，确认插件加载状态
4. 查找插件加载日志`service=plugin path=file:///.../superpowers.js loading plugin`确认加载流程

### 找不到技能
1. 确认Superpowers内置技能目录存在内容
2. 使用`find_skills`工具查看已发现的技能列表
3. 检查技能结构，每个技能必须包含`SKILL.md`文件

### 工具无法工作
1. 通过日志确认插件已成功加载
2. 检查Node.js版本，插件要求Node.js支持ES模块
3. 可通过Node.js手动测试插件模块是否可正常加载

### 上下文无法注入
1. 检查`chat.message`钩子是否正常工作
2. 确认内置的`using-superpowers`技能存在
3. 检查OpenCode版本，要求为支持插件的新版本

## 测试
插件在`tests/opencode/`目录提供自动化测试套件，可执行脚本验证插件功能，测试范围包含插件加载、核心库功能、工具执行、技能优先级解析、环境隔离等。
