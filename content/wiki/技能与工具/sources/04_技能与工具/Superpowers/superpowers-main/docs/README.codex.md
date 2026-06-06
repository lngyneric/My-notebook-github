---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/README.codex.md
raw_sha256: 59681464372d0714d4b03e0eec112337b0e8514ccc6a6d84bfe8929d98fdae1c
compiled_at: 2026-04-14T16:50:05.572Z
---
# Superpowers for Codex
Superpowers for Codex 是一套用于配合 OpenAI Codex 使用的技能扩展工具集，提供自定义技能管理、技能加载执行的完整工作流，支持用户创建个人自定义技能。

## 摘要
本文档是 OpenAI Codex 使用 Superpowers 工具集的完整指南，包含快速安装、手动安装流程、使用方法、架构说明、更新方式、问题排查与帮助渠道，同时说明 Codex 支持目前处于实验阶段。

## 关键要点
- 提供两种安装方式：一句话触发的快速安装，以及手动克隆仓库的分步安装
- 支持技能查找、单个技能加载、全技能引导启动、自定义个人技能四种核心使用场景
- 个人自定义技能会覆盖同名称的官方内置技能
- 适配 Claude Code 编写的技能，做了工具映射以适配 Codex 环境
- 更新仅需拉取最新的 Git 仓库代码即可

## 安装说明
### 快速安装
直接让 Codex 执行以下指令即可自动完成安装：
```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

### 手动安装
#### 前置要求
- 拥有 OpenAI Codex 访问权限
- 拥有安装文件所需的 Shell 访问权限

#### 安装步骤
1. 克隆仓库：
```bash
mkdir -p ~/.codex/superpowers
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
```
2. 引导程序已包含在仓库的 `.codex/superpowers-bootstrap.md`，Codex 会自动从克隆位置调用
3. 安装验证：让 Codex 执行 `Run ~/.codex/superpowers/.codex/superpowers-codex find-skills`，如果输出带描述的可用技能列表则安装成功

## 使用方式
### 查找所有可用技能
```
Run ~/.codex/superpowers/.codex/superpowers-codex find-skills
```

### 加载指定技能
```
Run ~/.codex/superpowers/.codex/superpowers-codex use-sill superpowers:brainstorming
```

### 引导加载所有技能
```
Run ~/.codex/superpowers/.codex/superpowers-codex bootstrap
```
该操作会加载包含所有技能信息的完整引导。

### 创建个人自定义技能
1. 在 `~/.codex/skills/` 目录下创建个人技能目录：
```bash
mkdir -p ~/.codex/skills/my-skill
```
2. 创建 `~/.codex/skills/my-skill/SKILL.md` 文件，按格式编写技能内容：
```markdown
---
name: my-skill
description: Use when [condition] - [what it does]
---

# My Skill

[Your skill content here]
```
个人技能会覆盖同名的 Superpowers 官方技能。

## 架构
### Codex CLI 工具
- 位置：`~/.codex/superpowers/.codex/superpowers-codex`
- 是一个 Node.js 命令行脚本，提供三个核心命令：
  - `bootstrap`：加载包含所有技能的完整引导
  - `use-skill <name>`：加载指定名称的技能
  - `find-skills`：列出所有可用技能

### 共享核心模块
- 位置：`~/.codex/superpowers/lib/skills-core.js`
- 采用 ES 模块格式，用于技能发现与解析，和 OpenCode 插件共享该模块，保证跨平台行为一致。

### 工具映射
为适配 Codex，对为 Claude Code 编写的技能做了如下工具映射：
- `TodoWrite` → `update_plan`
- 带子代理的 `Task` → 告知用户子代理不可用，直接完成工作
- `Skill` 工具 → `~/.codex/superpowers/.codex/superpowers-codex use-skill`
- 文件操作 → 使用 Codex 原生工具

## 更新
```bash
cd ~/.codex/superpowers
git pull
```

## 问题排查
### 找不到技能
1. 验证安装：`ls ~/.codex/superpowers/skills`
2. 检查CLI是否正常工作：`~/.codex/superpowers/.codex/superpowers-codex find-skills`
3. 验证技能目录包含`SKILL.md`文件

### CLI脚本无执行权限
```bash
chmod +x ~/.codex/superpowers/.codex/superpowers-codex
```

### Node.js 错误
CLI脚本需要 Node.js 环境，执行 `node --version` 验证版本，要求v14或更高，推荐v18+以支持ES模块。

## 帮助与说明
- 问题反馈：https://github.com/obra/superpowers/issues
- 主文档：https://github.com/obra/superpowers
- 介绍博客：https://blog.fsck.com/2025/10/27/skills-for-openai-codex/
- 注意：Codex 支持目前为实验性功能，可能需要根据用户反馈迭代优化。
