---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/README.md
raw_sha256: 98fd758ca85b8ffd07e65f29f5d7fb125be6d5109425b5688c1b789a5198b6fa
compiled_at: 2026-04-14T04:06:17.391Z
---
# Agentic Design Patterns 智能体设计模式 中英文对照翻译项目

> [!TIP] TL;DR
> 本项目是 Antonio Gulli 所著《Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems》的社区协作中英文对照翻译项目，采用双语对照格式，保留原书全部代码示例，遵循 CC BY-NC 4.0 开源协议，仅用于中文 AI 社区学习交流。

---

## 基础信息

### 项目元数据
| 项 | 信息 |
|-----|-----|
| 来源仓库 | [ginobefun/agentic-design-patterns-cn](https://github.com/ginobefun/agentic-design-patterns-cn) |
| 原书作者 | [Antonio Gulli](https://www.linkedin.com/in/searchguy/) |
| 原书出版 | Amazon 购买链接：[Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems](https://www.amazon.com/Agentic-Design-Patterns-Hands-Intelligent/dp/3032014018/) |
| 原文档公开链接 | [Google Docs 预览](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/preview?tab=t.0#heading=h.pxcur8v2qagu) |
| 本项目协议 | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/ginobefun-agentic-design-patterns-cn-badge.png)](https://mseep.ai/app/ginobefun-agentic-design-patterns-cn)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![GitHub stars](https://img.shields.io/github/stars/ginobefun/agentic-design-patterns-cn)](https://github.com/ginobefun/agentic-design-patterns-cn/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ginobefun/agentic-design-patterns-cn)](https://github.com/ginobefun/agentic-design-patterns-cn/network)

## 项目要点
- 完整保留原书内容，提供中英双语逐段对照，中文内容使用高亮标记便于区分
- 原书共 424 页，涵盖核心智能体设计模式、高级模式、集成模式、生产落地模式四大模块
- 社区协作翻译，每章节需完成 AI 翻译、人工评审、交叉评审三个环节才算正式交付
- 保留全部原书代码示例，支持本地运行与 Google Colab 在线运行

---

## 翻译进度（截至项目 README 最新更新）
总页数：424 页

### 前置内容
| 章节 | 状态 |
|------|------|
| [献辞](01-Dedication.md) | ✅ 全部完成 |
| [致谢](02-Acknowledgment.md) | ✅ 全部完成 |
| [序言](03-Foreword.md) | ✅ 全部完成 |
| [思想领袖的洞见](04-Thought-Leader.md) | ✅ 全部完成 |
| [介绍](05-Introduction.md) | ⏳ 交叉评审中 |
| [什么是"智能体"？](06-What-Makes-Agent.md) | ⏳ 交叉评审中 |

### 第一部分：核心设计模式（103 页）
| 章节 | 设计模式概述 | 状态 |
|------|-------------|------|
| [第 1 章：提示链](07-Chapter-01-Prompt-Chaining.md) | 分而治之的任务分解，将复杂任务拆解为处理流水线 | ✅ 全部完成 |
| [第 2 章：路由](08-Chapter-02-Routing.md) | 根据情境动态决策，选择最佳行动路径 | ✅ 全部完成 |
| [第 3 章：并行化](09-Chapter-03-Parallelization.md) | 并发执行多个独立任务，提升处理性能 | ✅ 全部完成 |
| [第 4 章：反思](10-Chapter-04-Reflection.md) | 通过自我评估与反馈循环迭代优化输出质量 | ✅ 全部完成 |
| [第 5 章：工具使用](11-Chapter-05-Tool-Use.md) | 集成外部工具与 API，扩展智能体能力边界 | ✅ 全部完成 |
| [第 6 章：规划](12-Chapter-06-Planning.md) | 制定多阶段执行计划，分解实现复杂目标 | ✅ 全部完成 |
| [第 7 章：多智能体协作](13-Chapter-07-Multi-Agent-Collaboration.md) | 多个智能体协同分工，共同完成复杂任务 | ✅ 全部完成 |

### 第二部分：高级设计模式（61 页）
| 章节 | 设计模式概述 | 状态 |
|------|-------------|------|
| [第 8 章：记忆管理](14-Chapter-08-Memory-Management.md) | 管理短期/长期记忆，维持上下文连续性 | ✅ 全部完成 |
| [第 9 章：学习与适应](15-Chapter-09-Learning-and-Adaptation.md) | 从经验中学习，持续优化智能体行为 | ✅ 全部完成 |
| [第 10 章：模型上下文协议](16-Chapter-10-Model-Context-Protocol.md) | 标准化智能体交互，规范通信方式 | ✅ 全部完成 |
| [第 11 章：目标设定与监控](17-Chapter-11-Goal-Setting-and-Monitoring.md) | 动态管理目标，实时追踪任务进展 | ⏳ 交叉评审中 |

### 第三部分：集成设计模式（34 页）
| 章节 | 设计模式概述 | 状态 |
|------|-------------|------|
| [第 12 章：异常处理与恢复](18-Chapter-12-Exception-Handling-and-Recovery.md) | 优雅处理错误，保障系统稳定性 | ⏳ 交叉评审中 |
| [第 13 章：人机协作](19-Chapter-13-Human-in-the-Loop.md) | 融合人类智慧与 AI 能力，协同决策 | ⏳ 交叉评审中 |
| [第 14 章：知识检索 (RAG)](20-Chapter-14-Knowledge-Retrieval.md) | 结合外部知识库，实现检索增强生成 | ⏳ 交叉评审中 |

### 第四部分：生产设计模式（114 页）
| 章节 | 设计模式概述 | 状态 |
|------|-------------|------|
| [第 15 章：智能体间通信 (A2A)](21-Chapter-15-Inter-Agent-Communication.md) | 实现智能体间高效交互的通信协议 | ❌ 交叉评审未开始 |
| [第 16 章：资源感知优化](22-Chapter-16-Resource-Aware-Optimization.md) | 优化资源分配，平衡性能与成本 | ⏳ 交叉评审中 |
| [第 17 章：推理技术](23-Chapter-17-Reasoning-Techniques.md) | 增强推理能力，提升决策质量 | ❌ 未开始 |
| [第 18 章：护栏/安全模式](24-Chapter-18-Guardrails-Safety-Patterns.md) | 构建安全保障机制，防止不当输出 | ❌ 未开始 |
| [第 19 章：评估与监控](25-Chapter-19-Evaluation-and-Monitoring.md) | 构建性能评估体系，量化智能体表现 | ❌ 未开始 |
| [第 20 章：优先级排序](26-Chapter-20-Prioritization.md) | 管理任务优先级，优化资源分配 | ⏳ 交叉评审中 |
| [第 21 章：探索与发现](27-Chapter-21-Exploration-and-Discovery.md) | 实现自主探索机制，发现新解决方案 | ⏳ 交叉评审中 |

### 附录（74 页）
| 章节 | 概述 | 状态 |
|------|------|------|
| [附录 A
