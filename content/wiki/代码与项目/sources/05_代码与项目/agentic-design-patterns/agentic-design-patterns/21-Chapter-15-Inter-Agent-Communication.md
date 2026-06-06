---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/21-Chapter-15-Inter-Agent-Communication.md
raw_sha256: 0d88906a17bc7768d2b074181b367baf1bcf66936a8833576883db16a7619a58
compiled_at: 2026-04-14T04:02:32.386Z
---
# 智能体间通信 (Inter-Agent Communication, A2A)
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/21-Chapter-15-Inter-Agent-Communication.md`

[[上一章：知识检索 RAG|20-Chapter-14-Knowledge-Retrieval-RAG]] | [[首页|000-Home]] | [[下一章：资源感知优化|22-Chapter-16-Resource-Aware-Optimization]]

---

## TL;DR
单个AI智能体处理复杂多面问题存在局限性，Google推出的开放标准**A2A (Agent2Agent) 协议**解决了不同框架构建的AI智能体无法高效协作的痛点，它提供标准化的通信规范，支持智能体自动发现、异步任务管理、多种交互模式，内置安全机制，实现跨框架的无缝协调、任务委派与信息交换，是构建模块化、可扩展分布式多智能体系统的核心基础。

---

## 目录
- [模式概述](#智能体间通信模式概述)
- [核心概念](#a2a-的核心概念)
- [通信与任务模型](#通信与任务)
- [交互机制](#交互机制)
- [安全机制](#安全性)
- [A2A 与 MCP 的关系](#a2a-vs-mcp)
- [应用场景](#实际应用与使用场景)
- [代码示例](#动手代码示例)
- [设计指南](#概览)
- [关键要点](#关键要点)
- [结论](#结论)
- [参考文献](#参考文献)

---

## 智能体间通信模式概述
Agent2Agent (A2A) 协议是**实现不同AI智能体框架之间通信与协作的开放开源标准**，核心价值是保证互操作性：允许LangGraph、CrewAI、Google ADK等不同技术开发的AI智能体不受来源/框架差异影响，协同工作。

A2A已经获得大量主流科技企业支持：
- 现有支持：Atlassian、Box、LangChain、MongoDB、Salesforce、SAP、ServiceNow、Auth0
- 计划集成：Microsoft 将把A2A集成到Azure AI Foundry和Copilot Studio

作为开源协议，A2A开放接受社区贡献，推动协议演进与广泛落地。

> 原始引用：*The Agent2Agent (A2A) protocol is an open standard designed to enable communication and collaboration between different AI agent frameworks. It ensures interoperability, allowing AI agents developed with technologies like LangGraph, CrewAI, or Google ADK to work together regardless of their origin or framework differences.*

---

## A2A 的核心概念
A2A 协议为智能体交互提供结构化设计，核心基础组件包括：核心参与者、智能体卡片、智能体发现、通信与任务、交互机制、安全性。

### 核心参与者
A2A 定义了三类核心交互实体：
1. **用户 (User)**：发起智能体协助请求
2. **A2A 客户端 (客户端智能体, A2A Client)**：代表用户请求操作或信息的应用程序或AI智能体
3. **A2A 服务器 (远程智能体, A2A Server)**：提供HTTP端点处理客户端请求并返回结果的AI智能体/系统；对客户端是"不透明"系统，客户端无需了解其内部实现细节

### 智能体卡片 (Agent Card)
智能体卡片是智能体的数字身份，通常为JSON格式，包含客户端交互与自动发现所需的全部关键信息：
- 基础信息：智能体身份、端点URL、版本
- 能力声明：支持的功能（流式传输、推送通知等）、技能列表、默认输入输出模式
- 安全要求：身份验证要求

下面是一个天气智能体的Agent Card示例：
```json
{
  "name": "WeatherBot",
  "description": "Provides accurate weather forecasts and historical data.",
  "url": "http://weather-service.example.com/a2a",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false,
    "stateTransitionHistory": true
  },
  "authentication": {
    "schemes": [
      "apiKey"
    ]
  },
  "defaultInputModes": [
    "text"
  ],
  "defaultOutputModes": [
    "text"
  ],
  "skills": [
    {
      "id": "get_current_weather",
      "name": "Get Current Weather",
      "description": "Retrieve real-time weather for any location.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "What's the weather in Paris?",
        "Current conditions in Tokyo"
      ],
      "tags": [
        "weather",
        "current",
        "real-time"
      ]
    },
    {
      "id": "get_forecast",
      "name": "Get Forecast",
      "description": "Get 5-day weather predictions.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "5-day forecast for New York",
        "Will it rain in London this weekend?"
      ],
      "tags": [
        "weather",
        "forecast",
        "prediction"
      ]
    }
  ]
}
```

### 智能体发现 (Agent Discovery)
智能体发现是客户端查找可用A2A服务器Agent Card、获取其能力描述的过程，常用三种策略：
1. **Well-Known URI**：智能体在标准化路径（例如 `/.well-known/agent.json`）托管Agent Card，适合公共/特定领域场景，支持广泛的自动化访问
2. **托管注册中心 (Curated Registries)**：集中式目录，统一发布Agent Card，支持按条件查询，适合需要集中管理与访问控制的企业环境
3. **直接配置 (Direct Configuration)**：Agent Card信息被嵌入或私下共享，适合动态发现不重要的紧密耦合/私有系统

无论使用哪种方式，都需要保护Agent Card端点，可通过访问控制、双向TLS (mTLS)、网络限制实现安全防护，尤其是卡片包含敏感（非机密）信息时。

---

## 通信与任务
在A2A框架中，通信围绕**异步任务**构建，任务是长时间运行流程的基本工作单元：
- 每个任务分配唯一ID，会经历`已提交`/`处理中`/`完成`等一系列状态，支持复杂操作的并行处理
- 智能体之间的通信通过**消息 (Message)** 承载

消息结构说明：
- 属性 (`attributes`)：描述消息的键值元数据，例如优先级、创建时间
- 一个或多个部分 (`part`)：承载实际交付内容，例如纯文本、文件、结构化JSON数据

任务执行过程中智能体生成的具体输出称为**工件 (artifacts)**，和消息类似，工件也由多个部分组成，支持增量流式输出。

A2A通信的基础规范：
- 所有通信基于HTTP(S)传输，负载使用JSON-RPC 2.0协议
- 为了维护多轮交互的上下文连续性，使用服务器生成的`contextId`对相关任务分组，保留上下文信息

---

## 交互机制
A2A提供多种交互模式适配不同AI应用需求：
| 交互模式 | 适用场景 | 机制说明 |
|---------|---------|---------|
| 同步请求/响应 | 快速即时操作 | 客户端发送请求后主动等待，服务器在单次同步交换中返回完整响应 |
| 异步轮询 | 长耗时处理任务 | 客户端发送请求后，服务器立即返回"处理中"状态与任务ID；客户端可执行其他任务，定期轮询查询任务状态，直到任务完成/失败 |
| 流式更新 (SSE 服务器发送事件) | 实时增量结果获取 | 建立服务器到客户端的持久单向连接，远程智能体持续推送状态更新/部分结果，无需客户端多次请求 |
| 推送通知 (Webhook) | 超长运行/资源密集型任务 | 客户端注册Webhook URL，当任务状态发生重大变化（例如完成）时，服务器异步推送通知到客户端URL，不需要维持长连接或频繁轮询，效率更高 |

能力声明规则：智能体是否支持流式传输、推送通知都需要在Agent Card中明确声明。

A2A是**模态无关 (modality-agnostic)** 的协议，不仅支持文本，还支持音频、视频等其他数据类型，可用于构建丰富的多模态AI应用。

### 请求示例
同步请求（使用`sendTask`方法，等待单次完整响应）：
```
