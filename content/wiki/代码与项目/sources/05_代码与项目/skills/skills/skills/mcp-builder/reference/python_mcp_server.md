---
source: raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/python_mcp_server.md
raw_sha256: 2da52f77e675191014ca2e146a4b95aa04d0ca7dd7e2b100322df15ade685e80
compiled_at: 2026-04-14T05:19:10.449Z
---
# Python MCP 服务器实现指南
> 来源路径：`raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/python_mcp_server.md`

---

## TL;DR
本指南是基于官方 MCP Python SDK 的 Python MCP 服务器实现规范，提供从服务器初始化、工具注册、输入验证到错误处理的完整最佳实践，推荐使用 `FastMCP` 框架 + Pydantic v2 快速构建符合规范的 MCP 服务器。

---

## 1 基础快速参考
### 要点
- 核心依赖：官方 MCP Python SDK 提供的 `FastMCP` 框架，配合 Pydantic v2 做输入验证
- 必须遵循统一的命名规范：服务器名为 `{服务名}_mcp`（小写下划线格式），工具名使用带服务上下文的蛇形命名避免冲突
- 推荐使用装饰器 `@mcp.tool` 完成工具注册

### 关键代码片段
#### 核心导入
```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Dict, Any
from enum import Enum
import httpx
```

#### 服务器初始化
```python
mcp = FastMCP("service_mcp")
```

#### 工具注册模板
```python
@mcp.tool(name="tool_name", annotations={...})
async def tool_function(params: InputModel) -> str:
    # Implementation
    pass
```

#### 命名规范示例
| 正确示例 | 错误示例 |
|---------|---------|
| `slack_send_message` | `sendMessage` / `send_message`（缺少服务上下文） |
| `github_create_issue` | `createIssue` / `create_issue`（缺少服务上下文） |

---

## 2 工具实现规范
### 要点
- 使用 Pydantic v2 模型做输入验证，禁止额外字段、自动去除字符串空格、赋值时自动校验
- 工具必须包含完整文档字符串，明确输入输出格式、使用场景和错误处理规则
- 支持 Markdown 和 JSON 两种响应格式，适配人工阅读和程序处理场景
- 列表类工具必须实现标准分页逻辑
- 所有网络 I/O 必须使用异步实现，禁止阻塞式同步请求

### Pydantic v2 关键变更
> [!WARNING]
> 冲突：与 Pydantic v1 存在不兼容变更，需使用以下新语法
- 用 `model_config` 替代嵌套 `Config` 类
- 用 `field_validator` 替代废弃的 `validator`
- 用 `model_dump()` 替代废弃的 `dict()` 方法
- 验证器必须添加 `@classmethod` 装饰器

### 完整工具结构示例
```python
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

# 初始化服务器
mcp = FastMCP("example_mcp")

# 输入验证模型
class ServiceToolInput(BaseModel):
    '''Input model for service tool operation.'''
    model_config = ConfigDict(
        str_strip_whitespace=True,  # 自动去除字符串空格
        validate_assignment=True,    # 赋值时自动校验
        extra='forbid'              # 禁止额外输入字段
    )

    param1: str = Field(..., description="First parameter description (e.g., 'user123', 'project-abc')", min_length=1, max_length=100)
    param2: Optional[int] = Field(default=None, description="Optional integer parameter with constraints", ge=0, le=1000)
    tags: Optional[List[str]] = Field(default_factory=list, description="List of tags to apply", max_items=10)

@mcp.tool(
    name="service_tool_name",
    annotations={
        "title": "Human-Readable Tool Title",
        "readOnlyHint": True,     # 工具不修改环境
        "destructiveHint": False,  # 工具不执行破坏性操作
        "idempotentHint": True,    # 重复调用无额外副作用
        "openWorldHint": False     # 工具不与外部实体交互
    }
)
async def service_tool_name(params: ServiceToolInput) -> str:
    '''Tool description automatically becomes the 'description' field.

    This tool performs a specific operation on the service. It validates all inputs
    using the ServiceToolInput Pydantic model before processing.

    Args:
        params (ServiceToolInput): Validated input parameters containing:
            - param1 (str): First parameter description
            - param2 (Optional[int]): Optional parameter with default
            - tags (Optional[List[str]]): List of tags

    Returns:
        str: JSON-formatted response containing operation results
    '''
    # 业务逻辑实现
    pass
```

### 响应格式实现
```python
from enum import Enum

class ResponseFormat(str, Enum):
    '''Output format for tool responses.'''
    MARKDOWN = "markdown"
    JSON = "json"

class UserSearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' for human-readable or 'json' for machine-readable"
    )
```

### 分页实现模板
```python
class ListInput(BaseModel):
    limit: Optional[int] = Field(default=20, description="Maximum results to return", ge=1, le=100)
    offset: Optional[int] = Field(default=0, description="Number of results to skip for pagination", ge=0)

async def list_items(params: ListInput) -> str:
    # 带分页参数的API请求
    data = await api_request(limit=params.limit, offset=params.offset)

    # 返回标准分页信息
    response = {
        "total": data["total"],
        "count": len(data["items"]),
        "offset": params.offset,
        "items": data["items"],
        "has_more": data["total"] > params.offset + len(data["items"]),
        "next_offset": params.offset + len(data["items"]) if data["total"] > params.offset + len(data["items"]) else None
    }
    return json.dumps(response, indent=2)
```

---

## 3 错误处理与公用工具
### 要点
- 统一错误处理格式，提供清晰可操作的错误信息
- 提取通用逻辑（API请求、格式化等）到可复用工具函数，避免代码重复

### 统一错误处理示例
```python
def _handle_api_error(e: Exception) -> str:
    '''Consistent error formatting across all tools.'''
    if isinstance(e, httpx.HTTPStatusError):
        if e.response.status_code == 404:
            return "Error: Resource not found. Please check the ID is correct."
        elif e.response.status_code == 403:
            return "Error: Permission denied. You don't have access to this resource."
        elif e.response.status_code == 429:
            return "Error: Rate limit exceeded. Please wait before making more requests."
        return f"Error: API request failed with status {e.response.status_code}"
    elif isinstance(e, httpx.TimeoutException):
        return "Error: Request timed out. Please try again."
    return f"Error: Unexpected error occurred: {type(e).__name__}"
```

### 通用API请求工具示例
```python
# 所有工具共享的API请求函数
async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
    '''Reusable function for all API calls.'''
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method,
            f"{API_BASE_URL}/{endpoint}",
            timeout=30.0,
            **kwargs
        )
        response.raise_for_status()
        return response.json()
```

---

## 4 高级 FastMCP 功能
### 要点
| 功能 | 用途 |
|------|------|
| 上下文注入 | 提供日志、进度报告、用户交互能力 |
| 资源注册 | 用URI模板暴露静态/半静态数据，比工具更简洁 |
| 结构化返回类型 | 支持TypedDict、Pydantic模型，FastMCP自动处理序列化 |
| 生命周期管理 | 管理跨请求的持久化资源（如数据库连接） |
| 传输配置 | 本地工具用stdio，远程服务用Streamable HTTP |

### 上下文注入示例
```python
from mcp.server.fastmcp import FastMCP
