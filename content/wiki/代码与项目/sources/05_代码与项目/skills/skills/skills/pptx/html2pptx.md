---
source: raw/05_代码与项目/skills/skills/skills/pptx/html2pptx.md
raw_sha256: f08ed7580969b796d9cd5ade93e2cdee981dcaf13cc5eb12e8d4a3700c2d6047
compiled_at: 2026-04-14T05:08:17.980Z
---
# HTML to PowerPoint (html2pptx.js) 使用指南

> [!NOTE] 来源路径
> `raw/05_代码与项目/skills/skills/skills/pptx/html2pptx.md`

## TL;DR
`html2pptx.js` 是一个可以将排版好的 HTML 幻灯片转换为带精确元素定位的 PowerPoint 演示文稿的工具，基于 `PptxGenJS`、`playwright` 和 `sharp` 实现，你只需要按照规范编写 HTML 幻灯片，即可一键生成 PowerPoint，还可以预留占位符插入动态图表。

## 要点
1. HTML 幻灯片需要按照固定尺寸设置 body，支持常见文本、列表、图片、占位符元素，所有文本必须放在 `<p>`/`<h1>`-`<h6>`/`<ul>`/`<ol>` 标签内，不支持手动项目符号和自定义非安全字体
2. 所有渐变、图标需要提前用 Sharp 栅格化为 PNG 再引入 HTML，不能直接使用 CSS 渐变
3. `html2pptx` 会自动校验 HTML 规范，批量输出错误，返回生成好的幻灯片和占位符位置信息供后续添加动态内容
4. 使用 PptxGenJS 时所有十六进制颜色不能带 `#` 前缀，否则会导致文件损坏，不同类型图表有对应的数据格式要求

---

