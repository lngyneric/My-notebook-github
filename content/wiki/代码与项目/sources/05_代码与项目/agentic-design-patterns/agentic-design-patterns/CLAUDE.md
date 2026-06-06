---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/CLAUDE.md
raw_sha256: 9e51573aa0e91696fd4f699ae007c19691784f1648030f3522d47f862ea9ebd5
compiled_at: 2026-04-14T04:06:00.265Z
---
# Agentic Design Patterns 中英双语翻译项目 CLAUDE 配置说明

> [!TIP] TL;DR
> 本仓库是 Antonio Gulli 所著《Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems》的中英双语翻译项目，仅做文档翻译不涉及代码开发；所有中文内容必须使用`<mark>`标签高亮，分短篇分块、段落交替两种双语排版，遵循统一术语和格式规范，目前仅完成前言前的前置内容，正文章节仍待翻译。

---

## 基本信息

| 项目属性 | 说明 |
|---------|------|
| 项目类型 | 纯文档翻译项目 |
| 原书页数 | 424页，含21章+附录 |
| 核心内容 | 覆盖21种核心智能体设计模式 |
| 当前状态 | 仅完成献词、致谢、前言，部分内容进行中，正文未开始翻译 |

---

## 核心规则整理

### 文件结构规范
原项目约定的文件命名结构如下：
```
00-Table-of-Contents.md     # 主目录
01-Dedication.md            # 献词
02-Acknowledgment.md        # 致谢
03-Foreword.md             # Google副总裁所作前言
04-Thought-Leader.md       # 行业观点（进行中）
05-Introduction.md         # 介绍（未翻译）
06-What-Makes-Agent.md     # 智能体定义（未翻译）
07-Chapter-01.md           # 第1章：提示链（未翻译）
...                        # 后续章节遵循相同命名规则
rules.md                   # 翻译规则与指南
README.md                  # 项目双语说明文档
```

### 翻译格式强制要求
1. **中文高亮要求**：所有中文翻译必须包裹在 HTML `<mark>` 标签中，方便在 GitHub 上区分中英内容
2. **排版格式**：
   - 短篇内容（献词、致谢、前言）：分「英文板块」和「中文板块」，用水平分隔线隔开
   - 长篇内容（正文章节）：英文段落和中文翻译段落交替排列
3. **术语约定**：首次出现的重要术语保留英文，中文译名放括号中，完整术语表见 `rules.md`
4. **间距与标点**：中文与英文、数字之间加空格，中文语境用中文标点，英文语境用英文标点

### 翻译质量要求
1. 准确性：100%忠实原文含义
2. 流畅性：符合中文表达习惯
3. 专业性：保持技术文档严谨性
4. 一致性：全文档术语统一
5. 格式合规：100%符合约定的Markdown语法

---

## 原书涵盖的21种核心智能体设计模式
按原书分为四个部分：
### 第一部分：核心模式
1. Prompt Chaining（提示链）
2. Routing（路由）
3. Parallelization（并行）
4. Reflection（反思）
5. Tool Use（工具调用）
6. Planning（规划）
7. Multi-Agent（多智能体）

### 第二部分：进阶模式
8. Memory Management（记忆管理）
9. Learning and Adaptation（学习与适配）
10. Model Context Protocol (MCP)（模型上下文协议）
11. Goal Setting and Monitoring（目标设定与监控）

### 第三部分：集成模式
12. Exception Handling and Recovery（异常处理与恢复）
13. Human-in-the-Loop（人在回路中）
14. Knowledge Retrieval (RAG)（知识检索/检索增强生成）

### 第四部分：生产模式
15. Inter-Agent Communication (A2A)（智能体间通信）
16. Resource-Aware Optimization（资源感知优化）
17. Reasoning Techniques（推理技术）
18. Guardrails/Safety Patterns（护栏/安全模式）
19. Evaluation and Monitoring（评估与监控）
20. Prioritization（优先级排序）
21. Exploration and Discovery（探索与发现）

---

