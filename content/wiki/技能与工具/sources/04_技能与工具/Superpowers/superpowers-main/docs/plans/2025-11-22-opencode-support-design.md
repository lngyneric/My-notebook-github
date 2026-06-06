---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/plans/2025-11-22-opencode-support-design.md
raw_sha256: 4688cb2e4bafa7e6124dd811be57c8873bfb4b8cccb95ddbd7032557a9cfd10b
compiled_at: 2026-04-14T16:51:21.652Z
---
# OpenCode Support Design (Superpowers)
## 基本信息
- 日期：2025-11-22
- 作者：Bot & Jesse
- 状态：设计完成，等待实现

## 概述
为Superpowers项目添加对OpenCode.ai的完整原生支持，基于原生OpenCode插件架构开发，同时与现有Codex实现共享核心功能。

## 背景
OpenCode.ai是与Claude Code、Codex类似的编码智能体，此前两次将Superpowers移植到OpenCode的尝试（PR #93、PR #116）都采用了文件复制方案，本设计改为使用OpenCode官方的JavaScript/TypeScript插件系统构建原生插件，同时与Codex实现共享代码。

### 各平台核心差异
| 平台 | 方案特点 |
| ---- | ---- |
| Claude Code | 原生Anthropic插件系统 + 基于文件的技能 |
| Codex | 无插件系统 → 引导markdown + CLI脚本 |
| OpenCode | 支持事件钩子与自定义工具API的JavaScript/TypeScript插件 |

### OpenCode智能体系统要点
- 主智能体：Build（默认，完全权限）、Plan（受限只读权限）
- 子智能体：通用型，用于研究、搜索、多步骤任务
- 调用方式：主智能体自动调度，或手动`@mention`语法调用
- 配置：自定义智能体存放在`opencode.json`或`~/.config/opencode/agent/`

## 架构设计
### 整体高层结构
1. **共享核心模块**（`lib/skills-core.js`）：提供通用的技能发现、解析逻辑，同时供Codex和OpenCode实现使用
2. **平台特定包装层**：Codex对应CLI脚本，OpenCode对应插件模块
3. **技能目录**：核心技能存放在`~/.config/opencode/superpowers/skills/`，个人技能存放在`~/.config/opencode/skills/`，个人技能会覆盖核心技能

### 代码复用策略
从原有Codex实现中提取公共功能到共享核心模块，共享核心提供以下工具方法：
- `extractFrontmatter`：从YAML解析技能名称与描述
- `findSkillsInDir`：递归发现目录下的SKILL.md文件
- `findAllSkills`：扫描多个目录获取所有技能
- `resolveSkillPath`：处理技能覆盖逻辑（个人技能优先于核心技能）
- `checkForUpdates`：通过Git检查更新

### 技能Frontmatter格式
当前格式不包含`when_to_use`字段，示例：
```yaml
---
name: skill-name
description: Use when [condition] - [what it does]; [additional context]
---
```

## OpenCode插件实现细节
### 自定义工具
1. **`use_skill`**：加载指定技能的内容到对话中，等价于Claude的Skill工具，接收`skill_name`参数返回技能完整内容。
2. **`find_skills`**：列出所有可用技能及其元数据，不需要参数。

### 会话启动钩子
新会话触发`session.started`事件时会执行以下操作：
1. 注入`using-superpowers`技能的完整内容，建立强制工作流
2. 自动运行`find_skills`，提前展示所有可用技能及其目录
3. 注入工具映射说明，将Superpowers原有工具映射为OpenCode原生工具：
   - `TodoWrite` → `update_plan`
   - 带子智能体的`Task` → OpenCode子智能体系统（@mention调用）
   - `Skill`工具 → 自定义`use_skill`工具
   - Read/Write/Edit/Bash → OpenCode原生等价工具
4. 非阻塞执行更新检查，有更新时发送通知

### 项目文件结构
```
superpowers/
├── lib/
│   └── skills-core.js           # 新增：共享技能逻辑核心
├── .codex/
│   ├── superpowers-codex        # 更新：改用共享核心
│   ├── superpowers-bootstrap.md
│   └── INSTALL.md
├── .opencode/
│   ├── plugin/
│   │   └── superpowers.js       # 新增：OpenCode插件本体
│   └── INSTALL.md               # 新增：安装指南
└── skills/                       # 保持不变
```

## 实施计划
### 阶段1：重构共享核心
1. 创建`lib/skills-core.js`，提取原有Codex实现中的frontmatter解析、技能发现、路径解析逻辑
2. 更新Codex的CLI脚本改用共享核心，移除重复代码，保留CLI包装逻辑
3. 测试Codex实现所有功能正常

### 阶段2：构建OpenCode插件
1. 创建OpenCode插件文件，导入共享核心，实现启动钩子和两个自定义工具
2. 创建OpenCode安装说明文档
3. 测试OpenCode实现所有功能正常

### 阶段3：文档整理优化
1. 更新README添加OpenCode支持说明
2. 在主文档中添加OpenCode安装说明
3. 更新发布日志
4. 回归测试Codex和OpenCode都可正常工作

## 后续步骤
1. 创建隔离开发工作区，分支为`feature/opencode-support`
2. 适用测试驱动开发，测试共享核心功能，做两个平台的集成测试
3. 按阶段增量实施，完成一个阶段验证通过后再进入下一阶段
4. 采用手动真实环境测试，验证技能加载、目录访问、工具映射等功能
5. 创建Pull Request，干净环境测试后合并到主分支

## 设计优势
- 代码复用：技能发现、解析逻辑单源可信
- 可维护性：修复bug可同时作用于两个平台
- 可扩展性：易于未来添加对Cursor、Windsurf等其他平台的支持
- 原生集成：符合OpenCode插件系统规范
- 一致性：所有平台提供一致的技能使用体验
