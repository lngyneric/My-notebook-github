---
source: raw/05_代码与项目/skills/skills/skills/skill-creator/SKILL.md
raw_sha256: b2e3d83f60425c2d0b9d4162efb8f9aa322b45843497340f2289f42be422801c
compiled_at: 2026-04-14T05:09:38.448Z
---
> [!INFO] 来源路径
> `raw/05_代码与项目/skills/skills/skills/skill-creator/SKILL.md`

# Skill Creator

---

## TL;DR
Skill Creator 是指导创建有效扩展技能的规范，用于帮助 Claude 新增/更新扩展专业知识、工作流或工具集成的技能。技能采用渐进式披露原则管理上下文窗口，通过元数据、SKILL.md 正文、按需加载捆绑资源三级结构控制Token消耗，遵循简洁、匹配自由度、渐进披露等核心设计原则，分六步完成技能的创建与迭代。

---

## 目录
- [基本信息](#基本信息)
- [核心概念](#核心概念)
- [核心设计原则](#核心设计原则)
- [技能结构规范](#技能结构规范)
- [渐进式披露设计原则](#渐进式披露设计原则)
- [技能创建流程](#技能创建流程)

---

## 基本信息

| 元数据 | 内容 |
|--------|------|
| 名称 | `skill-creator` |
| 用途 | 用户需要创建新技能或更新现有技能，扩展 Claude 能力时使用 |
| 许可证 | 完整条款见 `LICENSE.txt` |

---

## 核心概念

> [!QUOTE] 原始定义
> Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks—they transform Claude from a general-purpose agent into a specialized agent equipped with procedural knowledge that no model can fully possess.

技能可为 Claude 提供四类能力：
1. **专业化工作流**：特定领域的多步骤流程
2. **工具集成**：特定文件格式或API的操作说明
3. **领域专业知识**：企业特定知识、数据Schema、业务逻辑
4. **捆绑资源**：复杂重复任务所需的脚本、参考资料、资源文件

---

## 核心设计原则

### 1. 简洁优先
上下文窗口是公共资源，需要和系统提示、对话历史、其他技能元数据、用户请求共享。
> 核心假设：Claude 本身已经足够智能，**只添加 Claude 没有的上下文**，每一段信息都需要验证其Token成本是否合理，优先用简洁示例替代冗长说明。

### 2. 匹配合理的自由度
根据任务的稳定性和可变性匹配指令的灵活度：
| 自由度等级 | 形式 | 适用场景 |
|------------|------|----------|
| 高 | 文本式指令 | 多种方法都有效、决策依赖上下文、启发式方法引导 |
| 中 | 伪代码或带参数的脚本 | 存在偏好模式、允许一定变体、配置影响行为 |
| 低 | 固定脚本、少参数 | 操作易出错、一致性要求高、必须遵循特定顺序 |

> 类比：狭窄的悬崖桥梁需要低自由度护栏，开阔场地允许高自由度多路线。

---

## 技能结构规范

### 标准目录结构
```
skill-name/
├── SKILL.md (必需)
│   ├── YAML 前置元数据 (必需)
│   │   ├── name: (必需)
│   │   └── description: (必需)
│   └── Markdown 指令文档 (必需)
└── 可选捆绑资源
    ├── scripts/          - 可执行代码（Python/Bash等）
    ├── references/       - 按需加载的参考文档
    └── assets/           - 输出用文件（模板、图标、字体等）
```

### SKILL.md 要求
SKILL.md 是每个技能必需的入口文件，分为两部分：
1. **YAML前置元数据**：仅包含`name`和`description`两个字段，这是 Claude 判断是否触发该技能的唯一依据，必须清晰完整描述技能功能和触发场景。
2. **Markdown正文**：技能使用说明和指引，仅在技能触发后加载。

### 可选捆绑资源规范

#### 1. `scripts/` 脚本目录
存放需要确定性可靠性或需要重复生成的可执行代码：
- 适用场景：相同代码被重复编写、需要确定性结果
- 优势：节省Token、结果确定，无需加载到上下文即可执行
- 注意：仍可能需要 Claude 读取，进行补丁或环境适配修改

#### 2. `references/` 参考目录
存放按需加载到上下文的参考文档：
- 适用场景：技能工作过程中需要参考的文档，例如：数据库Schema、API文档、领域知识、企业政策、详细工作流指南
- 优势：保持 SKILL.md 简洁，仅在需要时加载
- 最佳实践：
  - 大于1万词的文件，需要在 SKILL.md 中提供grep搜索模式
  - 避免重复：信息只存在于 SKILL.md 或参考文件中，详细信息优先放在参考文件，仅在 SKILL.md 保留核心流程指引

#### 3. `assets/` 资源目录
存放不需要加载到上下文、用于 Claude 最终输出的文件：
- 适用场景：输出需要的模板、图片、图标、脚手架代码、字体、示例文档等
- 优势：将输出资源和文档分离，无需加载到上下文即可使用

### 禁止包含的内容
技能仅包含支持功能的必要文件，禁止创建额外文档或辅助文件，包括但不限于：
- `README.md`
- `INSTALLATION_GUIDE.md`
- `QUICK_REFERENCE.md`
- `CHANGELOG.md`

技能不包含创建过程、安装测试、面向用户文档等辅助上下文，额外文件只会增加混乱。

---

## 渐进式披露设计原则

为高效管理上下文，技能采用三级加载机制：
1. **元数据（name + description）**：始终保留在上下文中，约100词
2. **SKILL.md 正文**：技能触发后加载，要求小于5000词
3. **捆绑资源**：Claude 按需加载，脚本可无需读入上下文，无大小限制

### 规范要求
- SKILL.md 正文仅保留核心内容，控制在500行以内，接近限制时拆分内容到单独文件，拆分后必须在 SKILL.md 中说明文件用途和加载时机
- 核心原则：当技能支持多个变体、框架或选项时，仅在 SKILL.md 保留核心工作流和选择指引，变体特定细节移入单独参考文件

### 常用设计模式

#### 模式1：高层指南+拆分参考
```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber:
[code example]

## Advanced features

- **Form filling**: See [FORMS.md](FORMS.md) for complete guide
- **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
```
Claude 仅在需要时加载对应参考文件。

#### 模式2：按领域/变体组织
对于多领域、多框架支持的技能，按维度拆分参考文件：
```
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```
仅加载和当前需求相关的文件，节省上下文。

#### 模式3：条件化细节
基础内容放在SKILL.md，高级内容链接到单独文件：
```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```
仅在需要对应功能时加载相关文件。

### 重要指引
- 避免深度嵌套引用：参考文件仅从SKILL.md一级跳转，不嵌套
- 长参考文件需要加目录：超过100行的参考文件，顶部需要加目录方便预览

---

## 技能创建流程

按顺序执行以下步骤，仅在明确不适用时跳过：
1. 通过具体示例理解技能需求
2. 规划可复用的技能内容（脚本、参考、资源）
3. 初始化技能（运行`init_skill.py`）
4. 编辑实现技能内容和SKILL.md
5. 打包技能（运行`package_skill.py`）
6. 根据实际使用迭代

### 步骤1：通过具体示例理解需求
即使是更新现有技能，该步骤也有价值，仅在需求完全明确时跳过。
需要明确：
- 技能需要支持哪些功能