## 工作流约定
### 新增翻译步骤
1. 遵循文件命名规范创建文件
2. 根据内容类型选择对应排版格式
3. 所有中文内容添加`<mark>`标签
4. 保留原文结构与所有外部链接
5. 遵循术语表保证翻译一致性
6. 完成后更新`README.md`中的进度清单

### 翻译检查项
- 所有中文内容都已添加`<mark>`标签
- 术语使用符合术语表规范
- 中文与英文、数字的间距正确
- 主要章节间已添加水平分隔线
- 所有原始链接都已保留
- Markdown语法可正确渲染

### Git提交信息约定
使用英文提交，遵循以下格式：
```
Add: [章节名] translation
Update: [章节名] formatting
Fix: [具体问题] in [章节名]
```

---

## 其他说明
- 本项目是纯文档项目，无需构建、测试、运行任何代码
- 格式专为GitHub渲染优化，中文黄色高亮是强制要求
- 原书版税全部捐赠给救助儿童会
- 翻译内容采用CC BY 4.0协议发布

---

## 引用证据片段（原始内容完整保留）
> 原始来源：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **bilingual Chinese-English translation project** of "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems" by Antonio Gulli. The project provides a comprehensive technical guide covering 21 core agentic design patterns for building intelligent AI systems.

**Key Characteristics:**
- Pure documentation/translation project (no code to build, test, or run)
- All content is in Markdown format
- Uses HTML `<mark>` tags for Chinese text highlighting
- Follows strict bilingual format with English and Chinese side-by-side
- Original book has 424 pages across 21 chapters plus appendices

## File Structure

```
00-Table-of-Contents.md     # Main table of contents
01-Dedication.md            # Dedication section
02-Acknowledgment.md        # Acknowledgment section
03-Foreword.md             # Foreword by Google VP
04-Thought-Leader.md       # Thought leader perspective (in progress)
05-Introduction.md         # Introduction (not yet translated)
06-What-Makes-Agent.md     # What makes an AI system an agent (not yet translated)
07-Chapter-01.md           # Chapter 1: Prompt Chaining (not yet translated)
...                        # Subsequent chapters follow same naming pattern
rules.md                   # Translation rules and guidelines
README.md                  # Project README with bilingual content
```

## Translation Format and Rules

### Mandatory Highlighting System

**All Chinese translations MUST use HTML `<mark>` tags:**
```markdown
English text here.

<mark>中文翻译在这里。</mark>
```

This creates yellow highlighting for Chinese content on GitHub, making it easy to distinguish between languages.

### Two Layout Formats

**1. Short Content (Dedication, Acknowledgment, Foreword):**
```markdown
## English | 英文
[Complete English content]

---

## Chinese | 中文
[Complete Chinese translation]
```

**2. Long Content (Chapters):**
```markdown
[English paragraph 1]

<mark>[中文翻译段落 1]</mark>

[English paragraph 2]

<mark>[中文翻译段落 2]</mark>
```

### Technical Term Conventions

Keep important terms in English with Chinese in parentheses on first use:
- Agent → 智能体 (Agent)
- Prompt Chaining → 提示链 (Prompt Chaining)
- RAG → 检索增强生成 (RAG)
- Human-in-the-Loop → 人在回路中 (Human-in-the-Loop)

Reference the technical term dictionary in rules.md:1-179 for consistent translations.

### Spacing Rules

- Add space between Chinese and English: `AI 系统`
- Add space between Chinese and numbers: `21 个章节`
- Use Chinese punctuation in Chinese context
- Use English punctuation in English context

### Format Requirements

- Use horizontal rules (`---`) to separate major sections
- Add horizontal rules between level-2 headings for readability
- Preserve all original code example links (Google Colab/Drive)
- Maintain exact Markdown formatting from original
- Use proper Chinese quotation marks: 「」 or ""

## Translation Quality Standards

1. **Accuracy**: 100% faithful to original meaning
2. **Fluency**: Natural Chinese expression that follows local conventions
3. **
