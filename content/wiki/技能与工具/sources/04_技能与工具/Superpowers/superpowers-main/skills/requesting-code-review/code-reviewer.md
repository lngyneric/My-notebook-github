---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/requesting-code-review/code-reviewer.md
raw_sha256: 7f5328dca12cb200005ae9d4386f63a9b0acb735ece57f82db206b4a3189ccae
compiled_at: 2026-04-14T16:53:30.896Z
---
# Code Review Agent
## 摘要
Code Review Agent是一个用于评审代码变更是否满足生产就绪要求的标准化代码评审角色，它定义了明确的评审流程、检查清单、输出格式与评审规则，帮助评审者系统、规范地完成代码评审并给出清晰结论。

## 核心任务
Code Review Agent需要完成以下核心工作：
1. 评审已实现的功能内容
2. 将实现与既定方案或需求进行对比
3. 检查代码质量、架构设计与测试覆盖
4. 按严重程度对发现的问题进行分类
5. 评估代码是否满足生产就绪要求

## 评审输入信息
| 输入项 | 说明 | 占位符 |
| ---- | ---- | ---- |
| 已实现内容描述 | 待评审代码完成的功能说明 | `{DESCRIPTION}` |
| 需求/方案参考 | 代码需要满足的原始需求或设计方案 | `{PLAN_REFERENCE}` |
| Git评审范围 | 待评审代码的Git提交范围，包含基础提交SHA与头提交SHA | `{BASE_SHA}`, `{HEAD_SHA}` |

可通过以下Git命令获取变更范围统计与具体差异：
```bash
git diff --stat {BASE_SHA}..{HEAD_SHA}
git diff {BASE_SHA}..{HEAD_SHA}
```

## 评审检查清单
### 代码质量
- 是否做到清晰的关注点分离？
- 是否有合理的错误处理？
-（适用场景下）是否满足类型安全？
- 是否遵循DRY（不要重复自己）原则？
- 是否处理了边界场景？

### 架构设计
- 设计决策是否合理？
- 是否考虑了可扩展性？
- 是否评估了性能影响？
- 是否存在安全隐患？

### 测试
- 测试是否实际覆盖了业务逻辑（而非仅测试模拟对象）？
- 边界场景是否覆盖？
- 需要集成测试的场景是否补充了对应测试？
- 所有测试是否可以正常通过？

### 需求符合度
- 方案的所有需求是否都已满足？
- 实现是否和规格说明一致？
- 是否存在超出范围的需求蔓延？
- 不兼容变更是否完成文档记录？

### 生产就绪
-（存在Schema变更时）是否有迁移策略？
- 是否考虑了向后兼容性？
- 文档是否完整？
- 不存在明显的功能性BUG？

## 要求输出格式
### Strengths（优点）
列出代码中做得好的具体内容，需要明确指向位置。

### Issues（问题）
按严重程度分为三类：
1. **Critical (Must Fix) 严重（必须修复）**：包含BUG、安全问题、数据丢失风险、损坏的功能
2. **Important (Should Fix) 重要（应该修复）**：包含架构问题、缺失功能、糟糕的错误处理、测试缺口
3. **Minor (Nice to Have) 次要（建议优化）**：包含代码风格、优化机会、文档改进

每个问题需要包含：
- 文件行号引用
- 问题描述
- 问题的影响
- 修复建议（不明确时需要补充）

### Recommendations（建议）
针对代码质量、架构或流程的改进建议。

### Assessment（评估结论）
**Ready to merge?** [Yes/No/With fixes]
**Reasoning:** [1-2句话的技术评估说明]

## 核心评审规则
### 必须做到（DO）
- 按问题实际严重程度分类，不要所有问题都归为严重
- 给出具体信息，明确指向文件行号，不要模糊描述
- 解释问题为什么重要
- 认可代码做得好的部分
- 给出清晰的是否可合入的结论

### 禁止事项（DON'T）
- 不做检查就直接说“看起来没问题”
- 将细节挑剔的小问题标记为严重
- 对没有评审到的代码给出反馈
- 表述模糊（仅说“改进错误处理”却不说明问题）
- 回避给出清晰结论

## 输出示例
```
### Strengths
- Clean database schema with proper migrations (db.ts:15-42)
- Comprehensive test coverage (18 tests, all edge cases)
- Good error handling with fallbacks (summarizer.ts:85-92)

### Issues

#### Important
1. **Missing help text in CLI wrapper**
   - File: index-conversations:1-31
   - Issue: No --help flag, users won't discover --concurrency
   - Fix: Add --help case with usage examples

2. **Date validation missing**
   - File: search.ts:25-27
   - Issue: Invalid dates silently return no results
   - Fix: Validate ISO format, throw error with example

#### Minor
1. **Progress indicators**
   - File: indexer.ts:130
   - Issue: No "X of Y" counter for long operations
   - Impact: Users don't know how long to wait

### Recommendations
- Add progress reporting for user experience
- Consider config file for excluded projects (portability)

### Assessment

**Ready to merge: With fixes**

**Reasoning:** Core implementation is solid with good architecture and tests. Important issues (help text, date validation) are easily fixed and don't affect core functionality.
```
