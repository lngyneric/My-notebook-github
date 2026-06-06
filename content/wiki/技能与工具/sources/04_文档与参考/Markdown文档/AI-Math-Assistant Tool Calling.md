---
source: raw/04_文档与参考/Markdown文档/AI-Math-Assistant Tool Calling.md
raw_sha256: 95adec2f27faf780110374f498918003c2e9c419d78cdc6fe4b22f0cf924b52b
compiled_at: 2026-04-14T03:49:49.589Z
---
# 构建基于 LangChain 工具调用的 AI 数学助手
> 来源路径：`raw/04_文档与参考/Markdown文档/AI-Math-Assistant Tool Calling.md`
> 标签：`LangChain` `AI` `教程` | 创建日期：2026-01-08 | 预计完成时间：45 分钟

---

## TL;DR
本文是一份实操教程，介绍如何使用 LangChain 框架创建自定义工具、构建支持工具调用的 AI 智能体，最终实现一个能处理自然语言数学查询的数学助手。教程包含工具创建的两种方法、智能体选型、多工具编排、错误调试、内置工具使用全流程，并附带课后练习巩固知识点。

---

## 目录
1. [[#目标|目标]]
2. [[#实验设置|实验设置]]
3. [[#安装与导入依赖|安装与导入依赖]]
4. [[#加载语言模型|加载语言模型]]
5. [[#工具与函数基础|工具与函数基础]]
   - 5.1 [[#LangChain工具创建方法|LangChain 工具创建方法]]
   - 5.2 [[#智能体与initialize_agent|智能体与 `initialize_agent`]]
   - 5.3 [[#新一代create_react_agent|新一代 `create_react_agent`]]
6. [[#构建数学工具箱与智能体|构建数学工具箱与智能体]]
7. [[#使用LangChain内置工具|使用 LangChain 内置工具]]
8. [[#练习：创建乘方计算工具|练习：创建乘方计算工具]]
9. [[#作者|作者]]

---

## 目标
完成本实验后，你将能够：
- 解释 LangChain 中工具（Tools）的概念
- 创建用于特定任务的自定义工具
- 构建一个可以使用多个工具的 AI 智能体
- 调试并改进工具的功能
- 使用各种输入测试工具的实现

---

## 实验设置
本实验将使用以下核心库：
- **`langchain`**: 用于创建 AI 智能体和工具
- **`langchain.chat_models`**: 用于访问语言模型
- **`langchain.agents`**: 用于创建和管理 AI 智能体

### API 免责声明
> [!IMPORTANT] 重要提示
> 本实验使用 **IBM watsonx.ai** 和 **OpenAI** 提供的 LLM，Skills Network 实验环境已配置免 API 密钥的有限免费使用额度。如果你在实验环境**外本地运行本项目，必须配置你自己的 API 密钥，并自行承担相关费用**。

本地运行配置示例：
```python
from langchain_openai import ChatOpenAI
from langchain_ibm import ChatWatsonx

openai_llm = ChatOpenAI(
    model="gpt-4.1-nano",
    api_key = "your openai api key here",
)

watsonx_llm = ChatWatsonx(
    model_id="ibm/granite-3-2-8b-instruct",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="your project id associated with the API key",
    api_key="your watsonx.ai api key here",
)
```

---

## 安装与导入依赖
> [!WARNING] 警告
> 以下依赖库未预安装在 Skills Network Labs 环境中，你需要执行以下命令完成安装：

```python
%pip install langchain==0.3.23 | tail -n 1 
%pip install langchain-ibm==0.3.10 | tail -n 1 
%pip install langchain-community==0.3.16 | tail -n 1 
%pip install wikipedia==1.4.0 | tail -n 1
%pip install openai==1.77.0 | tail -n 1
%pip install langchain-openai==0.3.16 | tail -n 1
```

导入依赖：
```python
from langchain_ibm import ChatWatsonx
from langchain.agents import AgentType
import re
```

---

## 加载语言模型
本实验默认使用 IBM 的 `ChatWatsonx` 加载 Granite 系列大模型，不同厂商的 LLM 各有优势：
| LLM 提供商 | 优势 |
|---|---|
| OpenAI (GPT-4/GPT-3.5) | 通用性强，擅长高级推理 |
| Meta (LLaMA) | 开放可自定义，适合专用场景 |
| IBM watsonx Granite | 适合企业场景，集成能力强 |
| Anthropic (Claude) | 专注安全、可靠、合乎伦理的 AI |
| Cohere | 性价比高，适合轻量特定任务 |

本实验选择 `ChatWatsonx` 的原因：
- API 简单，可快速完成配置
- 支持高级配置，可调整 `temperature`（响应随机性）、`max_tokens`（响应长度）
- IBM Granite 模型被广泛认为是通用推理和对话的 SOTA 模型之一

初始化代码：
```python
llm = ChatWatsonx(
    model_id="ibm/granite-3-2-8b-instruct",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="skills-network",
)
```

测试：
```python
response = llm.invoke("What is tool calling in langchain?")
print("\nResponse Content: ", response.content)
```

---

## 工具与函数基础
在 AI 工具调用中，工具本质是封装了特定能力的可调用函数，可以类比为工具箱中的单个工具。

构建工具需要遵循以下核心原则：
1. **明确的目的**：确保工具的职责定义清晰
2. **标准化的输入**：工具接受可预测的结构化输入
3. **一致的输出**：以易于处理、易于集成的格式返回结果
4. **全面的文档**：清晰说明工具的功能、用法和限制（文档同时会帮助 LLM 理解工具用途）

我们先实现一个最基础的加法函数：
```python
def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input dictionary or extracts numbers from a string.

    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.

    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.

    Example Input (Dictionary):
    {"numbers": [10, 20, 30]}

    Example Input (String):
    "Add the numbers 10, 20, and 30."

    Example Output:
    {"result": 60}
    """
    numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]

    
    result = sum(numbers)
    return {"result": result}
```

测试函数：
```python
add_numbers("1 2") 
```

---

### LangChain 工具创建方法
LangChain 提供两种主流方式将普通 Python 函数包装为智能体可用的工具。

#### 方法1：`Tool` 类包装
`Tool` 是基础的包装类，每个工具需要三个核心组件：唯一名称、实际执行函数、帮助智能体理解用法的描述。
```python
from langchain.agents import Tool
add_tool=Tool(
        name="AddTool",
        func=add_numbers,
        description="Adds a list of numbers and returns the result.")

print("tool object",add_tool)
```

工具对象核心属性：
| 属性 | 作用 | 示例 |
|---|---|---|
| `name` | 工具的唯一标识符 | `"AddTool"` |
| `.invoke` | 工具包装的可调用函数 | `add_numbers` |
| `description` | 工具功能的简明说明 | `"Adds a list of numbers and returns the result."` |

查看属性示例：
```python
# Tool name
print("Tool Name:")
print(add_tool.name)

# Tool description
print("Tool Description:")
print(add_tool.description)

# Tool function
print("Tool Function:")
print(add_tool.invoke)
```

调用工具：
```python
print("Calling Tool Function:")
test_input = "10 20 30 a b" 
print(add_tool.invoke(test_input))  # Example
```

测试工具的意义：
1. 确认工具配置正确：元数据配置正确，函数和模式配置符合预期
2. 确认被包装函数符合预期：能正确完成任务，能优雅处理边缘情况和无效输入
3. 确认工具和智能体兼容：工具输出符合智能体要求，不会出现兼容性问题

####
