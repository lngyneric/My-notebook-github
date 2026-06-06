---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/plans/2025-11-22-opencode-support-implementation.md
raw_sha256: 3cf211c2a9ff7fd0b8bd60f995199a383da45978e068194a22c8a4cf10c4e224
compiled_at: 2026-04-14T16:51:36.034Z
---
# OpenCode Support Implementation Plan (Superpowers)

## 摘要
本文档是Superpowers项目为OpenCode.ai添加完整原生支持的实施计划，目标是通过抽离共享核心技能逻辑、重构现有Codex实现、开发原生OpenCode JavaScript插件，实现Superpowers技能系统对OpenCode.ai的完整支持，同时消除代码冗余，保证核心逻辑的一致性。

## 目标
为Superpowers添加OpenCode.ai完整支持，开发与现有Codex实现共享核心逻辑的原生JavaScript插件。

## 整体架构
1. 将通用的技能发现、解析逻辑抽离到共享模块`lib/skills-core.js`
2. 重构现有Codex实现，使用抽离后的共享核心
3. 基于OpenCode原生插件API开发OpenCode插件，包含自定义工具和会话钩子

## 技术栈
Node.js、JavaScript、OpenCode Plugin API、Git worktrees

## 实施阶段与关键任务

### Phase 1: 创建共享核心模块
| 任务 | 内容 | 产出 |
|------|------|------|
| 任务1：提取前置元信息(Frontmatter)解析 | 从`.codex/superpowers-codex`抽离YAML前置元信息解析逻辑，创建`lib/skills-core.js`并实现`extractFrontmatter`函数 | `lib/skills-core.js` |
| 任务2：提取技能发现逻辑 | 添加`findSkillsInDir`递归查找目录中所有`SKILL.md`技能文件 | 更新`lib/skills-core.js` |
| 任务3：提取技能路径解析逻辑 | 添加`resolveSkillPath`，支持个人技能覆盖同名Superpowers技能的阴影覆盖(shadowing)规则 | 更新`lib/skills-core.js` |
| 任务4：提取更新检查逻辑 | 添加`checkForUpdates`，检查Git仓库是否有远程更新，超时不阻塞启动 | 更新`lib/skills-core.js` |

### Phase 2: 重构Codex使用共享核心
1. 为`.codex/superpowers-codex`添加共享核心模块导入
2. 移除本地实现的`extractFrontmatter`/`findSkillsInDir`/`checkForUpdates`函数，替换为共享核心版本
3. 每步替换后验证脚本功能正常并提交变更

### Phase 3: 开发OpenCode插件
| 任务 | 内容 |
|------|------|
| 任务9：创建插件目录结构 | 创建`.opencode/plugin/superpowers.js`插件脚手架 |
| 任务10：实现`use_skill`工具 | 支持按名称加载技能，解析前置元信息，输出技能内容，支持个人技能阴影覆盖规则 |
| 任务11：实现`find_skills`工具 | 列出所有可用的Superpowers技能和个人技能 |
| 任务12：实现会话启动钩子 | 会话启动时自动注入`using-superpowers`技能说明、工具映射规则和更新通知 |

### Phase 4: 文档更新
1. 创建OpenCode安装指南`.opencode/INSTALL.md`，包含 prerequisites、安装步骤、使用说明、故障排查
2. 更新主README.md，添加OpenCode支持板块
3. 更新发布说明RELEASE-NOTES.md，添加OpenCode支持记录和Codex重构说明

### Phase 5: 最终验证
1. 验证Codex核心命令`find-skills`/`use-skill`/`bootstrap`仍然可用
2. 验证所有新创建文件都存在，目录结构符合预期
3. 确认所有变更已提交，工作区干净，生成实施完成总结

## 成功验收标准
- ✅ `lib/skills-core.js`已创建并包含所有核心函数
- ✅ `.codex/superpowers-codex`已重构为使用共享核心
- ✅ Codex所有核心命令工作正常
- ✅ 已创建`.opencode/plugin/superpowers.js`并包含所需工具和钩子
- ✅ 已创建安装指南，更新了README和RELEASE-NOTES
- ✅ 所有变更已提交，工作区干净

## 手动测试步骤（需要安装OpenCode）
1. 按照安装指南完成安装
2. 启动OpenCode会话，验证启动引导正常显示
3. 测试`find_skills`、`use_skill`功能正常
4. 验证支持文件访问、个人技能阴影覆盖、工具映射规则生效
