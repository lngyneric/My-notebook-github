---
source: raw/04_文档与参考/Markdown文档/JSON Canvas.md
raw_sha256: 27b0feca9709caa4bc5115fdb368fcd81388f0e8240aaf9860e30cfdbe676556
compiled_at: 2026-04-14T03:51:29.298Z
---
> [!INFO] 来源路径
> raw/04_文档与参考/Markdown文档/JSON Canvas.md

# JSON Canvas

标签：`Obsidian` `Guide` `Canvas` `JSON`  
最后更新：2026-01-08

---

## TL;DR

JSON Canvas 是一种开放的无限画布数据格式，使用 `.canvas` 扩展名存储，内容为符合规范的 JSON，可用于 Obsidian 等应用存储画布内容，包含节点（不同内容类型）和边（节点连接）两种核心结构，语法规范清晰，可用于创建思维导图、项目看板、流程图等多种可视化内容。

## 要点

- JSON Canvas 是开放文件格式，遵循 [JSON Canvas Spec 1.0 官方规范](https://jsoncanvas.org/spec/1.0/)
- 核心结构为两个顶级可选数组：`nodes`（画布元素）和 `edges`（元素连接）
- 共支持 4 种节点类型：`text`（Markdown文本）、`file`（内部文件引用）、`link`（外部链接）、`group`（容器分组）
- 节点按数组顺序排序 z 轴：数组第一个节点是最底层，最后一个节点是最顶层
- 边用于连接两个节点，支持配置端点形状、连接侧边、颜色和标签
- 颜色支持六进制 hex 格式和 1-6 号预设，预设具体色值由应用自行定义
- 节点和边的 ID 需全局唯一，Obsidian 默认使用 16 位小写十六进制字符串作为 ID

## 详细规范

### 概述

> [!QUOTE] 原始引用
> This skill enables Claude Code to create and edit valid JSON Canvas files (`.canvas`) used in Obsidian and other applications.
>
> JSON Canvas is an open file format for infinite canvas data. Canvas files use the `.canvas` extension and contain valid JSON following the [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/).

JSON Canvas 最顶层结构示例：
```json
{
  "nodes": [],
  "edges": []
}
```

| 顶级字段 | 是否必须 | 说明 |
|---------|---------|------|
| `nodes` | 否 | 节点对象数组 |
| `edges` | 否 | 边对象数组 |

### 节点规范

节点是放置在画布上的对象，共有四种类型：
- `text`：带 Markdown 的文本内容
- `file`：文件/附件引用
- `link`：外部URL链接
- `group`：容纳其他节点的可视化容器

#### Z 轴排序规则

> [!QUOTE] 原始引用
> Nodes are ordered by z-index in the array:
> - First node = bottom layer (displayed below others)
> - Last node = top layer (displayed above others)

#### 通用节点属性

所有节点共享以下属性：

| 属性 | 是否必须 | 类型 | 说明 |
|-----|---------|------|------|
| `id` | 是 | string | 节点的唯一标识 |
| `type` | 是 | string | 节点类型：`text`/`file`/`link`/`group` |
| `x` | 是 | integer | X 坐标（像素） |
| `y` | 是 | integer | Y 坐标（像素） |
| `width` | 是 | integer | 宽度（像素） |
| `height` | 是 | integer | 高度（像素） |
| `color` | 否 | canvasColor | 节点颜色，参见「颜色规范」 |

#### 文本节点（text）

文本节点存储带 Markdown 语法的文本内容，示例：
```json
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 200,
  "text": "# Hello World\n\nThis is **Markdown** content."
}
```

| 特有属性 | 是否必须 | 类型 | 说明 |
|---------|---------|------|------|
| `text` | 是 | string | 带 Markdown 语法的纯文本内容 |

#### 文件节点（file）

文件节点引用内部文件/附件（图片、视频、PDF、笔记等），示例：
```json
{
  "id": "a1b2c3d4e5f67890",
  "type": "file",
  "x": 500,
  "y": 0,
  "width": 400,
  "height": 300,
  "file": "Attachments/diagram.png"
}
```
```json
{
  "id": "b2c3d4e5f6789012",
  "type": "file",
  "x": 500,
  "y": 400,
  "width": 400,
  "height": 300,
  "file": "Notes/Project Overview.md",
  "subpath": "#Implementation"
}
```

| 特有属性 | 是否必须 | 类型 | 说明 |
|---------|---------|------|------|
| `file` | 是 | string | 系统内的文件路径 |
| `subpath` | 否 | string | 锚点，指向标题或块，以 `#` 开头 |

#### 链接节点（link）

链接节点展示外部 URL，示例：
```json
{
  "id": "c3d4e5f678901234",
  "type": "link",
  "x": 1000,
  "y": 0,
  "width": 400,
  "height": 200,
  "url": "https://obsidian.md"
}
```

| 特有属性 | 是否必须 | 类型 | 说明 |
|---------|---------|------|------|
| `url` | 是 | string | 外部 URL |

#### 分组节点（group）

分组节点是用于组织其他节点的可视化容器，示例：
```json
{
  "id": "d4e5f6789012345a",
  "type": "group",
  "x": -50,
  "y": -50,
  "width": 1000,
  "height": 600,
  "label": "Project Overview",
  "color": "4"
}
```
```json
{
  "id": "e5f67890123456ab",
  "type": "group",
  "x": 0,
  "y": 700,
  "width": 800,
  "height": 500,
  "label": "Resources",
  "background": "Attachments/background.png",
  "backgroundStyle": "cover"
}
```

| 特有属性 | 是否必须 | 类型 | 说明 |
|---------|---------|------|------|
| `label` | 否 | string | 分组的文本标签 |
| `background` | 否 | string | 背景图片路径 |
| `backgroundStyle` | 否 | string | 背景渲染样式 |

##### 背景样式可选值

| 值 | 说明 |
|---|------|
| `cover` | 填满节点的整个宽高 |
| `ratio` | 保持背景图片的宽高比 |
| `repeat` | 两个方向重复平铺图片 |

### 边规范

边是连接节点的线条，示例：
```json
{
  "id": "f67890123456789a",
  "fromNode": "6f0ad84f44ce9c17",
  "toNode": "a1b2c3d4e5f67890"
}
```
```json
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "fromEnd": "none",
  "toNode": "b2c3d4e5f6789012",
  "toSide": "left",
  "toEnd": "arrow",
  "color": "1",
  "label": "leads to"
}
```
