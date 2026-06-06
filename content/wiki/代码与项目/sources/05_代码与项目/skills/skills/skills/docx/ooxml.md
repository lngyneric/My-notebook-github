---
source: raw/05_代码与项目/skills/skills/skills/docx/ooxml.md
raw_sha256: a16f922797eeaa3670ea31c1e49d15b799613d03f39445c857a5dd3221aa3597
compiled_at: 2026-04-14T05:04:53.335Z
---
# Office Open XML (OOXML) 技术参考
> 来源路径：`raw/05_代码与项目/skills/skills/skills/docx/ooxml.md`

---

## TL;DR
本文是处理 `*.docx` 文件 OOXML 格式的技术规范，涵盖了 XML 结构合规要求、常用文档元素（标题、列表、表格、链接、图片等）的标准 XML 模式，以及推荐使用的 Python 操作库，重点说明了修订追踪（Tracked Changes/Redlining）的实现规则与最佳实践，是所有 docx 程序化编辑的依据。

---

## 目录
- [1 技术合规规范](#1-技术合规规范)
- [2 文档内容标准 XML 模式](#2-文档内容标准-xml-模式)
- [3 需要更新的包内文件清单](#3-需要更新的包内文件清单)
- [4 Python 文档操作库](#4-python-文档操作库)
  - [4.1 初始化与环境配置](#41-初始化与环境配置)
  - [4.2 创建追踪修订](#42-创建追踪修订)
  - [4.3 添加批注](#43-添加批注)
  - [4.4 驳回追踪修订](#44-驳回追踪修订)
  - [4.5 插入图片](#45-插入图片)
  - [4.6 节点查询](#46-节点查询)
  - [4.7 保存文档](#47-保存文档)
  - [4.8 直接 DOM 操作](#48-直接-dom-操作)
- [5 追踪修订（Redlining）参考规则](#5-追踪修订redlining参考规则)

---

## 1 技术合规规范

### 核心要点
| 项目 | 规则 |
|------|------|
| `<w:pPr>` 元素顺序 | 必须遵循：`<w:pStyle>` → `<w:numPr>` → `<w:spacing>` → `<w:ind>` → `<w:jc>` |
| 空白处理 | 带前导/ trailing 空格的 `<w:t>` 元素必须添加 `xml:space='preserve'` |
| Unicode 转义 | ASCII 内容中的特殊符号必须转义：<br>左引号 `"` → `&#8220;`，右引号 `"` → `&#8221;`<br>撇号 `'` → `&#8217;`，长破折号 `—` → `&#8212;` |
| 追踪修订 | 必须使用 `<w:del>`/`<w:ins>` 标签，属性 `w:author="Claude"`，必须放在 `<w:r>` 元素外部；不得错放标签闭合 |
| RSID 格式 | 必须是 8 位十六进制（仅 `0-9A-F`），示例：`00AB1234` |
| 修订开启配置 | `settings.xml` 中必须在 `<w:proofState>` 之后添加 `<w:trackRevisions/>` |
| 图片处理 | 图片存放在 `word/media/`，`document.xml` 中引用，必须设置尺寸防止溢出 |

> [!WARNING] 冲突：无

---

## 2 文档内容标准 XML 模式

### 基本结构
```xml
<w:p>
  <w:r><w:t>Text content</w:t></w:r>
</w:p>
```

### 标题与样式
```xml
<!-- 居中标题 -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="Title"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r><w:t>Document Title</w:t></w:r>
</w:p>

<!-- 二级标题 -->
<w:p>
  <w:pPr><w:pStyle w:val="Heading2"/></w:pPr>
  <w:r><w:t>Section Heading</w:t></w:r>
</w:p>
```

### 文本格式
```xml
<!-- 加粗 -->
<w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Bold</w:t></w:r>
<!-- 斜体 -->
<w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t>Italic</w:t></w:r>
<!-- 下划线 -->
<w:r><w:rPr><w:u w:val="single"/></w:rPr><w:t>Underlined</w:t></w:r>
<!-- 高亮 -->
<w:r><w:rPr><w:highlight w:val="yellow"/></w:rPr><w:t>Highlighted</w:t></w:r>
```

### 列表
```xml
<!-- 编号列表 -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="ListParagraph"/>
    <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
    <w:spacing w:before="240"/>
  </w:pPr>
  <w:r><w:t>First item</w:t></w:r>
</w:p>

<!-- 从1重新编号：使用不同的numId -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="ListParagraph"/>
    <w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
    <w:spacing w:before="240"/>
  </w:pPr>
  <w:r><w:t>New list item 1</w:t></w:r>
</w:p>

<!-- 二级项目符号列表 -->
<w:p>
  <w:pPr>
    <w:pStyle w:val="ListParagraph"/>
    <w:numPr><w:ilvl w:val="1"/><w:numId w:val="1"/></w:numPr>
    <w:spacing w:before="240"/>
    <w:ind w:left="900"/>
  </w:pPr>
  <w:r><w:t>Bullet item</w:t></w:r>
</w:p>
```

### 表格
```xml
<w:tbl>
  <w:tblPr>
    <w:tblStyle w:val="TableGrid"/>
    <w:tblW w:w="0" w:type="auto"/>
  </w:tblPr>
  <w:tblGrid>
    <w:gridCol w:w="4675"/><w:gridCol w:w="4675"/>
  </w:tblGrid>
  <w:tr>
    <w:tc>
      <w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr>
      <w:p><w:r><w:t>Cell 1</w:t></w:r></w:p>
    </w:tc>
    <w:tc>
      <w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr>
      <w:p><w:r><w:t>Cell 2</w:t></w:r></w:p>
    </w:tc>
  </w:tr>
</w:tbl>
```

### 布局
```xml
<!-- 新章节前的分页 -->
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
<w:p>
  <w:pPr>
    <w:pStyle w:val="Heading1"/>
  </w:pPr>
  <w:r>
    <w:t>New Section Title</w:t>
  </w:r>
</w:p>

<!-- 居中段落 -->
<w:p>
  <w:pPr>
    <w:spacing w:before="240" w:after="0"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r><w:t>Centered text</w:t></w:r>
</w:p>

<!-- 段落级别字体修改 -->
<w:p>
  <w:pPr>
    <w:rPr
