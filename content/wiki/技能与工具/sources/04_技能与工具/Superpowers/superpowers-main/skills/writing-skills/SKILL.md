---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/SKILL.md
raw_sha256: 6ffe287552c1ca9c050e1226408282535611365264fa05a6da81ddc70729a37e
compiled_at: 2026-04-15T00:35:23.798Z
---
# Writing Skills (Superpowers Skill Creation)
## 摘要
Writing Skills 是将测试驱动开发（TDD）应用到流程文档/技能编写的方法，定义了一套标准化的技能创建、编辑和验证流程，要求遵循TDD的RED-GREEN-REFACTOR循环，先做失败测试再编写技能文档，保证创建的技能可复用、可靠、能被AI正确发现和使用。

## 关键要点
### 核心定义与原则
- Writing skills 是**测试驱动开发（TDD）应用于流程文档编写**的方法
- 核心铁律：`NO SKILL WITHOUT A FAILING TEST FIRST`，创建、编辑技能都必须先看到没有技能时AI会失败，才能确认技能解决了正确问题，无例外
- 前置要求：必须先掌握`superpowers:test-driven-development`定义的RED-GREEN-REFACTOR循环

### 什么是Skill
Skill 是给AI agent使用的、经过验证的技术、模式或工具参考指南；是可复用的内容，不是单次问题解决的叙事记录。
| 属于Skill | 不属于Skill |
|-----------|-------------|
| 可复用技术、模式、工具、参考指南 | 单次问题解决叙事 |
| 通用解决方法 | 项目特定约定 |

### 技能类型
1. **Technique（技术）**：带执行步骤的具体方法
2. **Pattern（模式）**：思考问题的思维方式
3. **Reference（参考）**：API文档、语法指南等工具文档

### TDD到技能创建的映射
| TDD概念 | 技能创建对应环节 |
|---------|------------------|
| 测试用例 | 带子agent的压力场景 |
| 生产代码 | 技能文档SKILL.md |
| 测试失败（RED） | 没有技能时agent违反规则（基线行为） |
| 测试通过（GREEN） | 有技能时agent符合要求 |
| 重构 | 关闭漏洞同时保持合规 |
| 先写测试 | 编写技能前先运行基线场景 |

### 什么时候创建/不创建技能
**创建场景**：技术不直观、需要跨项目重复引用、模式适用范围广、对他人有价值
**不创建场景**：一次性解决方案、已有标准文档、项目特定约定、可通过正则/自动化校验的机械约束

### 目录与文档结构要求
- 目录结构：采用扁平命名空间，每个技能一个独立目录，必须包含`SKILL.md`作为主文档，仅在必要时添加支撑文件
- SKILL.md前端matter：仅支持`name`和`description`两个字段，`name`仅允许字母、数字、连字符；`description`必须以`Use when`开头，仅描述触发条件，不能总结技能流程/内容，避免AI直接使用描述跳过完整文档
- 标准文档结构：包含概述、使用时机、核心模式、快速参考、实现、常见错误等部分

### Claude搜索优化（CSO）
为了让未来的Claude能正确发现技能，需要满足：
1. 描述仅包含触发条件，使用具体问题、场景，不写流程
2. 覆盖Claude会搜索的关键词：错误信息、问题症状、同义词、工具名称
3. 描述性命名：主动语态、动词开头，用动名词描述过程，按实际操作/核心洞见命名
4. 令牌效率：严格控制字数，将细节移到工具帮助、使用交叉引用、压缩示例、消除冗余

### 测试不同类型技能
| 技能类型 | 测试方法 | 成功标准 |
|----------|----------|----------|
| 规则类纪律技能 | 知识提问、压力场景、组合压力 | 最大压力下agent依然遵守规则 |
| 技术类技能 | 应用场景、变体场景、信息缺失测试 | agent能正确应用技术到新场景 |
| 模式类思维模型 | 识别场景、应用场景、反例测试 | 正确识别什么时候/如何应用模式 |
| 参考类文档 | 检索场景、应用场景、缺口测试 | agent能找到并正确应用参考信息 |

### 技能创建完整流程（RED-GREEN-REFACTOR）
1. **RED（基线）**：不带技能运行子agent压力场景，记录agent的选择、合理化借口和违规场景
2. **GREEN（编写）**：仅针对发现的问题编写最小化技能，带技能重新运行场景验证合规
3. **REFACTOR（补漏洞）**：发现新的合理化借口就添加明确应对，反复测试直到无漏洞

## 证据片段
> 测试发现，如果描述总结了技能工作流，Claude可能遵循描述而不阅读完整技能内容：描述写`code review between tasks`会导致Claude只做1次评审，而技能流程图明确要求2次评审；修改为仅描述触发条件`Use when executing implementation plans with independent tasks`后，Claude正确阅读了流程图并执行了两阶段评审。

> 铁律原文：`NO SKILL WITHOUT A FAILING TEST FIRST`，适用于新技能和现有技能的修改，写技能前测试？删掉重来，编辑技能不测试？同样违规，没有例外。

> 常见合理化借口回应：`Clear to you ≠ clear to other agents. Test it.`，`Untested skills have issues. Always. 15 min testing saves hours.`
