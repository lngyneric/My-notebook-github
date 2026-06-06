---
source: raw/04_文档与参考/Markdown文档/SKILL.md
raw_sha256: 0af2f12742148c3775f13fe4d11862949d2ce765738f77297a18fdf1ccbe28b7
compiled_at: 2026-04-14T03:53:11.312Z
---
# Obsidian Flavored Markdown 语法参考

> [!INFO] 基础信息
> 这是 Obsidian 专属 Markdown 语法的完整参考文档，用于在 Obsidian 笔记软件中编写和编辑 Markdown 文件，支持 wikilinks、嵌入、标注、属性等 Obsidian 特有扩展语法。

---

## TL;DR
Obsidian Flavored Markdown (OFM) 是 Obsidian 笔记软件基于 CommonMark、GitHub Flavored Markdown 和 LaTeX 扩展的专属 Markdown 语法，新增了内部 wikilink、内容嵌入、标注、前置属性、块链接、mermaid 图表等笔记场景专用语法，适合知识库、个人笔记场景使用。

## 要点
- 语法基础：兼容 CommonMark、GFM、LaTeX 数学公式，新增 Obsidian 专属扩展
- 核心扩展：支持 wikilink 格式的内部链接，可链接到整个笔记、标题、任意文本块
- 内容嵌入：支持嵌入其他笔记的部分/全部内容、图片、音视频、PDF 等资源
- 结构化支持：支持 callout 标注、前置属性（Frontmatter）、标签体系，方便笔记组织
- 扩展能力：原生支持 Mermaid 图表、脚注、注释、HTML 嵌入等功能

---

## 引用原始资料
来源路径：`raw/04_文档与参考/Markdown文档/SKILL.md`

## 语法说明

### 基础格式
原始参考内容如下：
````markdown
---
name: obsidian-markdown
description: Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when the user mentions wikilinks, callouts, frontmatter, tags, embeds, or Obsidian notes.
---

# Obsidian Flavored Markdown Skill

This skill enables Claude Code to create and edit valid Obsidian Flavored Markdown, including all Obsidian-specific syntax extensions.

## Overview

Obsidian uses a combination of Markdown flavors:
- [CommonMark](https://commonmark.org/)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)
- [LaTeX](https://www.latex-project.org/) for math
- Obsidian-specific extensions (wikilinks, callouts, embeds, etc.)

## Basic Formatting

### Paragraphs and Line Breaks

```markdown
This is a paragraph.

This is another paragraph (blank line between creates separate paragraphs).

For a line break within a paragraph, add two spaces at the end  
or use Shift+Enter.
```

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

### Text Formatting

| Style | Syntax | Example | Output |
|-------|--------|---------|--------|
| Bold | `**text**` or `__text__` | `**Bold**` | **Bold** |
| Italic | `*text*` or `_text_` | `*Italic*` | *Italic* |
| Bold + Italic | `***text***` | `***Both***` | ***Both*** |
| Strikethrough | `~~text~~` | `~~Striked~~` | ~~Striked~~ |
| Highlight | `==text==` | `==Highlighted==` | ==Highlighted== |
| Inline code | `` `code` `` | `` `code` `` | `code` |

### Escaping Formatting

Use backslash to escape special characters:
```markdown
\*This won't be italic\*
\#This won't be a heading
1\. This won't be a list item
```

Common characters to escape: `\*`, `\_`, `\#`, `` \` ``, `\|`, `\~`
````

### 内部链接（Wikilinks）
原始参考内容如下：
```markdown
## Internal Links (Wikilinks)

### Basic Links

```markdown
[[Note Name]]
[[Note Name.md]]
[[Note Name|Display Text]]
```

### Link to Headings

```markdown
[[Note Name#Heading]]
[[Note Name#Heading|Custom Text]]
[[#Heading in same note]]
[[##Search all headings in vault]]
```

### Link to Blocks

```markdown
[[Note Name#^block-id]]
[[Note Name#^block-id|Custom Text]]
```

Define a block ID by adding `^block-id` at the end of a paragraph:
```markdown
This is a paragraph that can be linked to. ^my-block-id
```

For lists and quotes, add the block ID on a separate line:
```markdown
> This is a quote
> With multiple lines

^quote-id
```

### Search Links

```markdown
[[##heading]]     Search for headings containing "heading"
[[^^block]]       Search for blocks containing "block"
```
```

### Markdown 风格链接
原始参考内容如下：
```markdown
## Markdown-Style Links

```markdown
[Display Text](Note%20Name.md)
[Display Text](Note%20Name.md#Heading)
[Display Text](https://example.com)
[Note](obsidian://open?vault=VaultName&file=Note.md)
```

Note: Spaces must be URL-encoded as `%20` in Markdown links.
```

### 内容嵌入
原始参考内容如下：
````markdown
## Embeds

### Embed Notes

```markdown
![[Note Name]]
![[Note Name#Heading]]
![[Note Name#^block-id]]
```

### Embed Images

```markdown
![[image.png]]
![[image.png|640x480]]    Width x Height
![[image.png|300]]        Width only (maintains aspect ratio)
```

### External Images

```markdown
![Alt text](https://example.com/image.png)
![Alt text|300](https://example.com/image.png)
```

### Embed Audio

```markdown
![[audio.mp3]]
![[audio.ogg]]
```

### Embed PDF

```markdown
![[document.pdf]]
![[document.pdf#page=3]]
![[document.pdf#height=400]]
```

### Embed Lists

```markdown
![[Note#^list-id]]
```

Where the list has been defined with a block ID:
```markdown
- Item 1
- Item 2
- Item 3

^list-id
```

### Embed Search Results

````markdown
```query
tag:#project status:done
```
````
````

### Callout 标注
原始参考内容如下：
````markdown
## Callouts

### Basic Callout

```markdown
> [!note]
> This is a note callout.

> [!info] Custom Title
> This callout has a custom title.

> [!tip] Title Only
```

### Foldable Callouts

```markdown
> [!faq]- Collapsed by default
> This content is hidden until expanded.

> [!faq]+ Expanded by default
> This content is visible but can be collapsed.
```

### Nested Callouts

```markdown
> [!question] Outer callout
> > [!note] Inner callout
> > Nested content
```

### Supported Callout Types

| Type | Aliases | Description |
|------|---------|-------------|
| `note` | - | Blue, pencil icon |
| `abstract` | `summary`, `tldr` | Teal, clipboard icon |
| `info` | - | Blue, info icon |
| `todo` | - | Blue, checkbox icon |
| `tip` | `hint`, `important` | Cyan, flame icon |
| `success` | `check`, `done` | Green, checkmark icon |
| `question` | `help`, `faq` | Yellow, question mark |
| `warning` | `caution`, `attention` | Orange, warning icon |
| `failure` | `fail`, `missing` | Red, X icon |
| `danger` | `error` | Red, zap icon |
| `bug` | - | Red, bug icon |
| `example` | - | Purple, list icon |
| `quote` | `cite` | Gray, quote icon |

### Custom Callouts (CSS)

```css
.callout[data-callout="custom-type"] {
  --callout-color: 255, 0, 0;
  --callout-icon: lucide-alert-circle;
}
```
````

### 列表、引用与代码块
原始参考内容如下：
````markdown
## Lists

### Unordered Lists

```markdown
- Item 1
- Item 2
  - Nested
