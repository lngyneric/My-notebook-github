---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/06-What-Makes-Agent.md
raw_sha256: 0e5388b5b07e911b956b71073ab9ad5b3d95dac8b285ea1330b2b5f2a3dbd4f4
compiled_at: 2026-04-14T03:57:29.928Z
---
# 是什么让 AI 系统成为「智能体」

> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/06-What-Makes-Agent.md`

---

## TL;DR
AI 智能体是能够感知环境、规划并采取行动自主完成目标的系统，是大语言模型能力的演进；智能体按照能力可分为从基础推理引擎到多智能体协作四个复杂度等级，行业目前已经进入多智能体协作的发展阶段，未来有望在通用化、个性化、具身化、经济参与、自组织演化等方向实现突破。

---

## 核心要点

### 什么是 AI 智能体
简单来说，**AI 智能体**是一个能够感知环境并采取行动以实现特定目标的系统。它从标准大语言模型演进而来，被赋予了规划、使用工具以及与周围环境交互的能力，可类比为能在工作中持续学习的智能助手。

AI 智能体遵循固定的五步循环完成任务：
1. **获取任务**：接收用户指定目标
2. **分析环境**：收集所有必要信息，了解当前状况
3. **思考对策**：规划达成目标的最佳行动方案
4. **采取行动**：执行行动计划完成目标
5. **学习并改进**：从结果中学习，优化未来表现

![AI Agent Five-Step Loop](images/fig1.png)
*图 1：AI 智能体如同一位智能助手，通过经验持续学习。它通过一个简单的五步循环来完成任务。*

### AI 范式的演进
仅仅两年时间，AI 的范式就发生了巨大转变，从简单的自动化演进为复杂的自主系统，演进路径为：
`基础大语言模型` → `检索增强生成（RAG）` → `单智能体` → `多智能体协作的智能体 AI`

![AI Evolution Timeline](images/fig2.png)
*图 2：从 LLM 到 RAG，再到智能体 RAG，最终走向 AI 智能体的演进。*

### 智能体的四个复杂度等级
![Agent Complexity Levels](images/fig3.png)
*图 3：展示不同复杂度智能体的实例。*

---

#### 0 级：核心推理引擎
大语言模型本身不是智能体，但可以作为基础智能体系统的推理核心。0 级配置下，大语言模型不依赖工具、记忆或环境交互，仅基于预训练知识响应，优势是强大的内部推理能力，缺陷是不具备实时/新知识获取能力，无法回答超出训练范围的问题。

---

#### 1 级：连接外部的问题解决者
大语言模型通过连接并使用外部工具成为功能性智能体，解决问题不再局限于预训练知识，可以通过多步动作从互联网、数据库等外部来源获取和处理信息，调用专业工具获得高精度结果。跨多步与外部世界交互是 1 级智能体的核心能力。

---

#### 2 级：战略性问题解决者
能力显著扩展，涵盖战略规划、主动协助和自我提升，提示工程和上下文工程是其核心赋能技能。核心能力包括：
- 处理复杂多步骤问题，主动为每个步骤做上下文工程（战略性选择、打包、管理最相关信息，避免模型认知过载，保证任务高效准确）
- 支持主动持续运行，自动处理全流程信息抽取与工具调用
- 在专业领域支持全工作流管理
- 通过自动化反馈循环优化自身的上下文工程流程，实现自我提升

---

#### 3 级：协作型多智能体系统的兴起
AI 开发的重大范式转变：不再追求单一全能超级智能体，转向发展复杂协作的多智能体系统，模仿人类组织的分工协作模式，由不同专业领域的智能体分工完成复杂目标，核心优势来自劳动分工和协同产生的合力。

当前挑战：多智能体系统的效果受限于底层大语言模型的推理能力，多智能体集体学习的能力仍处于早期，突破这些瓶颈后即可实现端到端全业务工作流自动化。

---

### 智能体未来的五大假设
![Future Agent Hypotheses](images/fig4.png)
*图 4：关于智能体未来的五个假设*

1. **通用智能体的崛起**：AI 智能体将从领域专家演进为能够高可靠管理复杂、模糊、长期目标的通用智能体；也可能通过小型专业智能体组合的「乐高模式」实现，两种路径并不冲突，可以互补。
2. **深度个性化与主动发现目标**：智能体将成为深度个性化的主动合作伙伴，从被动响应指令转向学习用户模式、主动预测需求，帮助用户实现尚未清晰表达的目标。
3. **具身化与物理世界交互**：智能体将脱离纯数字边界，和机器人结合形成具身智能体，在物理世界执行任务，弥合数字智能和物理行动的鸿沟。
4. **智能体驱动的经济**：高度自主的智能体将成为独立经济参与者，以最大化特定目标（如利润）为导向自主运行，创造超高效率的全新智能体经济。
5. **目标驱动的、可演化的多智能体系统**：未来智能系统将基于用户声明的目标自主运行，能够动态调整自身多智能体架构：根据任务需求创建、复制、移除智能体，从架构、指令多个层面动态优化，自主适配目标。

---

## 引用证据片段
> 智能体的普及速度惊人。根据最近的研究，大多数大型 IT 公司正在积极使用这些智能体，其中五分之一的公司是在过去一年内才开始使用的。金融市场也注意到了这一点。到 2024 年底，AI 智能体初创公司已筹集了超过 20 亿美元，市场估值达到 52 亿美元。预计到 2034 年，其市场价值将爆炸式增长至近 2000 亿美元。简而言之，所有迹象都表明 AI 智能体将在我们未来的经济中扮演极为重要的角色。

---

## 参考文献
1. Cloudera, Inc. (April 2025), 96% of enterprises are increasing their use of AI agents. [https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html](https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html)
2. Deloitte, Autonomous generative AI agents. [https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html)
3. Market.us. Global Agentic AI Market Size, Trends and Forecast 2025–2034. [https://market.us/report/agentic-ai-market/](https://market.us/report/agentic-ai-market/)

---

## 导航
[[05-Introduction|< Previous Chapter]] | [[000-Home|Home]] | [[07-Chapter-01-Prompt-Chaining|Next Chapter >]]