## 目录
1. [创建 HTML 幻灯片](#创建-html-幻灯片)
2. [使用 html2pptx 库](#使用-html2pptx-库)
3. [使用 PptxGenJS 添加内容](#使用-pptxgenjs-添加内容)

---

## 创建 HTML 幻灯片

### 布局尺寸
每个 HTML 幻灯片的 body 需要设置对应比例的固定尺寸：
| 比例 | 尺寸 | 默认 |
|------|------|------|
| 16:9 | `width: 720pt; height: 405pt` | ✅ 默认 |
| 4:3 | `width: 720pt; height: 540pt` | |
| 16:10 | `width: 720pt; height: 450pt` | |

### 支持的元素
| 元素 | 说明 |
|------|------|
| `<p>`, `<h1>`-`<h6>` | 带样式的文本容器 |
| `<ul>`, `<ol>` | 列表，**禁止使用手动项目符号 •/\-/\*** |
| `<b>`, `<strong>` | 行内加粗 |
| `<i>`, `<em>` | 行内斜体 |
| `<u>` | 行内下划线 |
| `<span>` | 带 CSS 样式的行内格式化（支持加粗、斜体、下划线、颜色） |
| `<br>` | 换行 |
| 带背景/边框的 `<div>` | 转换为 PowerPoint 形状 |
| `<img>` | 图片 |
| `class="placeholder"` | 图表预留占位，会返回占位块位置信息 `{ id, x, y, w, h }` |

### 文本强制规则
> [!WARNING]
> 所有文本必须放在 `<p>`, `<h1>`-`<h6>`, `<ul>`, 或 `<ol>` 标签内：
> - ✅ 正确：`<div><p>Text here</p></div>`
> - ❌ 错误：`<div>Text here</div>` - **文本不会出现在 PowerPoint 中**
> - ❌ 错误：`<span>Text</span>` - **文本不会出现在 PowerPoint 中**
> - 放在未嵌套文本标签的 `<div>` 或 `<span>` 内的文本会被静默忽略

另外两条强制规则：
1. 禁止使用手动项目符号（•, -, *, 等），必须使用 `<ul>` 或 `<ol>` 列表
2. 只能使用通用网页安全字体，非安全字体会导致渲染问题：
   - ✅ 允许：`Arial`, `Helvetica`, `Times New Roman`, `Georgia`, `Courier New`, `Verdana`, `Tahoma`, `Trebuchet MS`, `Impact`, `Comic Sans MS`
   - ❌ 禁止：`'Segoe UI'`, `'SF Pro'`, `'Roboto'` 以及任何自定义字体

### 样式规范
- body 添加 `display: flex` 防止外边距折叠破坏溢出校验
- 使用 `margin` 控制间距（padding 会计入元素尺寸）
- 行内格式化可以使用 `<b>`, `<i>`, `<u>` 标签，或带 CSS 的 `<span>`：
  - `<span>` 支持：`font-weight: bold`, `font-style: italic`, `text-decoration: underline`, `color: #rrggbb`
  - `<span>` 不支持：`margin`, `padding`（PowerPoint 文本 run 不支持该属性）
  - 示例：`<span style="font-weight: bold; color: #667eea;">Bold blue text</span>`
- 支持 Flexbox，会从渲染后的布局计算元素位置
- CSS 中颜色需要使用带 `#` 前缀的十六进制格式
- 文本对齐：使用 CSS `text-align` 作为 PptxGenJS 的格式提示，避免文本长度偏差导致的对齐问题

### DIV 形状样式规范
> [!IMPORTANT]
> 背景、边框、阴影仅支持放在 `<div>` 元素上，不允许放在文本元素（`<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>`）上：
- **背景**：仅 `<div>` 支持 CSS `background` 或 `background-color`，示例：`<div style="background: #f0f0f0;">` 会创建带背景的形状
- **边框**：`<div>` 的 CSS `border` 会转换为 PowerPoint 形状边框：
  - 支持全边框：`border: 2px solid #333333`
  - 支持单边框：`border-left`, `border-right`, `border-top`, `border-bottom`（会渲染为线形）
  - 示例：`<div style="border-left: 8pt solid #E76F51;">`
- **圆角**：`<div>` 的 CSS `border-radius` 支持设置圆角：
  - `border-radius: 50%` 或更高会生成圆形
  - 小于 50% 的百分比会相对于形状的较小边计算
  - 支持 px 和 pt 单位，例如 `border-radius: 8pt;`, `border-radius: 12px;`
  - 示例：100x200px 的矩形设置 `border-radius: 25%;` = 100px * 25% = 25px 半径
- **阴影**：`<div>` 的 CSS `box-shadow` 会转换为 PowerPoint 阴影：
  - 仅支持外阴影，内阴影会被忽略以避免文件损坏
  - 示例：`<div style="box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);">`
  - 说明：PowerPoint 本身不支持内阴影，会直接跳过

### 图标与渐变规范
> [!WARNING]
> 禁止使用 CSS 渐变（`linear-gradient`, `radial-gradient`），无法转换为 PowerPoint：
> - 所有渐变、图标必须先用 Sharp 栅格化为 PNG，再在 HTML 中引用
> - 渐变：将 SVG 渐变栅格化为 PNG 背景
> - 图标：将 react-icons 这类 SVG 图标栅格化为 PNG 图片
> - 所有视觉效果必须在 HTML 渲染前预渲染为栅格图

#### 使用 Sharp 栅格化图标：
```javascript
const React = require('react');
const ReactDOMServer = require('react-dom/server');
const sharp = require('sharp');
const { FaHome } = require('react-icons/fa');

async function rasterizeIconPng(IconComponent, color, size = "256", filename) {
  const svgString = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color: `#${color}`, size: size })
  );

  // Convert SVG to PNG using Sharp
  await sharp(Buffer.from(svgString))
    .png()
    .toFile(filename);

  return filename;
}

// Usage: Rasterize icon before using in HTML
const iconPath = await rasterizeIconPng(FaHome, "4472c4", "256", "home-icon.png");
// Then reference in HTML: <img src="home-icon.png" style="width: 40pt; height: 40pt;">
```

#### 使用 Sharp 生成渐变背景：
