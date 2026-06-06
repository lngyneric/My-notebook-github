---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/31-Appendix-D.md
raw_sha256: 64ecca4028e8a2e10ea36f0b365fd927e9bcdd5fa64d0ace576763ad948a1d67
compiled_at: 2026-04-14T04:04:48.124Z
---
# 附录 D：基于 AgentSpace 构建智能体
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/31-Appendix-D.md`

---

## TL;DR
AgentSpace（现已更名为 Gemini Enterprise，本文保留原名）是Google推出的面向企业的AI智能体开发平台，核心提供全企业数字资产统一搜索、企业知识图谱构建、无代码自定义智能体开发，支持多智能体通过A2A开放协议协作，可快速搭建能自主推理、执行多步骤任务的场景化AI智能体，开发者可通过平台UI零编程完成智能体开发与部署。

---

## 重要说明
> [!NOTE]
> AgentSpace 现已更名为 Gemini Enterprise。考虑到与原文保持一致的原则，本译文仍继续采用 AgentSpace 名称。

---

## 要点
1. **平台定位与核心能力**
   - 面向企业打造的智能体开发平台，目标是通过嵌入AI提升生产力、优化决策，实现「智能体驱动型企业」
   - 核心提供跨文档、邮件、数据库全企业数字资产的统一搜索，依托Google Gemini等大模型理解整合多源信息
   - 构建企业知识图谱，映射人员、文档、数据关系，提供上下文感知的个性化结果
   - 原生支持基于Agent2Agent（A2A）开放协议的多智能体通信协作，可支撑复杂编排工作流
   - 内置基于角色的访问控制、数据加密，安全能力为基础组件
2. **无代码开发能力**
   - 提供无代码界面Agent Designer，无需深度技术经验即可创建自定义智能体
   - 支持从Google预制提示库选择提示，也可自定义提示词定义智能体行为
   - 支持对接日历、Gmail、Jira、Outlook、ServiceNow等数十种Google及第三方服务
   - 高级功能包括：自定义数据存储集成、Google/私有知识图谱对接、Web端发布、使用监控分析等
3. **访问路径**：可从Google Cloud Console入口进入AgentSpace，开发完成后直接提供可交互的聊天界面供最终使用

---

## 步骤指引（基于AgentSpace UI构建智能体）
1. 从Google Cloud Console中选择AI Applications访问AgentSpace
2. 为智能体配置需要集成的第三方/Google服务
3. 选择Google提供的预制提示，或自定义提示词定义智能体参数
4. 按需配置数据存储、知识图谱、发布、监控等高级功能
5. 开发完成后即可通过内置聊天界面和智能体交互

---

## 引用证据（原图文对照）

### 图1：如何使用 Google Cloud Console 访问 AgentSpace
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597818-455d7428-484f-4bf5-858f-7495fd418bbd.png)

### 图2：与包括 Google 和第三方平台在内的各种服务集成
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597872-5c91627d-6ad6-4f13-a72e-82888c0b0eee.png)

### 图 3：Google 预置提示库
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598084-0db2871e-1251-44d1-8bcd-ab4c9b13d6f1.png)

### 图 4：自定义智能体提示
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598048-09bf9f3c-c8bd-4ff9-9514-fc76840344c5.png)

### 图 5：AgentSpace 高级功能
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598223-8f7249bf-931c-42c2-8f33-a916c0a4bdcb.png)

### 图 6：用于与您的智能体发起聊天的 AgentSpace 用户界面
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598253-264347cb-f46d-468c-abcc-a87eb21ef909.png)

---

## 结语
AgentSpace 提供用于在组织现有的数字基础架构内开发和部署AI智能体的功能框架。该系统的架构将复杂的后端流程（例如自主推理和企业知识图谱映射）链接到用于构建智能体的图形用户界面。通过该界面，用户可以通过集成各种数据服务并通过提示定义其操作参数来配置智能体，从而构建定制的、情境感知的自动化系统。

这种方法抽象了底层的技术复杂性，无需深厚的编程专业知识即可构建专用的多智能体系统。其主要目标是将自动化分析和操作功能直接嵌入到工作流中，从而提高流程效率并增强数据驱动的分析能力。在实践教学方面，我们提供动手学习模块，例如 Google Cloud Skills Boost 上的“Build a Gen AI Agent with Agentspace”实验，它为技能学习提供结构化的环境。

---

## 参考文献
1. Create a no-code agent with Agent Designer: [https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer](https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer)
2. Google Cloud Skills Boost: [https://www.cloudskillsboost.google/](https://www.cloudskillsboost.google/)

---

## 导航
[[30-Appendix-C|< 上一章]] | [[000-Home|首页]] | [[32-Appendix-E|下一章 >]]
