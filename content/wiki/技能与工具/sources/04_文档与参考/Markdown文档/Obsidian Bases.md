---
source: raw/04_文档与参考/Markdown文档/Obsidian Bases.md
raw_sha256: 2684057042608c15d54f35c8cec1cf430140b19d9cc22790c44a39afa694c4c8
compiled_at: 2026-04-14T03:51:47.127Z
---
---
title: Obsidian Bases
tags: [Obsidian, Guide, Bases]
date: 2026-01-08
source: raw/04_文档与参考/Markdown文档/Obsidian Bases.md
---

# Obsidian Bases

> [!TL;DR]
> Obsidian Bases 是 Obsidian 中基于 YAML 格式定义的动态数据视图功能，支持 `.base` 文件和嵌入 Markdown 的写法，可以通过过滤器、公式、多种视图类型对库内笔记进行筛选、计算和展示，支持表格、卡片、列表、地图多种展示形式。

## 要点
- Obsidian Bases 是基于 YAML 格式定义，用于对 Obsidian 库内笔记生成动态视图的功能，文件扩展名为 `.base`，也支持嵌入 Markdown 代码块。
- 一个 Base 文件可包含：全局过滤器、全局公式、属性显示配置、自定义汇总、多个不同类型的视图。
- 过滤器支持嵌套逻辑（与/或/非），可以对笔记属性、文件元数据进行条件筛选。
- 属性分为三类：笔记前置元属性、文件内置属性、公式计算属性。
- 支持公式表达式，内置大量日期、字符串、数值、列表、文件等相关函数，可实现自定义计算。
- 支持四种视图类型：表格、卡片、列表、地图（地图需 Obsidian Maps 插件），支持分组、分页限制、列排序和属性汇总。
- 支持嵌入到其他 Markdown 文件中，可以指定展示特定视图。

## 完整定义与语法

### 概述
`Obsidian Bases` 能力使 Claude Code 可以创建和编辑合法的 Obsidian Bases（`.base` 文件），包含视图、过滤器、公式和所有相关配置。

Obsidian Bases 是基于 YAML 的文件，用于定义 Obsidian 库中笔记的动态视图。一个 Base 文件可包含多个视图、全局过滤器、公式、属性配置和自定义汇总。

### 文件格式
Base 文件使用 `.base` 扩展名，内容为合法 YAML，也可以嵌入在 Markdown 代码块中。

### 完整 Schema
```yaml
# Global filters apply to ALL views in the base
filters:
  # Can be a single filter string
  # OR a recursive filter object with and/or/not
  and: []
  or: []
  not: []

# Define formula properties that can be used across all views
formulas:
  formula_name: 'expression'

# Configure display names and settings for properties
properties:
  property_name:
    displayName: "Display Name"
  formula.formula_name:
    displayName: "Formula Display Name"
  file.ext:
    displayName: "Extension"

# Define custom summary formulas
summaries:
  custom_summary_name: 'values.mean().round(3)'

# Define one or more views
views:
  - type: table | cards | list | map
    name: "View Name"
    limit: 10                    # Optional: limit results
    groupBy:                     # Optional: group results
      property: property_name
      direction: ASC | DESC
    filters:                     # View-specific filters
      and: []
    order:                       # Properties to display in order
      - file.name
      - property_name
      - formula.formula_name
    summaries:                   # Map properties to summary formulas
      property_name: Average
```

## 过滤器语法
过滤器用于筛选结果，可以全局应用，也可以按视图单独应用。

### 过滤器结构
```yaml
# Single filter
filters: 'status == "done"'

# AND - all conditions must be true
filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

# OR - any condition can be true
filters:
  or:
    - 'file.hasTag("book")'
    - 'file.hasTag("article")'

# NOT - exclude matching items
filters:
  not:
    - 'file.hasTag("archived")'

# Nested filters
filters:
  or:
    - file.hasTag("tag")
    - and:
        - file.hasTag("book")
        - file.hasLink("Textbook")
    - not:
        - file.hasTag("book")
        - file.inFolder("Required Reading")
```

### 过滤器运算符
| Operator | Description |
|----------|-------------|
| `==` | equals |
| `!=` | not equal |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |
| `&&` | logical and |
| `||` | logical or |
| `!` | logical not |

## 属性
### 属性的三种类型
1. **笔记属性** - 来自前置元数据：`note.author` 或简写 `author`
2. **文件属性** - 文件元数据：`file.name`、`file.mtime` 等
3. **公式属性** - 计算值：`formula.my_formula`

### 文件属性参考
| Property | Type | Description |
|----------|------|-------------|
| `file.name` | String | File name |
| `file.basename` | String | File name without extension |
| `file.path` | String | Full path to file |
| `file.folder` | String | Parent folder path |
| `file.ext` | String | File extension |
| `file.size` | Number | File size in bytes |
| `file.ctime` | Date | Created time |
| `file.mtime` | Date | Modified time |
| `file.tags` | List | All tags in file |
| `file.links` | List | Internal links in file |
| `file.backlinks` | List | Files linking to this file |
| `file.embeds` | List | Embeds in the note |
| `file.properties` | Object | All frontmatter properties |

### `this` 关键字
- 在主内容区：指代 Base 文件本身
- 嵌入场景：指代嵌入当前 Base 的文件
- 在侧边栏：指代主内容区的活跃文件

## 公式语法
公式通过属性计算值，在 `formulas` 段定义：
```yaml
formulas:
  # Simple arithmetic
  total: "price * quantity"
  
  # Conditional logic
  status_icon: 'if(done, "✅", "⏳")'
  
  # String formatting
  formatted_price: 'if(price, price.toFixed(2) + " dollars")'
  
  # Date formatting
  created: 'file.ctime.format("YYYY-MM-DD")'
  
  # Complex expressions
  days_old: '((now() - file.ctime) / 86400000).round(0)'
```

## 函数参考
### 全局函数
| Function | Signature | Description |
|----------|-----------|-------------|
| `date()` | `date(string): date` | Parse string to date. Format: `YYYY-MM-DD HH:mm:ss` |
| `duration()` | `duration(string): duration` | Parse duration string |
| `now()` | `now(): date` | Current date and time |
| `today()` | `today(): date` | Current date (time = 00:00:00) |
| `if()` | `if(condition, trueResult, falseResult?)` | Conditional |
| `min()` | `min(n1, n2, ...): number` | Smallest number |
| `max()` | `max(n1, n2, ...): number` | Largest number |
| `number()` | `number(any): number` | Convert to number |
| `link()` | `link(path, display?): Link` | Create a link |
| `list()` | `list(element): List` | Wrap in list if not already |
| `file()` | `file(path): file` | Get file object |
| `image()` | `image(path): image` | Create image for rendering |
| `icon()` | `icon(name): icon` | Lucide icon by name |
| `html()` | `html(string): html` | Render as HTML |
| `escapeHTML()` | `escapeHTML(string): string` | Escape HTML characters |

### 任意类型通用函数
| Function | Signature | Description |
|----------|-----------|-------------|
| `isTruthy()` | `any.isTruthy(): boolean` | Coerce to boolean |
| `isType()` | `any.isType(type): boolean` | Check type |
| `toString()` | `any.toString(): string` | Convert to string |

### 日期函数与字段
**可用字段：** `date.year`、`date.month`、`date.day`、`date.hour`、`date.minute`
