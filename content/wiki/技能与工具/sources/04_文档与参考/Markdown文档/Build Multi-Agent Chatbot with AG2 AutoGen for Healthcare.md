---
source: raw/04_文档与参考/Markdown文档/Build Multi-Agent Chatbot with AG2 AutoGen for Healthcare.md
raw_sha256: 9057f4a66165014265ae8a5ec78f276964e1057b308281fd4c729d083eeedbcc
compiled_at: 2026-04-14T03:50:38.470Z
---
<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

# Build a Multi-Agent Chatbot with AG2 (AutoGen) for Healthcare

> 来源路径：`raw/04_文档与参考/Markdown文档/Build Multi-Agent Chatbot with AG2 AutoGen for Healthcare.md`

## TL;DR
本文是一个时长约30分钟的指导项目教程，介绍如何使用微软开源的AG2（AutoGen）多智能体框架搭建面向医疗场景的多智能体对话系统AutoMed。教程涵盖AutoGen基础概念、环境配置、核心组件使用说明，并提供了完整的AutoMed实现代码，最后布置了一个搭建心理健康聊天机器人的练习。

> [!WARNING] 医疗免责声明：本项目仅用于教授AG2（AutoGen）开发技术，项目提供的医疗建议不能替代专业医疗咨询、诊断或治疗，任何健康问题请务必咨询合格医疗专业人员。

---

## 要点
- AutoMed是基于AG2（AutoGen）的多智能体AI系统，通过多个分工明确的专用智能体协作，模拟真实医疗团队的问诊流程，可提供比传统单智能体聊天机器人更精准、个性化的医疗建议
- AutoGen是微软推出的开源多智能体框架，核心优势包括支持多智能体协作、LLM驱动的对话、自动化工作流编排、支持人机协作
- 搭建AutoMed使用了AutoGen核心组件：`ConversableAgent`（可对话智能体）、`GroupChat`（群组对话管理器）、`GroupChatManager`（群组对话协调器）
- 本教程提供完整可运行的代码示例，结尾附带练习：基于同样架构搭建一个心理健康多智能体聊天机器人

---

## 目录
<ol>
    <li><a href="#Objectives">学习目标</a></li>
    <li>
        <a href="#Setup">环境配置</a>
        <ol>
            <li><a href="#Installing-Required-Libraries">安装依赖库</a></li>
            <li><a href="#Importing-Required-Libraries">导入依赖库</a></li>
        </ol>
    </li>
    <li><a href="#什么是AutoGen">什么是AutoGen</a></li>
    <li><a href="#AutoGen的核心特性">AutoGen的核心特性</a></li>
    <li><a href="#对比-AutoGen-vs-传统AI智能体">对比：AutoGen vs 传统AI智能体</a></li>
    <li><a href="#AutoMed工作流程：多智能体AI实践">AutoMed工作流程：多智能体AI实践</a></li>
    <li><a href="#为什么使用GPT-4o">为什么使用GPT-4o</a></li>
    <li><a href="#什么是-ConversableAgent">什么是 ConversableAgent</a></li>
    <li><a href="#什么是-GroupChat">什么是 GroupChat</a></li>
    <li><a href="#练习：使用AutoGen库搭建心理健康聊天机器人">练习：使用AutoGen库搭建心理健康聊天机器人</a></li>
</ol>

<ul>
    <li><a href="#作者">作者</a></li>
    <li><a href="#贡献者">贡献者</a></li>
    <li><a href="#更新日志">更新日志</a></li>
</ul>

---

## 学习目标 {#Objectives}

完成本实验后，你将能够：
- 理解AG2（AutoGen）如何为复杂工作流启用多智能体AI系统
- 掌握AG2（AutoGen）如何与GPT-4这类大语言模型集成，实现动态AI驱动对话
- 实现智能体间通信，支撑智能医疗决策
- 开发多个可交互协作的AI智能体，处理不同医疗健康任务

----

## 环境配置 {#Setup}

本实验需要使用以下依赖库：
*   [`AG2 (AutoGen)`](https://microsoft.github.io/autogen/0.2/docs/installation/)：用于编排多智能体AI交互，自动化基于LLM的工作流
*   [`OpenAI`](https://platform.openai.com/docs/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01)：用于将OpenAI大语言模型集成到AI工作流中
*   [`python-dotenv`](https://pypi.org/project/python-dotenv/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01)：用于管理环境变量，安全加载API密钥和配置

### 安装依赖库 {#Installing-Required-Libraries}

Skills Network Labs环境未预装以下依赖库，你必须运行下方代码单元完成安装。该步骤可能需要**数分钟**，请耐心等待：

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/crvBKBOkg9aBzXZiwGEXbw/Restarting-the-Kernel.png" width="50%" alt="Restart kernel">

**注意**：如果遇到问题，点击**Restart the kernel**图标重启内核后重新运行即可。

```python
!pip install autogen==0.7 openai==1.64.0 python-dotenv==1.1.0 | tail -n 1
```

### 导入依赖库 {#Importing-Required-Libraries}

导入所有需要的库：

```python
import warnings

# Suppress autogen and other deprecation/user warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings('ignore', category=UserWarning)

from autogen import ConversableAgent, GroupChat, GroupChatManager
from openai import OpenAI
import logging
```

```python
# Suppress warnings from autogen.oai.client
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)
```

---

## 什么是AutoGen {#什么是AutoGen}

AutoGen是微软开发的开源框架，允许开发者使用多个AI智能体编排和优化AI工作流。这些智能体可以协作、自动决策，并在复杂问题解决任务中动态生成响应。

与传统孤立工作的AI系统不同，AutoGen支持多个AI智能体（GPT这类大语言模型）交互、交换信息并优化输出，因此更强大灵活，可适配多种应用场景。

## AutoGen的核心特性 {#AutoGen的核心特性}

### 1. 多智能体协作

AutoGen允许多个AI智能体通信协作解决任务。每个智能体可以拥有特定角色，例如问题解决者、验证者或优化器。

示例：
- 一个智能体生成代码，另一个评审代码，第三个测试代码
- 研究智能体收集信息，另一个智能体汇总信息

### 2. 面向对话和任务的AI

AutoGen支持LLM驱动的对话，AI智能体可以进行多轮对话优化答案。

示例：
- 一个聊天机器人可以咨询不同的AI智能体，例如一个提供法律咨询，另一个提供金融建议
- 客户支持AI可以将未解决的问题升级给另一个AI智能体处理

### 3. 自动化工作流编排

你可以为AI驱动的自动化编排工作流，例如AI辅助编程、研究、文档生成。

示例：
- 自动化软件调试，AI识别问题、提出修复方案并验证解决方案

### 4. 支持人机协作

AutoGen允许人类介入AI驱动的工作流，必要时提供反馈或手动引导智能体。

示例：
- 研究助理AI起草报告，由人类专家优化内容

## 对比：AutoGen vs 传统AI智能体 {#对比-AutoGen-vs-传统AI智能体}

<table width="60%" align="left" >
        <thead>
            <tr>
                <th>特性</th>
                <th>传统AI智能体</th>
                <th>AutoGen AI智能体</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td
