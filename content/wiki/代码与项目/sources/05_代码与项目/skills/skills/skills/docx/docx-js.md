---
source: raw/05_代码与项目/skills/skills/skills/docx/docx-js.md
raw_sha256: 83b4a2f88d058a10509fbc0b3b12b6933c407805f4d4afc955cd3fb939c16428
compiled_at: 2026-04-14T05:04:26.549Z
---
# docx-js
> 来源路径：`raw/05_代码与项目/skills/skills/skills/docx/docx-js.md`

---

## TL;DR
docx-js 是一个用于在 JavaScript/TypeScript 中生成 `.docx` 文件的开源库，本教程整理了官方推荐用法、强制格式规则和常见错误避坑指南，严格遵循规则可避免生成损坏文件或渲染异常。

---

## 要点
1. 行换行必须使用单独 `Paragraph` 元素，绝对禁止使用 `\n`
2. 列表必须通过编号配置生成，绝对禁止使用 Unicode 字符/`SymbolRun` 制作假列表，编号使用 `LevelFormat.BULLET` 常量而非字符串
3. 每个独立编号列表必须使用唯一的 `reference`，不同 reference 会独立重新计数
4. 表格必须同时设置表格级 `columnWidths` 和每个单元格的宽度，边框要加在单元格而非表格上，单元格 shading 必须用 `ShadingType.CLEAR` 防止出现黑色背景
5. 分页必须放在 `Paragraph` 内部，禁止使用 standalone `PageBreak`，否则会生成无效 XML 导致 Word 无法打开
6. 图片必须指定 `type` 参数和完整 altText 三个字段
7. 目录只支持使用原生 `HeadingLevel` 的标题，禁止给标题段落加自定义样式，否则目录会失效
8. 推荐使用自定义样式替代行内格式，设置全局默认字体（推荐 Arial）保证兼容性

---

## 安装与基础用法
### 安装
假设已全局安装，若未安装执行：
```bash
npm install -g docx
```

### 基础引入与保存
```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun, Media, 
        Header, Footer, AlignmentType, PageOrientation, LevelFormat, ExternalHyperlink, 
        InternalHyperlink, TableOfContents, HeadingLevel, BorderStyle, WidthType, TabStopType, 
        TabStopPosition, UnderlineType, ShadingType, VerticalAlign, SymbolRun, PageNumber,
        FootnoteReferenceRun, Footnote, PageBreak } = require('docx');

// 创建 & 保存文档
const doc = new Document({ sections: [{ children: [/* content */] }] });
Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer)); // Node.js 环境
Packer.toBlob(doc).then(blob => { /* download logic */ }); // 浏览器环境
```

---

## 文本与格式
> [!WARNING]
> 强制规则：永远不要用 `\n` 做换行，必须每个行使用单独 `Paragraph`
> ```javascript
> // ❌ 错误写法: new TextRun("Line 1\nLine 2")
> // ✅ 正确写法: new Paragraph({ children: [new TextRun("Line 1")] }), new Paragraph({ children: [new TextRun("Line 2")] })
> ```

```javascript
// 带全部格式化选项的基础文本
new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 200, after: 200 },
  indent: { left: 720, right: 720 },
  children: [
    new TextRun({ text: "Bold", bold: true }),
    new TextRun({ text: "Italic", italics: true }),
    new TextRun({ text: "Underlined", underline: { type: UnderlineType.DOUBLE, color: "FF0000" } }),
    new TextRun({ text: "Colored", color: "FF0000", size: 28, font: "Arial" }), // 默认Arial
    new TextRun({ text: "Highlighted", highlight: "yellow" }),
    new TextRun({ text: "Strikethrough", strike: true }),
    new TextRun({ text: "x2", superScript: true }),
    new TextRun({ text: "H2O", subScript: true }),
    new TextRun({ text: "SMALL CAPS", smallCaps: true }),
    new SymbolRun({ char: "2022", font: "Symbol" }), // 项目符号 •
    new SymbolRun({ char: "00A9", font: "Arial" })   // 版权符号 © - 符号推荐用Arial
  ]
})
```

---

## 样式与专业格式化
```javascript
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 24 } } }, // 12pt 默认字号
    paragraphStyles: [
      // 文档标题样式 - 覆盖内置Title样式
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 56, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, alignment: AlignmentType.CENTER } },
      // 重要提示：必须使用准确ID才能覆盖内置标题样式
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: "000000", font: "Arial" }, // 16pt
        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } }, // 目录生成要求必须设置
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, color: "000000", font: "Arial" }, // 14pt
        paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 } },
      // 自定义样式使用自定义ID
      { id: "myStyle", name: "My Style", basedOn: "Normal",
        run: { size: 28, bold: true, color: "000000" },
        paragraph: { spacing: { after: 120 }, alignment: AlignmentType.CENTER } }
    ],
    characterStyles: [{ id: "myCharStyle", name: "My Char Style",
      run: { color: "FF0000", bold: true, underline: { type: UnderlineType.SINGLE } } }]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [
      new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("Document Title")] }), // 使用覆盖后的Title样式
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Heading 1")] }), // 使用覆盖后的Heading1样式
      new Paragraph({ style: "myStyle", children: [new TextRun("Custom paragraph style")] }),
      new Paragraph({ children: [
        new TextRun("Normal with "),
        new TextRun({ text: "custom char style", style: "myCharStyle" })
      ]})
    ]
  }]
});
```

### 推荐专业字体组合
- **Arial (标题) + Arial (正文)**：通用性最强，干净专业
- **Times New Roman (标题) + Arial (正文)**：经典衬线标题+现代无衬线正文
- **Georgia (标题) + Verdana (正文)**：屏幕阅读优化，优雅对比

### 核心样式原则
- 覆盖内置样式：必须使用准确ID `Heading1`/`Heading2`/`Heading3` 才能覆盖Word内置标题样式
- `HeadingLevel` 常量对应：`HeadingLevel.HEADING_1` 对应 `Heading1` 样式，以此类推
- 必须添加 `outlineLevel`：H1 设 `outlineLevel: 0`，H2 设 `outlineLevel: 1`，以此类推保证目录正常工作
- 使用自定义样式替代行内格式保证一致性
- 通过 `styles.default.document.run.font` 设置默认字体，推荐使用通用性最强的 Arial
- 通过字号差建立视觉层级（标题>子标题>正文）
- 通过 `before`/`after` 给段落添加正确间距
- 尽量少用颜色，标题正文默认使用黑色（`000000`）和灰色系
- 标准1英寸边距对应数值是 `1440`
