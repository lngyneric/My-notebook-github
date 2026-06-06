---
source: raw/04_文档与参考/Markdown文档/JSON Canvas.md
raw_sha256: 27b0feca9709caa4bc5115fdb368fcd81388f0e8240aaf9860e30cfdbe676556
compiled_at: 2026-04-24T06:02:48.703Z
---
<wiki>
# JSON Canvas

## Summary
This documentation describes the JSON Canvas format, which enables tools like Claude Code to create and edit valid `.canvas` files used in Obsidian and other applications. JSON Canvas is an open file format for infinite canvas data, using the `.canvas` file extension and valid JSON structured per the [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/). It enables visual organization of text, files, links, and grouped content. This page covers its schema, element types, formatting rules, usage examples, and validation requirements.

## File Structure
A valid JSON Canvas file contains two top-level optional arrays:
```json
{
  "nodes": [],
  "edges": []
}
```
- `nodes`: Array of node objects representing elements placed on the canvas
- `edges`: Array of edge objects representing connections between nodes

## Nodes
Nodes are discrete objects placed on the infinite canvas. There are four supported node types: `text`, `file`, `link`, and `group`.

### Z-Index Ordering
Nodes are rendered in z-index order based on their position in the `nodes` array:
- The first entry in the array is the bottom layer (displayed below all other nodes)
- The last entry in the array is the top layer (displayed above all other nodes)

### Generic Node Attributes
All node types share the following required and optional attributes:
| Attribute | Required | Type | Description |
|-----------|----------|------|-------------|
| `id` | Yes | string | Unique identifier for the node |
| `type` | Yes | string | Node type: `text`, `file`, `link`, or `group` |
| `x` | Yes | integer | X position in pixels, measured from the top-left corner of the node |
| `y` | Yes | integer | Y position in pixels, measured from the top-left corner of the node |
| `width` | Yes | integer | Width of the node in pixels |
| `height` | Yes | integer | Height of the node in pixels |
| `color` | No | canvasColor | Node color (see [Colors](#colors) section) |

### Text Nodes
Text nodes store Markdown-formatted plain text content.
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
| Attribute | Required | Type | Description |
|-----------|----------|------|-------------|
| `text` | Yes | string | Plain text with supported Markdown syntax |

### File Nodes
File nodes reference local files or attachments (images, videos, PDFs, notes, etc.).
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
| Attribute | Required | Type | Description |
|-----------|----------|------|-------------|
| `file` | Yes | string | Relative path to the target file within the system |
| `subpath` | No | string | Link to a specific heading or block within the target file, prefixed with `#` |

### Link Nodes
Link nodes embed and link to external URLs.
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
| Attribute | Required | Type | Description |
|-----------|----------|------|-------------|
| `url` | Yes | string | External web URL |

### Group Nodes
Group nodes are visual containers for organizing other nodes on the canvas.
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
| Attribute | Required | Type | Description |
|-----------|----------|------|-------------|
| `label` | No | string | Text label displayed for the group |
| `background` | No | string | Relative path to a background image for the group |
| `backgroundStyle` | No | string | Rendering style for the group's background image |

#### Background Styles
| Value | Description |
|-------|-------------|
| `cover` | Fills the entire width and height of the node |
| `ratio` | Maintains the original aspect ratio of the background image |
| `repeat` | Repeats the image as a tile pattern in both directions |

## Edges
Edges are line objects that connect two nodes on the canvas.
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
| Attribute | Required | Type | Default | Description |
|-----------|----------|------|---------|-------------|
| `id` | Yes | string | - | Unique identifier for the edge |
| `fromNode` | Yes | string | - | ID of the node where the connection starts |
| `fromSide` | No | string | - | Side of the source node where the edge attaches |
| `fromEnd` | No | string | `none` | Shape of the edge's start endpoint |
| `toNode` | Yes | string | - | ID of the node where the connection ends |
| `toSide` | No | string | - | Side of the target node where the edge attaches |
| `toEnd` | No | string | `arrow` | Shape of the edge's end endpoint |
| `color` | No | canvasColor | - | Color of the edge line |
| `label` | No | string | - | Text label displayed along the edge |

### Side Values
Valid values for `fromSide` and `toSide` attributes:
| Value | Description |
|-------|-------------|
| `top` | Attaches to the top edge of the node |
| `right` | Attaches to the right edge of the node |
| `bottom` | Attaches to the bottom edge of the node |
| `left` | Attaches to the left edge of the node |

### End Shapes
Valid values for `fromEnd` and `toEnd` attributes:
| Value | Description |
|-------|-------------|
| `none` | No endpoint shape is displayed |
