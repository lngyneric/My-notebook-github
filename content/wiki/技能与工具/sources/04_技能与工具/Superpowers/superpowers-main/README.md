---
source: raw/04_技能与工具/Superpowers/superpowers-main/README.md
raw_sha256: 0f2b0a3dcf43fc34961f615d5379e105a382bb24ba9ebcd90a25a7a8d6edbb80
compiled_at: 2026-04-14T16:49:03.786Z
---
# Superpowers
## 摘要
Superpowers 是一套面向编码智能体的完整软件开发工作流，基于可组合的技能集合构建，能够引导编码智能体按规范流程完成开发任务，支持 Claude Code、Codex、OpenCode 等多个平台，可实现数小时的自主开发。

## 核心工作原理
1. 编码智能体启动后不会直接编写代码，而是先通过对话梳理出需求规格，分块展示供开发者确认
2. 开发者确认设计后，智能体生成清晰可执行的实现计划，强调红/绿测试驱动开发(TDD)、YAGNI、DRY原则
3. 开发者确认后启动子代理驱动开发流程，多个智能体逐个处理工程任务并自检工作，可脱离人工干预自主运行数小时

## 安装方式
安装流程根据平台不同有所区别：
### Claude Code（插件市场）
1. 执行 `plugin marketplace add obra/superpowers-marketplace` 添加插件市场
2. 执行 `/plugin install superpowers@supermarkets-marketplace` 安装插件
3. 执行 `/help` 验证安装，可查看三个可用命令：`/superpowers:brainstorm`、`/superpowers:write-plan`、`/superpowers:execute-plan`
### Codex
让 Codex 获取并遵循 `https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md` 的指引安装，详细文档见 [docs/README.codex.md](docs/README.codex.md)
### OpenCode
让 OpenCode 获取并遵循 `https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md` 的指引安装，详细文档见 [docs/README.opencode.md](docs/README.opencode.md)

## 标准工作流
Superpowers 的工作流为强制性流程，智能体会在任意任务前检查对应技能，流程如下：
1. **头脑风暴（brainstorming）**：编写代码前激活，通过提问梳理粗略想法、探索替代方案，分块展示设计供验证，保存设计文档
2. **使用Git工作树（using-git-worktrees）**：设计通过后激活，在新分支创建隔离工作区，完成项目配置，验证干净的测试基线
3. **编写计划（writing-plans）**：基于通过验证的设计激活，将工作拆分为2-5分钟即可完成的小块任务，每个任务包含明确文件路径、完整代码要求和验证步骤
4. **子代理驱动开发/执行计划（subagent-driven-development/executing-plans）**：基于计划激活，每个任务分配一个新的子代理，完成两步评审（先检查规格一致性，再检查代码质量），或分批次执行并设置人工检查点
5. **测试驱动开发（test-driven-development）**：实现过程中激活，强制执行RED-GREEN-REFACTOR流程：先编写失败测试、确认测试失败、编写最简代码让测试通过、提交代码，会删除在测试之前编写的代码
6. **请求代码评审（requesting-code-review）**：任务间隙激活，对照计划评审工作，按严重程度报告问题，严重问题会阻塞后续进度
7. **完成开发分支（finishing-a-development-branch）**：所有任务完成后激活，验证测试，提供合并/发起PR/保留/丢弃选项，清理工作树

## 内置技能库
| 分类 | 技能 | 说明 |
| ---- | ---- | ---- |
| 测试 | test-driven-development | 遵循RED-GREEN-REFACTOR开发循环，包含测试反模式参考 |
| 调试 | systematic-debugging | 4阶段根因定位流程，包含根因追踪、深度防御、基于条件等待等技术 |
| 调试 | verification-before-completion | 确保问题真正被修复 |
| 协作 | brainstorming | 苏格拉底式设计细化 |
| 协作 | writing-plans | 生成详细实现计划 |
| 协作 | executing-plans | 带检查点的批量执行 |
| 协作 | dispatching-parallel-agents | 并发子代理工作流 |
| 协作 | requesting-code-review | 预评审检查清单 |
| 协作 | receiving-code-review | 处理评审反馈 |
| 协作 | using-git-worktrees | 并行开发分支管理 |
| 协作 | finishing-a-development-branch | 合并/PR决策流程 |
| 协作 | subagent-driven-development | 带两阶段评审（规格一致性、代码质量）的快速迭代 |
| 元技能 | writing-skills | 遵循最佳实践创建新技能，包含测试方法 |
| 元技能 | using-superpowers | 技能系统介绍 |

## 核心理念
- 测试驱动开发：永远先写测试
- 系统化优于临时处理：流程优先于猜测
- 降低复杂度：以简洁为首要目标
- 证据优先于主张：声明成功前先验证

## 贡献指南
1. Fork 仓库
2. 为你要添加的技能创建新分支
3. 遵循 `writing-skills` 技能的要求创建和测试新技能
4. 提交Pull Request
完整指南参见 `skills/writing-skills/SKILL.md`

## 其他信息
- **更新**：更新插件时技能会自动更新，Claude Code更新命令为 `/plugin update superpowers`
- **赞助**：创作者欢迎用户通过GitHub赞助支持开源开发
- **开源协议**：MIT License
- **支持渠道**：Issue反馈：https://github.com/obra/superpowers/issues；插件市场：https://github.com/obra/superpowers-marketplace
