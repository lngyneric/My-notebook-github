---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/using-git-worktrees/SKILL.md
raw_sha256: 4e2aeeb740335d9160ee3a6da66ca6b2ceea8e1e03b9835b5ee357a17500f2bc
compiled_at: 2026-04-14T16:57:03.956Z
---
# Using Git Worktrees
## 摘要
Using Git Worktrees是一项用于创建隔离Git工作区的开发技能，适用于需要与当前工作区隔离的功能开发或执行实现计划前的场景。它遵循系统化目录选择、安全验证的核心原则，可让开发者在同一个仓库同时处理多个分支，无需频繁切换分支，保证工作区的可靠性隔离。

## 关键要点
### 核心原理
Git worktrees可创建共享同一仓库的隔离工作区，支持同时处理多个分支无需切换，核心原则为「系统化目录选择 + 安全验证 = 可靠隔离」。

### 目录选择优先级
1. 优先使用已存在的目录：`.worktrees`优先于`worktrees`
2. 若不存在已有的目录，检查`CLAUDE.md`中的偏好配置，按配置选择
3. 若无配置则询问用户，提供项目本地隐藏目录（`.worktrees/`）和全局位置（`~/.config/superpowers/worktrees/<project-name>/`）两种选项

### 安全验证规则
- 项目本地目录（`.worktrees`/`worktrees`）必须验证是否已被git忽略：若未忽略，则按照Jesse规则，立即添加忽略规则到`.gitignore`并提交，再创建工作树，避免意外提交工作树内容
- 全局目录无需验证，位于项目仓库之外

### 标准创建流程
1. 检测项目名称
2. 根据目录位置生成完整路径，创建带新分支的worktree并切换目录
3. 根据项目配置文件自动检测并执行依赖安装（支持Node.js、Rust、Python、Go等主流项目类型）
4. 运行基准测试验证工作区初始状态：测试失败需告知用户并询问是否继续，通过则报告就绪
5. 输出工作树位置、测试状态和待实现功能信息

## 证据片段
- 核心定义：*Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.*
- 安全验证必要性：*Prevents accidentally committing worktree contents to repository.*
- 禁止操作：不验证本地目录是否被忽略、跳过基准测试、不询问就继续失败测试、歧义情况下假设目录位置、跳过`CLAUDE.md`检查
- 集成关系：被头脑风暴阶段（第四阶段）设计批准后要求调用，可与`finishing-a-development-branch`配合完成工作完成后的清理，配合`executing-plans`/`subagent-driven-development`开展工作。

## 常见错误
| 错误类型 | 问题 | 修复方案 |
|---------|------|----------|
| 跳过忽略验证 | 工作树内容被追踪，污染git状态 | 创建本地工作树前始终用`git check-ignore`验证 |
| 假设目录位置 | 造成不一致，违反项目约定 | 遵循优先级：已有目录 > CLAUDE.md配置 > 询问用户 |
| 测试失败仍继续 | 无法区分新错误和原有问题 | 报告失败，获取明确许可后再继续 |
| 硬编码设置命令 | 对不同工具的项目不兼容 | 根据项目文件（`package.json`等）自动检测 |

## 快速参考表
| 场景 | 操作 |
|-----|------|
| `.worktrees/` 存在 | 使用，并验证是否被忽略 |
| `worktrees/` 存在 | 使用，并验证是否被忽略 |
| 两者都存在 | 使用`.worktrees/` |
| 两者都不存在 | 检查CLAUDE.md → 询问用户 |
| 目录未被忽略 | 添加到.gitignore并提交 |
| 基准测试失败 | 报告失败并询问用户 |
| 无依赖配置文件 | 跳过依赖安装 |
