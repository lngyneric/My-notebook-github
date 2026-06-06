---
source: raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/evaluation.md
raw_sha256: 8c99479f8a2d22a636c38e274537aac3610879e26f34e0709825077c4576f427
compiled_at: 2026-04-14T05:18:22.077Z
---
# MCP Builder 评估指南

> [!info] 来源路径
> `raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/evaluation.md`

---

## TL;DR
本指南定义了 MCP Server 评估的完整规范：要求创建10个满足「只读、独立、非破坏性、结果稳定」要求的问题，每个问题需要多步工具调用才能得到唯一可验证答案，最终输出为标准XML格式，可使用官方提供的评估脚本自动运行测试，得出MCP Server服务LLM工具调用能力的准确率。

---

## 目录
- [评估创建规范](#评估创建规范)
  - [核心要求](#核心要求)
  - [问题设计指南](#问题设计指南)
  - [答案设计指南](#答案设计指南)
  - [评估创建流程](#评估创建流程)
  - [输出格式](#输出格式)
  - [示例：好问题与坏问题](#示例好问题与坏问题)
  - [验证流程](#验证流程)
- [运行评估](#运行评估)
  - [环境准备](#环境准备)
  - [支持的传输方式与运行命令](#支持的传输方式与运行命令)
  - [命令行参数说明](#命令行参数说明)
  - [评估输出](#评估输出)
  - [完整工作流示例](#完整工作流示例)
  - [故障排查](#故障排查)

---

## 评估创建规范

### 核心要求
| 要求项 | 说明 |
|--------|------|
| 问题数量 | 需要创建10个人类可读的问题 |
| 问题属性 | 必须是只读、独立、非破坏性操作 |
| 复杂度 | 每个问题需要多次（最多数十次）工具调用才能解决 |
| 答案要求 | 必须是单个、可验证、稳定（不随时间变化）的值 |

**引用原始要求片段：**
> ```
> - Create 10 human-readable questions
> - Questions must be READ-ONLY, INDEPENDENT, NON-DESTRUCTIVE
> - Each question requires multiple tool calls (potentially dozens)
> - Answers must be single, verifiable values
> - Answers must be STABLE (won't change over time)
> ```

评估的核心目标：
> MCP服务器的质量衡量标准，不是工具实现得多么完善全面，而是这些实现（输入输出schema、文档描述、功能）能否让仅能访问MCP服务器、无其他上下文的LLM成功回答真实的复杂问题。

### 问题设计指南

#### 基础约束
1. **必须独立**：每个问题不依赖其他问题的答案，不依赖其他问题的写入操作
2. **仅需非破坏性幂等操作**：不需要修改任何状态就能得到答案
3. **必须真实、清晰、简洁、复杂**：要求LLM调用多个（最多数十个）工具/步骤才能解决

#### 复杂度要求
4. 需要深度探索，通常为多跳问题，后一步依赖前一步工具返回的信息
5. 可能需要多页翻页、查询历史数据来获取小众信息，题目必须有难度
6. 需要深度理解，而非表层知识：可设计为需要证据的判断题、需要遍历多个假设的选择题
7. 不能通过简单关键词搜索解决：不能包含目标内容的特定关键词，需要用同义词/相关概念/转述，要求多次搜索、分析多个关联条目、提取上下文后推导答案

#### 工具测试要求
8. 应该对工具返回值做压力测试：可触发工具返回大JSON或列表、考验LLM对多种格式数据（ID、时间戳、文件信息、URL等）的理解能力
9. 大部分问题应该反映真实人类使用场景，即人类在LLM辅助下会真正进行的信息检索任务
10. 可设计需要数十次工具调用的问题，以此挑战LLM的上下文限制，推动MCP工具减少不必要的信息返回
11. 可包含一定歧义性：可以存在歧义，或者要求LLM自行决策调用哪个工具，强迫LLM可能犯错，但最终仍必须存在唯一可验证答案

#### 稳定性要求
12. 答案必须不随时间变化：不能依赖动态的「当前状态」，比如帖子反应数、帖子回复数、频道成员数都是不允许的
13. 不要被MCP服务器现有能力限制出题：需要创建有挑战的复杂问题，即使部分问题现有工具无法解决也是允许的

### 答案设计指南

1. **可通过直接字符串比较验证**
   - 如果答案有多种格式，必须在问题中明确指定输出格式，例如`请使用YYYY/MM/DD格式回答`
   - 必须是单个可验证值，支持类型：用户ID/名称、频道ID/名称、消息ID/字符串、URL、标题、数值、时间戳、布尔值、邮箱、文件信息、选择题选项等
   - 不需要复杂格式/结构化输出，验证方式为直接字符串比较

2. **优先人类可读格式**
   - 优先使用名称、时间、文件名等人类可读内容，不透明ID仅可接受
   - 绝大多数答案都应为人类可读格式

3. **必须稳定**
   - 基于已结束的历史内容创建问题，保证答案永远不变
   - 可通过指定固定时间窗口来避免答案变化
   - 选择不太可能变更的上下文作为出题基础

4. **清晰无歧义**
   - 题目设计必须保证存在唯一清晰的答案，且答案可通过MCP工具推导得出

5. **多样性**
   - 答案需要覆盖不同类型、不同格式的值（用户、频道、消息等不同概念）

6. **不能是复杂结构**
   - 不能是值列表、复杂对象、自然文本，除非可以非常方便地通过直接字符串比较验证，且LLM可以稳定复现结果

### 评估创建流程

| 步骤 | 操作说明 |
|------|----------|
| 1 文档检查 | 阅读目标API文档，理解可用端点和功能，歧义点从网络补充信息，可最大化并行 |
| 2 工具检查 | 列出MCP服务器所有可用工具，理解输入输出schema和文档描述，此阶段不调用工具 |
| 3 建立理解 | 重复步骤1-2直到完全理解，不允许阅读MCP服务器实现代码，基于理解设计有挑战的真实任务 |
| 4 只读内容检查 | 理解后仅使用只读非破坏性工具调用检查内容，定位出题需要的特定内容；必须增量小范围调用工具，每次调用用limit参数限制结果数不超过10，使用分页避免上下文溢出 |
| 5 生成任务 | 基于内容检查结果，生成10个符合所有规范的问题 |

### 输出格式
评估必须使用XML格式，示例如下：

```xml
<evaluation>
   <qa_pair>
      <question>你的问题在这里</question>
      <answer>单个可验证答案</answer>
   </qa_pair>
</evaluation>
```

完整示例：
```xml
<evaluation>
   <qa_pair>
      <question>Find the project created in Q2 2024 with the highest number of completed tasks. What is the project name?</question>
      <answer>Website Redesign</answer>
   </qa_pair>
   <qa_pair>
      <question>Search for issues labeled as "bug" that were closed in March 2024. Which user closed the most issues? Provide their username.</question>
      <answer>sarah_dev</answer>
   </qa_pair>
   <qa_pair>
      <question>Look for pull requests that modified files in the /api directory and were merged between January 1 and January 31, 2024. How many different contributors worked on these PRs?</question>
      <answer>7</answer>
   </qa_pair>
</evaluation>
```

### 示例：好问题与坏问题

#### 好问题示例

**示例1：需要深度探索的多跳问题（GitHub MCP）**
```xml
<qa_pair>
   <question>Find the repository that was archived in Q3 2023 and had previously been the most forked project in the organization. What was the primary programming language used in that repository?</question>
   <answer>Python</answer>
</qa_pair>
```
优点：需要多次搜索、需要识别归档前的分叉数、需要查询仓库语言信息，答案简单可验证，基于不会变化的历史数据。

**示例2：不需要关键词匹配，需要理解上下文（项目管理MCP）**
```xml
<qa_pair>
   <question>Locate the initiative focused on improving customer onboarding that was completed in late 2023. The project lead created a retrospective document after completion. What was the lead's role title at that time?</question>
   <answer>Product Manager</answer>
</qa_pair>
```
优点：不直接使用具体项目名，需要按
