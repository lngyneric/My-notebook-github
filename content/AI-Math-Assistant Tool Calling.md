---
title: 构建基于 LangChain 工具调用的 AI 数学助手
tags: [LangChain, AI, 教程]
date: 2026-01-08
---

# 构建基于 LangChain 工具调用的 AI 数学助手

> [!INFO] 预计所需时间：**45** 分钟

在本实验中，你将学习如何使用 LangChain 构建一个简单的智能体（Agent），使 AI 能够执行特定任务。你将创建一个数学工具箱，允许 AI 智能体通过自然语言交互执行基本的算术运算。

通过本实验，你将构建一个能够理解并解决诸如“25 加上 15，然后乘以 2”这类数学查询的智能体，它能将复杂的操作分解为简单的步骤。

# 目录

1. [[#Objectives|目标]]
2. [[#Setup|设置]]
3. [[#Installing required libraries|安装所需库]]
4. [[#Loading the LLM: Choosing the right language model|加载 LLM：选择合适的语言模型]]
5. [[#Function|函数]]
   - 5.1 [[#Tool|工具]]
   - 5.2 [[#initialize_agent|initialize_agent]]
6. [[#Relationship between agent and LLM|智能体与 LLM 的关系]]
7. [[#Key parameters of initialize_agent|initialize_agent 的关键参数]]
8. [[#Orchestrating multiple tools with an agent: Mathematical toolkit|使用智能体编排多个工具：数学工具箱]]
   - 8.1 [[#Subtraction tool|减法工具]]
9. [[#Building the agent|构建智能体]]
   - 9.1 [[#Exploring LangChain's built-in tools|探索 LangChain 的内置工具]]
   - 9.2 [[#Popular built-in tools|常用的内置工具]]
   - 9.3 [[#Example: Using the Wikipedia tool|示例：使用 Wikipedia 工具]]
10. [[#Exercise: Create a power tool to calculate exponents|练习：创建一个计算指数的乘方工具]]
    - 10.1 [[#Objective|目标]]
    - 10.2 [[#Step 1: Create the power tool|步骤 1：创建乘方工具]]
    - 10.3 [[#Step 2: Create an agent with the power tool|步骤 2：使用乘方工具创建智能体]]
    - 10.4 [[#Step 3: Test the agent|步骤 3：测试智能体]]
11. [[#Authors|作者]]


## 目标

完成本实验后，你将能够：

- 解释 LangChain 中工具（Tools）的概念
- 创建用于特定任务的自定义工具
- 构建一个可以使用多个工具的 AI 智能体
- 调试并改进工具的功能
- 使用各种输入测试工具的实现


----


## 设置



在本实验中，你将使用以下库：

- **`langchain`**: 用于创建 AI 智能体和工具
- **`langchain.chat_models`**: 用于访问语言模型
- **`langchain.agents`**: 用于创建和管理 AI 智能体

---


## 安装所需库

> [!WARNING] 警告
> 以下所需的库**未**预安装在 Skills Network Labs 环境中。**你需要运行以下单元格**来安装它们：



```python
%pip install langchain==0.3.23 | tail -n 1 
%pip install langchain-ibm==0.3.10 | tail -n 1 
%pip install langchain-community==0.3.16 | tail -n 1 
%pip install wikipedia==1.4.0 | tail -n 1
%pip install openai==1.77.0 | tail -n 1
%pip install langchain-openai==0.3.16 | tail -n 1
```

## 导入所需库



```python
from langchain_ibm import ChatWatsonx
from langchain.agents import AgentType
import re
```

## 加载 LLM：选择合适的语言模型

在这个例子中，我们将使用 IBM 的 `ChatWatsonx` 来加载一个语言模型（LLM）以与工具进行交互。IBM 的模型（如 Granite 3.2 和 Granite 3.3）具有高度的多功能性，擅长高级推理任务。

话虽如此，其他提供商也提供具有不同优势的 LLM：

- **OpenAI (GPT-4/GPT-3.5)**: 最适合多功能性和高级推理。
- **Facebook (Meta, LLaMA)**: 开放访问，高度可定制，适用于专门的用例。
- **IBM watsonx Granite**: 极其适合企业应用，具有无缝集成能力。
- **Anthropic (Claude)**: 专注于安全性、可靠性和合乎道德的 AI。
- **Cohere**: 价格实惠且高效，适用于轻量级、特定任务的模型。

---

对于本项目，你将使用 `ChatWatsonx`，因为：
- 它提供了一个简单的 API 用于快速设置。
- 它支持高级配置，如：
  - **`temperature`**: 调整响应的随机性。
  - **`max_tokens`**: 限制响应的长度。
- IBM 的模型被广泛认为是通用推理和对话的最先进模型。



```python
llm = ChatWatsonx(
    model_id="ibm/granite-3-2-8b-instruct",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="skills-network",
)
```

让我们生成一个简单的响应：



```python
response = llm.invoke("What is tool calling in langchain?")
print("\nResponse Content: ", response.content)
```

## API 免责声明

> [!IMPORTANT] 重要提示
> 本实验使用 **IBM watsonx.ai** 和 **OpenAI** 提供的 LLM。此环境已配置为允许在没有 API 密钥的情况下使用 LLM，因此你可以**免费（有限制）**地提示它们。考虑到这一点，如果你希望在 Skills Network 的 JupyterLab 环境**之外本地运行**此笔记本，你必须**配置你自己的 API 密钥**。请注意，使用你自己的 API 密钥意味着你将承担个人费用。


### 本地运行

如果你在本地运行此实验，你需要配置你自己的 API 密钥。本实验使用 `langchain` 中的 `ChatOpenAI` 和 `ChatWatsonx` 模块。下面显示了这两种配置及其说明。请在整个实验中用下面完整的模块**替换所有实例**。如果你不是在本地运行，**请勿**运行下面的单元格，这会导致错误。

> [!CAUTION] 如果你不是在本地运行，请忽略此部分

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




## 函数

在 AI 中，**工具（Tool）**会调用一个基本的**函数（Function）**或能力，可以被调用来执行特定任务。把它想象成工具箱里的单个物品：就像锤子、螺丝刀或扳手一样，AI 工具箱里装满了旨在解决问题或完成工作的特定函数。

在构建用于工具调用的工具时，有几个关键原则需要牢记：

1. **明确的目的**：确保工具具有定义明确的工作。
2. **标准化的输入**：工具应接受可预测的、结构化格式的输入，以便于使用。
3. **一致的输出**：始终以易于处理或与其他系统集成的格式返回结果。
4. **全面的文档**：你的工具应包含清晰、简单的文档，解释它做什么、如何使用它以及任何怪癖或限制。

请记住，文档不仅是为了给其他开发人员看，也是为了让语言模型（LLM）理解工具的目的以及如何有效地使用它。

在这个例子中，你将从一个简单的数字相加工具开始。它将满足大多数基本要求，但一个关键限制是它不处理**基本错误情况**，比如忽略非数字输入。改进错误处理将使工具更加健壮，并为实际使用做好准备。



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

直接测试工具可以让你查明问题所在——无论是工具的逻辑、输入解析还是输出格式。
在这里，你将输入字符串 `1 2` 并获得总和。



```python
add_numbers("1 2") 
```


## 工具
LangChain 中的 `Tool` 类作为一个结构化包装器，将常规 Python 函数转换为兼容智能体的工具。每个工具都需要三个关键组件：
1. 一个标识工具的名称
2. 执行实际操作的函数
3. 一个帮助智能体理解何时使用该工具的描述

测试部分改进：





```python
from langchain.agents import Tool
add_tool=Tool(
        name="AddTool",
        func=add_numbers,
        description="Adds a list of numbers and returns the result.")

print("tool object",add_tool)
```

让我们看看对象的参数：

- **`name`** (*str*):
  - 工具的唯一标识符。
  - **示例**: `"AddTool"`

- **`.invoke`** (*Callable*):
  - 工具包装的函数。
  - **示例**: `add_numbers`

- **`description`** (*str*):
  - 关于工具功能的简明解释。
  - **示例**: `"Adds a list of numbers and returns the result."`




这些属性允许你检查工具对象



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

你可以通过 ```add_tool``` 对象调用工具的函数：



```python
print("Calling Tool Function:")
test_input = "10 20 30 a b" 
print(add_tool.invoke(test_input))  # Example
```

测试工具对象可以确保：

1. **工具设置正确**：
   - 元数据（`name`, `description` 等）已正确定义并与其用途一致。
   - 函数和模式（如适用）已正确配置。

2. **被包装的函数表现符合预期**：
   - 函数正确执行预期的任务。
   - 它优雅地处理边缘情况和无效输入。

3. **工具与智能体顺利集成**：
   - 工具的输出与智能体的预期一致。
   - 智能体调用工具时没有兼容性问题。


### `@tool` 操作符

现在你知道了如何使用 `Tool` 类（使用 Tool 接口）创建工具，实际上还有另一种方法，即使用 `@tool` 装饰器来创建工具。推荐的创建工具的方法是使用 `@tool` 装饰器。这个装饰器旨在简化工具创建过程，并且应该在大多数情况下使用。定义函数后，你可以用 `@tool` 装饰它，以创建一个实现 Tool 接口的工具。

`@tool` 操作符将函数制作成工具。见下文：



```python
from langchain_core.tools import tool
import re

@tool
def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input string.
    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.
    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.
    Example Input:
    "Add the numbers 10, 20, and 30."
    Example Output:
    {"result": 60}
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    # numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    
    result = sum(numbers)
    return {"result": result}
```

上面的函数现在将作为一个工具。你可以使用以下命令检查工具的模式和其他属性：



```python
print("Name: \n", add_numbers.name)
print("Description: \n", add_numbers.description) 
print("Args: \n", add_numbers.args) 

```

你可以使用 ```invoke``` 方法调用该工具。



```python
test_input = "what is the sum between 10, 20 and 30 " 
print(add_numbers.invoke(test_input))  # Example
```


### 使用 @tool-StructuredTool

`@tool` 装饰器创建了一个 `StructuredTool`，其中包含从函数签名和文档字符串中提取的模式信息，如下所示。这有助于 LLM 更好地理解工具期望的输入以及如何正确使用它。虽然两种方法都有效，但 `@tool` 通常是现代 LangChain 应用程序的首选，尤其是在使用 LangGraph 和函数调用模型时。



```python
# Comparing the two approaches
print("Tool Constructor Approach:")

print(f"Has Schema: {hasattr(add_tool, 'args_schema')}")
print("\n")

print("@tool Decorator Approach:")


print(f"Has Schema: {hasattr(add_numbers, 'args_schema')}")
print(f"Args Schema Info: {add_numbers.args}")
```

在这个例子中，工具由两个输入：一个包含要相加的数字的字符串，以及第二个布尔输入，决定是否对这些数字的绝对值求和。



```python
from typing import List

@tool
def add_numbers_with_options(numbers: List[float], absolute: bool = False) -> float:
    """
    Adds a list of numbers provided as input.

    Parameters:
    - numbers (List[float]): A list of numbers to be summed.
    - absolute (bool): If True, use the absolute values of the numbers before summing.

    Returns:
    - float: The total sum of the numbers.
    """
    if absolute:
        numbers = [abs(n) for n in numbers]
    return sum(numbers)
```

让我们比较一下 `add_numbers_with_options` 和 `add_numbers` 的参数。两者都是结构化工具。它们都包含 `inputs` 字段，这是一个字符串输入。然而，`add_numbers_with_options` 有一个额外的键值对：`absolute`，这是一个默认值为 `False` 的布尔字段。这意味着 `add_numbers_with_options` 支持可选行为——取数字的绝对值——而 `add_numbers` 仅处理基本的数字提取和求和。



```python
print(f"Args Schema Info: {add_numbers_with_options.args}")
print(f"Args Schema Info: {add_numbers.args}")
```

你可以使用字典作为输入来调用工具，其中每个键对应一个参数名称，值是该参数的输入。例如，要控制是正常求和还是使用绝对值求和，请将 `absolute` 标志设置为 `False` 或 `True`：你将分别得到 -6 和 6。



```python
print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":False}))
print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":True}))
```

## 使用 Python 类型提示改进工具返回类型

创建工具时，必须准确指定其返回值。这有助于智能体理解和处理不同的可能输出。



函数 `sum_numbers_with_complex_output` 返回更灵活的输出格式。当成功求和数字时，它返回包含浮点值的字典；如果未找到数字或处理过程中发生问题，则返回作为字符串的描述性错误消息。

```python
from typing import Dict, Union

@tool
def sum_numbers_with_complex_output(inputs: str) -> Dict[str, Union[float, str]]:
    """
    Extracts and sums all integers and decimal numbers from the input string.

    Parameters:
    - inputs (str): A string that may contain numeric values.

    Returns:
    - dict: A dictionary with the key "result". If numbers are found, the value is their sum (float). 
            If no numbers are found or an error occurs, the value is a corresponding message (str).

    Example Input:
    "Add 10, 20.5, and -3."

    Example Output:
    {"result": 27.5}
    """
    matches = re.findall(r'-?\d+(?:\.\d+)?', inputs)
    if not matches:
        return {"result": "No numbers found in input."}
    try:
        numbers = [float(num) for num in matches]
        total = sum(numbers)
        return {"result": total}
    except Exception as e:
        return {"result": f"Error during summation: {str(e)}"}
```

函数 `sum_numbers_from_text` 返回一个直接的输出格式。它从输入字符串中提取所有整数值，对它们求和，并以浮点数形式返回总数。此函数假设输入中至少存在一个有效数字，并且不处理未找到数字或可能发生错误的情况。



```python
@tool
def sum_numbers_from_text(inputs: str) -> float:
    """
    Adds a list of numbers provided in the input string.
    
    Args:
        text: A string containing numbers that should be extracted and summed.
        
    Returns:
        The sum of all numbers found in the input.
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    result = sum(numbers)
    return result
```

### `initialize_agent`

当你设置一个智能体时，你正在连接工具和 LLM 以便无缝协作。智能体使用 LLM 来理解需要做什么，并根据任务决定使用哪个工具。以下是关键部分的简单概述：


#### **智能体与 LLM 的关系**
- **智能体（Agent）**充当决策者，弄清楚使用哪些工具以及何时使用。
- **LLM** 是推理引擎。它：
  - 解释用户的输入。
  - 帮助智能体做决定。
  - 根据工具的输出生成响应。

把智能体想象成分配任务的经理，把 LLM 想象成解决问题或委派工作的大脑。

---

#### **`initialize_agent` 的关键参数**

1. **`tools`** - 见上文

2. **`llm`** - 见上文

3. **`agent`**:
   - 指定智能体的推理框架。
   - `"zero-shot-react-description"` 启用：
     - **零样本推理（Zero-shot reasoning）**：智能体可以通过一步步思考问题来解决以前从未见过的任务。
     - **React 框架**：一个逻辑循环：
       - **Reason (推理)** → 思考任务。
       - **Act (行动)** → 使用工具执行动作。
       - **Observe (观察)** → 检查工具的输出。
       - **Plan (计划)** → 决定下一步做什么。

4. **`verbose`**:
   - 如果为 `True`，它会打印智能体思维过程的详细日志。
   - 对调试或理解智能体如何做决定很有用。




你现在可以使用 `initialize_agent` 创建一个智能体对象。



```python
from langchain.agents import initialize_agent

agent = initialize_agent([add_tool], llm, agent="zero-shot-react-description", verbose=True, handle_parsing_errors=True)
```

现在，你可以通过提问来运行智能体。


> [!NOTE] 注意
> 当使用 `.run()` 或 `.invoke()` 运行智能体时，你可能会偶尔遇到代码无限期执行的情况，即使 LLM 已经产生了一个有效的答案。这通常发生在系统遇到 `OUTPUT_PARSING_ERROR` 时——通常是由于 LLM 响应中的格式问题。
>
> 在这种情况下，智能体可能会陷入循环并且不会自行终止。如果你看到这种情况发生，只需点击顶部工具栏中的停止按钮 (■) 中断执行。



```python
# Use the agent
response =agent.run("In 2023, the US GDP was approximately $27.72 trillion, while Canada's was around $2.14 trillion and Mexico's was about $1.79 trillion what is the total.")
```


```python
response
```


```python
agent.invoke({"input": "Add 10, 20, two and 30"})
```

智能体被要求将数字 10, 20, "two" 和 30 相加。智能体首先注意到其中一个输入是单词 "two" 而不是数字，因此它将 "two" 转换为数字形式，即 2。在准备好数字列表（10, 20, 2 和 30）后，智能体决定使用 `AddTool` 来执行加法。它将数字传递给工具，工具计算总和并返回结果 62。最后，智能体提供了答案：**62**。


#### **结构化聊天零样本 React 描述 (Structured chat zero shot react-description)**

在 LangChain 中选择智能体时，两个因素很重要：智能体类型和工具格式，尤其是工具的返回类型。像 `zero-shot-react-description` 这样的智能体期望工具接收并返回纯字符串，这与手动定义的 `Tool(...)` 包装器配合良好。

相比之下，像 `structured-chat-zero-shot-react-description` 或 `openai-functions` 这样的结构化智能体是为通过 `@tool` 装饰器处理结构化输入和输出而构建的。如果工具返回一个字典但智能体期望一个字符串，可能会导致键错误或解析失败。


在下面的智能体示例中，使用 `sum_numbers_from_text` 作为工具，使用 `structured-chat-zero-shot-react-description` 作为智能体类型。对于 LLM，你将使用 `Granite`。



```python
agent_2 = initialize_agent([sum_numbers_from_text], llm, agent="structured-chat-zero-shot-react-description", verbose=True, handle_parsing_errors=True)
response = agent_2.invoke({"input": "Add 10, 20 and 30"})
print(response)
```

现在，对于下面的智能体，你将使用 `sum_numbers_with_complex_output` 作为工具。至于 LLM，你将使用 `gpt-4.1-nano` 和智能体类型 `openai-functions`。

这里需要注意的一点是，某些 LLM（如 `Granite`）无法解包字典输出，因为它们缺乏对结构化输出解析的原生支持。结果是，当你将 `sum_numbers_with_complex_output` 与 `structured-chat-zero-shot-react-description` 智能体类型一起使用时，智能体无法解释返回的字典，并抛出输入验证或解析错误。



```python
from langchain_openai import ChatOpenAI

llm_ai = ChatOpenAI(model="gpt-4.1-nano")
```


```python
agent_3 = initialize_agent([sum_numbers_with_complex_output], llm_ai, agent="openai-functions", verbose=True, handle_parsing_errors=True)
response = agent_3.invoke({"input": "Add 10, 20 and 30"})
print(response)
```

现在，让我们转向具有多个输入的工具。下面的智能体使用 `Granite` 作为 LLM，使用 `add_numbers_with_options` 作为工具，该工具接受多个输入参数。但是，如果工具返回复杂的输出——例如像 `sum_numbers_with_complex_output` 中的字典——你需要切换到像 GPT 这样的模型，并使用支持多输入工具和结构化输出的智能体类型。Granite 和类似模型可能无法可靠地处理复杂的输出解析，尤其是在与 `structured-chat-zero-shot-react-description` 等智能体一起使用时。



```python
agent_2 = initialize_agent(
    [add_numbers_with_options],
    llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True
)
```


```python
response = agent_2.invoke({
    "input": "Add -10, -20, and -30 using absolute values."
})
print(response)
```

让我们用 OpenAI 试试，看看它是否能处理多个输入。



```python
agent_openai = initialize_agent(
    [add_numbers_with_options],
    llm_ai,
    agent="openai-functions",
    verbose=True
)
```


```python
response = agent_openai.invoke({
    "input": "Add -10, -20, and -30 using absolute values."
})
print(response)
```

### **`create_react_agent`**

随着 LangChain 的 `AgentExecutor` 被弃用，来自 LangGraph 的 `create_react_agent` 为构建 AI 智能体提供了一个更灵活、更强大的替代方案。此函数创建一个基于图的智能体，该智能体与聊天模型一起工作并支持工具调用功能。

---

#### **`create_react_agent` 的关键参数**

1. **`model`**
    - 驱动智能体推理的语言模型。
    - 必须支持工具调用才能实现全部功能。

2. **`tools`**
    - 智能体可以用来执行动作的工具列表。
    - 可以是 LangChain 工具、带有 @tool 装饰器的 Python 函数或 ToolNode 实例。
    - 每个工具都应该有名称、描述和实现。

3. **`prompt (optional)`**:
    - 自定义给 LLM 的指令。
    - 可以是：
        - 字符串（转换为 SystemMessage）
        - SystemMessage 对象
        - 转换状态的函数
        - 处理状态的 Runnable

以及其他参数。要查看更多参数，请参阅 [文档](https://langchain-ai.github.io/langgraph/reference/prebuilt/)。

#### 它是如何工作的

与使用固定循环结构的旧版 `AgentExecutor` 不同，`create_react_agent` 创建一个具有这些关键节点的图：

1. **Agent Node (智能体节点)**：使用消息历史调用 LLM。
2. **Tools Node (工具节点)**：执行 LLM 响应中的任何工具调用。
3. **Continue/End Nodes (继续/结束节点)**：根据是否存在工具调用来管理工作流。

该图遵循此过程：

1. 用户消息进入图。
2. LLM 生成响应，可能带有工具调用。
3. 如果存在工具调用，则执行它们，并将其结果添加到消息历史记录中。
4. 更新后的消息被发送回 LLM。
5. 此循环继续，直到 LLM 响应且没有工具调用。
6. 返回包含所有消息的最终状态。



```python
%pip install langgraph==0.6.1 | tail -n 1
```


```python
from langgraph.prebuilt import create_react_agent

agent_exec = create_react_agent(model=llm, tools=[sum_numbers_from_text])
msgs = agent_exec.invoke({"messages": [("human", "Add the numbers -10, -20, -30")]})
```


```python
print(msgs["messages"][-1].content)
```

## 使用智能体编排多个工具：数学工具箱
在实际应用中，单个工具往往不足以应对用户请求的复杂性和多样性。诸如数据分析、执行计算或检索特定信息等任务需要专门的能力，而这些能力无法由单个函数完成。通过为智能体配备多个工具，每个工具都针对不同的目的，你可以创建一个能够根据用户的查询动态选择并利用适当工具的系统。这种方法增强了 AI 的灵活性和可扩展性，使其能够精确高效地处理广泛的任务。多个工具的编排确保智能体可以无缝管理复杂的工作流，使其成为构建健壮且多功能 AI 系统的重要框架。

为了演示这个概念，让我们创建额外的工具，即一个数学工具箱。除了加法工具外，你现在还将创建用于减法、乘法和除法的工具。这些工具将被集成到一个能够处理各种数学查询的智能体中，展示多个工具如何在单个 AI 系统中协同工作。

### 减法工具
减法工具旨在获取一个数字列表，并返回从第一个数字中减去所有后续数字的结果。此工具特别适用于处理涉及差值的查询，例如“100 减去 20 再减去 10 是多少？”。



```python
@tool
def subtract_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string, negates the first number, and successively subtracts 
    the remaining numbers in the list.

    This function is designed to handle input in string format, where numbers are separated 
    by spaces, commas, or other delimiters. It parses the string, extracts valid numeric values, 
    and performs a step-by-step subtraction operation starting with the first number negated.

    Parameters:
    - inputs (str): 
      A string containing numbers to subtract. The string may include spaces, commas, or 
      other delimiters between the numbers.

    Returns:
    - dict: 
      A dictionary containing the key "result" with the calculated difference as its value. 
      If no valid numbers are found in the input string, the result defaults to 0.

    Example Input:
    "100, 20, 10"

    Example Output:
    {"result": -130}

    Notes:
    - Non-numeric characters in the input are ignored.
    - If the input string contains only one valid number, the result will be that number negated.
    - Handles a variety of delimiters (e.g., spaces, commas) but does not validate input formats 
      beyond extracting numeric values.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]

    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Start with the first number negated
    result = -1 * numbers[0]

    # Subtract all subsequent numbers
    for num in numbers[1:]:
        result -= num

    return {"result": result}
```

你可以使用以下命令检查工具的模式和其他属性：



```python
print("Name: \n", subtract_numbers.name)
print("Description: \n", subtract_numbers.description) 
print("Args: \n", subtract_numbers.args) 
```

让我们通过调用函数直接使用它：



```python
print("Calling Tool Function:")
test_input = "10 20 30 and four a b" 
print(subtract_numbers.invoke(test_input))  # Example
```

现在让我们构建多个工具，从 `MultiplyTool` 和 `DivideTool` 开始，通过定义两个函数：`multiply_numbers` 和 `divide_numbers`。这些函数很简单 - `multiply_numbers` 接受字符串格式的数字列表并返回它们的乘积，而 `divide_numbers` 接受第一个数字并将其依次除以每个后续数字。你不用手动将这些函数包装在 Tool 类中，而是使用 `@tool` 装饰器自动将它们转换为 LangChain 工具，使用它们的文档字符串作为描述。这些装饰过的工具可以直接添加到智能体中，与其他操作（如加法或减法）并列，允许智能体根据用户的查询智能地选择适当的操作，使其在处理各种数学问题时具有多功能性。



```python
# Multiplication Tool
@tool
def multiply_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates their product.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the product of the numbers.

    Example Input:
    "2, 3, 4"

    Example Output:
    {"result": 24}

    Notes:
    - If no numbers are found, the result defaults to 1 (neutral element for multiplication).
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]
    print(numbers)

    # If no numbers are found, return 1
    if not numbers:
        return {"result": 1}

    # Calculate the product of the numbers
    result = 1
    for num in numbers:
        result *= num
        print(num)

    return {"result": result}
```


```python
# Division Tool
@tool
def divide_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates the result of dividing the first number 
    by the subsequent numbers in sequence.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the quotient.

    Example Input:
    "100, 5, 2"

    Example Output:
    {"result": 10.0}

    Notes:
    - If no numbers are found, the result defaults to 0.
    - Division by zero will raise an error.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]


    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Calculate the result of dividing the first number by subsequent numbers
    result = numbers[0]
    for num in numbers[1:]:
        result /= num

    return {"result": result}
```

直接测试这些数学工具时，请注意使用原始字符串输入（如 "2, 3, and four" 或 "100, 5, two"）将会失败。这些工具旨在仅处理数字输入——它们不具备 LLM 智能体层所具有的自然语言理解能力。要正确测试，你需要使用数值：



```python
# Testing multiply_tool
multiply_test_input = "2, 3, and four "
multiply_result = multiply_numbers.invoke(multiply_test_input)
print("--- Testing MultiplyTool ---")
print(f"Input: {multiply_test_input}")
print(f"Output: {multiply_result}")
```


```python
# Testing divide_tool
divide_test_input = "100, 5, two"
divide_result = divide_numbers.invoke(divide_test_input)
print("--- Testing DivideTool ---")
print(f"Input: {divide_test_input}")
print(f"Output: {divide_result}")
```

## 构建智能体

随着数学运算符——加法、减法、乘法和除法——的实现，你已经建立了一个简单但功能齐全的数学工具箱。与之前不同的是，智能体现在不仅必须选择适当的工具并处理输入，还必须根据用户的查询确定正确的数学运算。

让我们创建智能体对象。首先，将所有工具合并到一个列表中：



```python
tools = [add_numbers,subtract_numbers, multiply_numbers, divide_numbers]
tools
```

像以前一样，你将使用工具和语言模型作为输入来创建智能体。



```python
from langgraph.prebuilt import create_react_agent

# Create the agent with all tools
math_agent = create_react_agent(
    model=llm,
    tools=tools,
    # Optional: Add a system message to guide the agent's behavior
    prompt="You are a helpful mathematical assistant that can perform various operations. Use the tools precisely and explain your reasoning clearly."
)
```


```python
response = math_agent.invoke({
    "messages": [("human", "What is 25 divided by 4?")]
})

# Get the final answer
final_answer = response["messages"][-1].content
print(final_answer)
```


```python
response_2 = math_agent.invoke({
    "messages": [("human", "Subtract 100, 20, and 10.")]
})

# Get the final answer
final_answer_2 = response_2["messages"][-2].content
print(final_answer_2)
```

当智能体尝试从 100 中减去 20 和 10 时，发生了一些意想不到的事情。名为 `SubtractTool` 的工具的工作方式与智能体的预期不同。当你输入 "100, 20, 10" 时，它给出的不是你预期的 70，而是 -130。这是因为你的特殊计算器首先将 100 变成 -100，然后减去其他数字。

```The Confusion (困惑)``` 

智能体期望函数像普通数学一样工作 (100 - 20 - 10 = 70)。当智能体试图通过将问题分解为更小的步骤来解决这个问题时，它仍然得到意想不到的答案，因为计算器一直使用其特殊的规则。


```Getting Stuck (陷入困境)```

智能体不断尝试相同的方法，却没有意识到为什么不起作用。最终，它耗尽了时间而没有解决问题。

在你解决这个问题之前，让我们测试一下其他工具。



```python
print("\n--- Testing MultiplyTool ---")
response = math_agent.invoke({
    "messages": [("human", "Multiply 2, 3, and four.")]
})
print("Agent Response:", response["messages"][-1].content)

print("\n--- Testing DivideTool ---")
response = math_agent.invoke({
    "messages": [("human", "Divide 100 by 5 and then by 2.")]
})
print("Agent Response:", response["messages"][-1].content)
```

现在让我们更改 `SubtractTool`，使其直接减去数字（而不否定第一个数字）。这使工具的行为与标准算术和智能体的预期保持一致。



```python
@tool
def new_subtract_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and performs subtraction sequentially, starting with the first number.
    
    This function is designed to handle input in string format, where numbers may be separated by spaces, 
    commas, or other delimiters. It parses the input string, extracts numeric values, and calculates 
    the result by subtracting each subsequent number from the first. inputs[0]-inputs[1]-inputs[2]

    Parameters:
    - inputs (str): 
      A string containing numbers to subtract. The string can include spaces, commas, or other 
      delimiters between the numbers.

    Returns:
    - dict: 
      A dictionary containing the key "result" with the calculated difference as its value. 
      If no valid numbers are found in the input string, the result defaults to 0.

    Example Usage:
    - Input: "100, 20, 10"
    - Output: {"result": 70}

    Limitations:
    - The function does not handle cases where numbers are formatted with decimals or other non-integer representations.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]

    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Start with the first number
    result = numbers[0]

    # Subtract all subsequent numbers
    for num in numbers[1:]:
        result -= num

    return {"result": result}
```


## 注意：演示不同方法时的工具命名

在本实验中，有意展示了两种创建相同数学工具（加法）的不同方法：

1. 使用 `Tool()` 构造函数方法 (`add_tool`)
2. 使用 `@tool` 装饰器方法 (`add_numbers`)

这是为了比较不同的 LangChain 工具创建方法以用于教学目的。在生产应用程序中，通常会选择一种一致的方法，而不是为相同的功能拥有重复的工具。

在构建真正的智能体时，具有相似功能的重复工具会混淆 LLM，因为它不知道该选择哪一个。在生产代码中，始终使用具有明确区分目的的唯一工具。


接下来，创建一个新的智能体，确保它包含更新后的减法工具。



```python
tools_updated = [add_numbers, new_subtract_numbers, multiply_numbers, divide_numbers]
# Create the agent with all tools
math_agent_new = create_react_agent(
    model=llm,
    tools=tools_updated,
    # Optional: Add a system message to guide the agent's behavior
    prompt="You are a helpful mathematical assistant that can perform various operations. Use the tools precisely and explain your reasoning clearly."
)
print("agent",math_agent_new)
```

现在，你将创建一个 Python 字典来测试智能体的多个用例。测试智能体本身就很重要，因为它有助于确保它在不同情况下正常工作。自动化测试用例使这个过程更容易，并有助于在错误成为问题之前捕获它们。一个好的测试套件会检查智能体如何处理不同的输入，包括像除以零这样的棘手情况、处理大数字以及处理小数。你还可以测试智能体如何处理混合运算，例如结合加法和乘法。



```python
# Test Cases
test_cases = [
    {
        "query": "Subtract 100, 20, and 10.",
        "expected": {"result": 70},
        "description": "Testing subtraction tool with sequential subtraction."
    },
    {
        "query": "Multiply 2, 3, and 4.",
        "expected": {"result": 24},
        "description": "Testing multiplication tool for a list of numbers."
    },
    {
        "query": "Divide 100 by 5 and then by 2.",
        "expected": {"result": 10.0},
        "description": "Testing division tool with sequential division."
    },
    {
        "query": "Subtract 50 from 20.",
        "expected": {"result": -30},
        "description": "Testing subtraction tool with negative results."
    }

]
```

此代码从智能体的响应结构中提取实际的计算结果。与返回简单字典的直接工具调用不同，LangGraph 智能体返回一个包含作为消息列表的整个对话历史记录的复杂结构。要找到计算结果，你必须在此列表中找到特定的 `ToolMessage`（通过其名称与数学工具之一匹配来标识），然后解析其内容，其中包含作为 JSON 字符串的实际结果。这种方法是必要的，因为结果不能直接从响应对象访问，而是嵌套在消息历史记录中，需要你浏览消息以查找并提取相关数据以便与预期值进行比较。



```python
correct_tasks = []
# Corrected test execution
for index, test in enumerate(test_cases, start=1):
    query = test["query"]
    expected_result = test["expected"]["result"]  # Extract just the value
    
    print(f"\n--- Test Case {index}: {test['description']} ---")
    print(f"Query: {query}")
    
    # Properly format the input
    response = math_agent_new.invoke({"messages": [("human", query)]})
    
    # Find the tool message in the response
    tool_message = None
    for msg in response["messages"]:
        if hasattr(msg, 'name') and msg.name in ['add_numbers', 'new_subtract_numbers', 'multiply_numbers', 'divide_numbers']:
            tool_message = msg
            break
    
    if tool_message:
        # Parse the tool result from its content
        import json
        tool_result = json.loads(tool_message.content)["result"]
        print(f"Tool Result: {tool_result}")
        print(f"Expected Result: {expected_result}")
        
        if tool_result == expected_result:
            print(f"✅ Test Passed: {test['description']}")
            correct_tasks.append(test["description"])
        else:
            print(f"❌ Test Failed: {test['description']}")
    else:
        print("❌ No tool was called by the agent")

print("\nCorrectly passed tests:", correct_tasks)
```

当前的函数将受益于增强的错误处理和输入验证。`add_numbers`、`subtract_numbers`、`multiply_numbers` 和 `divide_numbers` 函数应更新为使用浮点转换处理十进制数字，更严格地验证输入，并为边缘情况提供清晰的错误消息。例如，`divide_numbers` 应显式检查除以零，并且所有函数都应优雅地处理非数字输入，如 "two" 或 "hundred"。测试用例应扩展到基本运算之外，包括边缘情况，如除以零、空输入和混合数字/文本输入（例如，“divide one hundred by 5”）。还要考虑添加对小数（例如，“multiply 3.5 by 2”）和连续运算（例如，“multiply 10 by 2 then add 5”）的测试。这种全面的测试方法可确保智能体能够处理各种现实世界的数学查询。


## **探索 LangChain 的内置工具**

虽然创建自定义工具很强大，但 LangChain 提供了一个丰富的**预构建工具**生态系统，可以开箱即用地解决常见任务。这些工具抽象了复杂的实现细节（API 调用、输入解析、错误处理），让你能够专注于快速构建健壮的智能体。


---

#### **为什么要使用内置工具？**
- **可靠性**：由 LangChain 社区测试和维护。
- **节省时间**：无需为常见任务重新发明轮子。
- **集成**：旨在与 LangChain 智能体无缝协作。

---


#### **常用的内置工具**
以下是一些来自 `langchain_community.tools` 的广泛使用的工具：

| 工具名称 | 描述 |
|---|---|
| `WikipediaQueryRun` | 搜索 Wikipedia 以获取事实信息。 |
| `GoogleSearchRun` | 使用 Google API 执行网络搜索。 |
| `PythonREPLTool` | 在安全环境中执行 Python 代码。 |
| `OpenWeatherMapQueryRun`| 获取实时天气数据。 |
| `YouTubeSearchTool` | 搜索 YouTube 视频。 |

---



#### **示例：使用 Wikipedia 工具**
让我们通过访问 Wikipedia 来增强数学智能体，以回答需要事实背景的问题。


现在，你将开始使用 `@tool` 操作符创建一个 Wikipedia 搜索工具。此工具将允许智能体在需要时从 Wikipedia 获取事实信息。



```python
from langchain_community.utilities import WikipediaAPIWrapper

# Create a Wikipedia tool using the @tool decorator
@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for factual information about a topic.
    
    Parameters:
    - query (str): The topic or question to search for on Wikipedia
    
    Returns:
    - str: A summary of relevant information from Wikipedia
    """
    wiki = WikipediaAPIWrapper()
    return wiki.run(query)
```


```python
search_wikipedia.invoke("What is tool calling?")
```

现在，你将**创建一个可用工具列表**（包括自定义数学工具和使用 Wikipedia 工具 `search_wikipedia`），然后**初始化一个智能体**，该智能体可以使用这些工具来解决问题。此智能体将结合：
- 自定义数学工具（`add_numbers`、`new_subtract_numbers` 等），用于算术运算。
- 内置工具（`wiki_tool`，例如，用于 Wikipedia 搜索），用于附加功能。

通过结合这些工具，智能体可以根据用户的请求处理**数学计算**（例如，加法、减法）和**信息查询**（例如，从 Wikipedia 获取事实）。



```python
# Update your tools list to include the Wikipedia tool
tools_updated = [add_numbers, new_subtract_numbers, multiply_numbers, divide_numbers, search_wikipedia]

# Create the agent with all tools including Wikipedia
math_agent_updated = create_react_agent(
    model=llm,
    tools=tools_updated,
    prompt="You are a helpful assistant that can perform various mathematical operations and look up information. Use the tools precisely and explain your reasoning clearly."
)
```

现在，你将**问智能体一个多步骤问题**，这需要：
1. **在线搜索**（使用 `search_wikipedia` 或其他内置工具）以获取现实世界的数据。
2. **数学计算**（使用 `multiply_numbers`）来处理检索到的数据。





```python
query = "What is the population of Canada? Multiply it by 0.75"

response = math_agent_updated.invoke({"messages": [("human", query)]})

print("\nMessage sequence:")
for i, msg in enumerate(response["messages"]):
    print(f"\n--- Message {i+1} ---")
    print(f"Type: {type(msg).__name__}")
    if hasattr(msg, 'content'):
        print(f"Content: {msg.content}")
    if hasattr(msg, 'name'):
        print(f"Name: {msg.name}")
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        print(f"Tool calls: {msg.tool_calls}")
```

**它是如何工作的**：
1. 智能体首先使用 `search_wikipedia` 查找加拿大的人口。
2. 从 Wikipedia 的响应中提取数值。
3. 使用 `multiply_numbers` 计算人口的 75%。
4. 返回带有上下文的最终结果。


有关可用工具的完整列表，请参阅 [LangChain 工具文档](https://python.langchain.com/docs/integrations/tools/)。


## **练习：创建一个计算指数的乘方工具**

#### **目标**
在本练习中，你将创建一个自定义工具来计算数字的乘方（例如，\( x^y \)）。然后，你将把这个工具集成到一个智能体中并测试其功能。

---

#### **步骤 1：创建乘方工具**

1. **定义工具函数**：
   - 创建一个名为 `calculate_power` 的 Python 函数，该函数将字符串作为输入。该字符串将包含两个数字：底数（\( x \)）和指数（\( y \)）。
   - 该函数应提取数字，计算 \( x^y \)，并将结果作为带有键 `"result"` 的字典返回。



```python
#TODO

```

<details>
    <summary>点击此处查看解决方案</summary>

```python
def calculate_power(input_text: str) -> dict:
    """
    Calculates the power of a number (x^y).

    Parameters:
    - input_text (str): A string like "2, 3", "2 3", "5^2", or "2 to the power of 3".

    Returns:
    - dict: {"result": <calculated value>} or an error message.
    """
    # Try to extract expressions like "5^2"
    match = re.search(r"(\d+(?:\.\d+)?)\s*\^+\s*(\d+(?:\.\d+)?)", input_text)
    if match:
        base = float(match.group(1))
        exponent = float(match.group(2))
        return {"result": base ** exponent}

    # Try to extract expressions like "2 to the power of 3"
    match = re.search(r"(\d+(?:\.\d+)?)\s*(?:to\s+the\s+power\s+of)\s*(\d+(?:\.\d+)?)", input_text, re.IGNORECASE)
    if match:
        base = float(match.group(1))
        exponent = float(match.group(2))
        return {"result": base ** exponent}

    # Fallback: assume two numbers separated by space or comma
    try:
        numbers = [float(num) for num in input_text.replace(",", " ").split()]
        if len(numbers) != 2:
            return {"result": "Invalid input. Please provide exactly two numbers."}
        base, exponent = numbers
        return {"result": base ** exponent}
    except ValueError:
        return {"result": "Invalid input format. Provide input like '2 3', '2^3', or '2 to the power of 3'."}


```

</details>


2. **创建工具对象**：
   - 使用 LangChain 中的 `Tool` 类为 `calculate_power` 函数创建一个工具对象。
   - 为工具提供名称、描述和函数。



```python
#TODO

```

<details>
    <summary>点击此处查看解决方案</summary>

```python
power_tool = Tool(
   name="PowerTool",
   func=calculate_power,
   description="Calculates the power of a number (x^y). Input should be two numbers: base and exponent."
)
```

</details>


#### **步骤 2：使用乘方工具创建智能体**

1. **设置智能体**：
   - 使用 LangChain 中的 `initialize_agent` 函数创建一个智能体。
   - 将 `power_tool` 包含在提供给智能体的工具列表中。
   - 指定智能体类型（例如，`zero-shot-react-description`）。



```python
#TODO

```

<details>
    <summary>点击此处查看解决方案</summary>

```python
# List of tools for the agent
tools = [power_tool]

# Create the agent
agent = initialize_agent(
   tools,
   llm,
   agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
   verbose=True,
    handle_parsing_errors=True
)
```

</details>


#### **步骤 3：测试智能体**

1. **使用 `run` 函数测试智能体**：
   - 使用智能体的 `run` 函数测试其计算乘方的能力。
   - 向智能体传递自然语言查询并观察其响应。



```python
#TODO

```

<details>
    <summary>点击此处查看解决方案</summary>

```python
agent.run("Calculate 5 to the power of 2.")
```

</details>


## 作者


[Joseph Santarcangelo](https://author.skills.network/instructors/joseph_santarcangelo)


[Kunal Makwana](https://author.skills.network/instructors/kunal_makwana)


Copyright © IBM Corporation. All rights reserved.
