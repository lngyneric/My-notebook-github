---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/anthropic-best-practices.md
raw_sha256: 3e8b909316d7ff2084f04947e85d4fd1691c9ceb02105542139fe2e3a0e26c26
compiled_at: 2026-04-15T00:34:40.986Z
---
# Anthropic Claude Skill 编写最佳实践
本指南是Anthropic为开发者提供的编写可被Claude成功发现并使用的Skill的实践规范，旨在帮助作者编写简洁、结构清晰、可被Claude高效使用的Skill。

## 核心原则
### 1. 简洁优先
Skill的内容会占用Claude的上下文窗口，仅添加Claude本身不具备的信息，对每一段内容评估其token成本是否合理：
- 启动时仅预加载所有Skill的元数据（名称、描述），只有Skill匹配当前任务时Claude才会加载SKILL.md
- 一旦加载SKILL.md，其每个token都会挤占对话历史和其他上下文的空间
- 默认假设Claude已经具备通用知识，只补充特定领域的专属信息

**好示例（约50token）：仅给出核心代码，省略Claude已知的PDF、第三方库背景介绍**
```markdown
## Extract PDF text
Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

### 2. 设置匹配任务的自由度
根据任务的容错性和可变性，匹配对应的指令灵活度：
| 自由度等级 | 适用场景 | 示例 |
| ---- | ---- | ---- |
| 高自由度（文本指令） | 多方案可行、决策依赖上下文 | 代码审查流程 |
| 中等自由度（带参数的伪代码/脚本） | 存在偏好模式、允许一定变体 | 基于模板生成报告 |
| 低自由度（固定脚本、无参数） | 操作易出错、要求一致性、必须遵循固定顺序 | 数据库迁移 |

可类比理解：危险狭窄的桥梁提供精确指令（低自由度），开阔无危险的场地提供大致方向即可（高自由度）。

### 3. 针对计划使用的所有模型测试
Skill的效果依赖底层模型，不同模型能力不同：
- Claude Haiku（快速经济）：需要Skill提供足够引导
- Claude Sonnet（平衡）：要求Skill清晰高效
- Claude Opus（强推理）：要避免过度解释
如果需要跨模型使用，要编写适配所有模型的指令。

## Skill结构规范
### YAML前置元数据要求
SKILL.md仅支持两个前置字段：
- `name`：Skill的人类可读名称，最多64字符
- `description`：Skill功能和触发场景的单行描述，最多1024字符

### 命名规范
推荐使用动名词（动词+ing）格式命名，清晰表达Skill提供的能力：
- 好示例：`Processing PDFs`、`Analyzing spreadsheets`
- 可接受替代：名词短语（`PDF Processing`）、动作句式（`Process PDFs`）
- 需避免：模糊名称、过度泛化名称、集合内不一致命名

### 描述编写规范
- 必须使用第三人称，避免不一致人称导致Skill发现失败
- 必须具体，同时包含**Skill做什么**和**何时使用该Skill**，包含关键触发词，帮助Claude从上百个Skill中正确选择

**有效示例**
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```
**无效示例（模糊）**
```yaml
description: Helps with documents
```

### 渐进式披露模式
SKILL.md作为总入口，仅保留核心信息，详细内容拆分到单独文件，Claude仅在需要时加载对应内容：
- 建议SKILL.md主体不超过500行，接近限制就拆分内容
- 参考模式：高级指南+引用拆分、按领域组织内容、条件化细节
- 所有引用必须从SKILL.md一级直达，避免深层嵌套引用，防止Claude无法读取完整内容
- 超过100行的引用文件需要添加目录，方便Claude跳转定位

## 工作流与反馈循环
- 复杂任务拆分为清晰的连续步骤，使用可勾选 Checklist 让Claude跟踪进度
- 使用验证循环模式：运行验证→修复错误→重复验证，能大幅提升输出质量，提前发现错误

## 内容规范
- 避免包含时效性信息，过时内容整理到`旧模式`章节归档，不干扰主流程
- 全Skill保持术语一致性，避免同一个概念混用多个表述，减少Claude理解成本

## 通用模式
1. **模板模式**：根据需求严格程度提供输出模板，严格要求可固定完整结构，灵活需求可提供默认结构允许调整
2. **示例模式**：对于输出质量依赖风格格式的Skill，提供输入输出对，比文字描述更清晰
3. **条件工作流模式**：在决策点引导Claude根据场景选择对应分支，复杂工作流可拆分到单独文件

## 评估与迭代
推荐评估驱动开发，在编写大量文档前先构建评估场景：
1. 无Skill时运行任务，记录具体失败和缺失上下文
2. 构建3个测试场景覆盖问题缺口
3. 建立无Skill时的性能基线
4. 编写刚好满足评估通过的最小指令
5. 运行评估对比基线，迭代优化

推荐使用Claude辅助迭代Skill：使用Claude A（辅助开发）编写整理Skill，使用Claude B（新实例加载Skill）测试实际效果，基于实际使用观察持续优化，该方法结合了Claude对Agent需求的理解和开发者的领域知识，比纯人工编写更高效。

## 需要避免的反模式
- 避免使用Windows风格反斜杠路径，全平台统一使用Unix风格正斜杠
- 避免无必要提供多个可选方案，推荐给出默认方案，仅在特殊场景下提供替代选项

## 带可执行代码的Skill高级规范
- 脚本要主动处理错误，不要把错误抛给Claude处理；所有常量要添加注释说明含义，避免魔数
- 优先提供预制工具脚本，比Claude动态生成代码更可靠、更节省token
- 需要明确说明脚本是需要执行，还是需要作为参考读取
- 对于可渲染为图片的输入，可利用Claude的视觉能力做布局分析
- 复杂高风险任务使用`计划-验证-执行`模式，先输出结构化计划，验证通过后再执行，提前拦截错误
- 明确列出依赖包，不要假设环境已经预装；使用MCP工具需要写全限定名`服务名:工具名`避免找不到工具

## 最终检查清单
发布Skill前需要验证：
1. 核心质量：描述具体包含触发场景、SKILL.md不超过500行、无时效性问题、术语一致、引用一级深度、工作流步骤清晰
2. 代码脚本：脚本主动处理错误、无魔数、依赖明确、路径正确、关键操作有验证、包含质量反馈循环
3. 测试：至少3个评估场景、覆盖目标使用模型、经过真实场景测试、吸收团队反馈
