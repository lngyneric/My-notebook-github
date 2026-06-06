---
source: raw/05_代码与项目/skills/skills/skills/pdf/reference.md
raw_sha256: 03a5f964f8abecbbe156f363356e927e864d7ee964f1012c84ee1bfc8acbeb95
compiled_at: 2026-04-14T05:07:40.302Z
---
# PDF 处理高级参考
> 来源路径：`raw/05_代码与项目/skills/skills/skills/pdf/reference.md`

## TL;DR
本文档汇总了多种环境（Python/JavaScript/命令行）下未在基础教程中覆盖的高级PDF处理功能，包含核心库的进阶用法、复杂工作流示例、性能优化与常见问题排查方案。

---

## 目录
- [pypdfium2 库（Python）](#pypdfium2-库-apachebsd-许可证)
- [JavaScript PDF 处理库](#javascript-库)
- [高级命令行操作](#高级命令行操作)
- [高级 Python 技术](#高级-python-技术)
- [复杂工作流示例](#复杂工作流)
- [性能优化建议](#性能优化技巧)
- [常见问题排查](#故障排除常见问题)
- [许可证信息](#许可证信息)

---

## pypdfium2 库 (Apache/BSD 许可证)
### 概述
pypdfium2 是 Chromium 核心 PDF 库 PDFium 的 Python 绑定，适合快速PDF渲染、图片生成，可作为 PyMuPDF 的替代方案。

### 示例1：PDF 渲染为图片
```python
import pypdfium2 as pdfium
from PIL import Image

# 加载PDF
pdf = pdfium.PdfDocument("document.pdf")

# 渲染单页为图片
page = pdf[0]  # 第一页
bitmap = page.render(
    scale=2.0,  # 缩放参数，值越大分辨率越高
    rotation=0  # 旋转角度，0为不旋转
)

# 转换为PIL Image并保存
img = bitmap.to_pil()
img.save("page_1.png", "PNG")

# 批量处理多页
for i, page in enumerate(pdf):
    bitmap = page.render(scale=1.5)
    img = bitmap.to_pil()
    img.save(f"page_{i+1}.jpg", "JPEG", quality=90)
```

### 示例2：提取文本
```python
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("document.pdf")
for i, page in enumerate(pdf):
    text = page.get_text()
    print(f"Page {i+1} text length: {len(text)} chars")
```

---

## JavaScript 库

### pdf-lib (MIT 许可证)
pdf-lib 是一款功能强大的 JavaScript 库，可在任意JS环境中创建和修改PDF文档。

#### 示例1：加载并修改现有PDF
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function manipulatePDF() {
    // 加载已有PDF
    const existingPdfBytes = fs.readFileSync('input.pdf');
    const pdfDoc = await PDFDocument.load(existingPdfBytes);

    // 获取页数
    const pageCount = pdfDoc.getPageCount();
    console.log(`Document has ${pageCount} pages`);

    // 添加新页面
    const newPage = pdfDoc.addPage([600, 400]);
    newPage.drawText('Added by pdf-lib', {
        x: 100,
        y: 300,
        size: 16
    });

    // 保存修改后的PDF
    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('modified.pdf', pdfBytes);
}
```

#### 示例2：从零创建复杂PDF
```javascript
import { PDFDocument, rgb, StandardFonts } from 'pdf-lib';
import fs from 'fs';

async function createPDF() {
    const pdfDoc = await PDFDocument.create();

    // 嵌入字体
    const helveticaFont = await pdfDoc.embedFont(StandardFonts.Helvetica);
    const helveticaBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

    // 添加A4页面
    const page = pdfDoc.addPage([595, 842]); // A4尺寸
    const { width, height } = page.getSize();

    // 添加样式化文本
    page.drawText('Invoice #12345', {
        x: 50,
        y: height - 50,
        size: 18,
        font: helveticaBold,
        color: rgb(0.2, 0.2, 0.8)
    });

    // 添加矩形（表头背景）
    page.drawRectangle({
        x: 40,
        y: height - 100,
        width: width - 80,
        height: 30,
        color: rgb(0.9, 0.9, 0.9)
    });

    // 添加类表格内容
    const items = [
        ['Item', 'Qty', 'Price', 'Total'],
        ['Widget', '2', '$50', '$100'],
        ['Gadget', '1', '$75', '$75']
    ];

    let yPos = height - 150;
    items.forEach(row => {
        let xPos = 50;
        row.forEach(cell => {
            page.drawText(cell, {
                x: xPos,
                y: yPos,
                size: 12,
                font: helveticaFont
            });
            xPos += 120;
        });
        yPos -= 25;
    });

    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('created.pdf', pdfBytes);
}
```

#### 示例3：高级合并拆分操作
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function mergePDFs() {
    // 创建新文档
    const mergedPdf = await PDFDocument.create();

    // 加载源PDF
    const pdf1Bytes = fs.readFileSync('doc1.pdf');
    const pdf2Bytes = fs.readFileSync('doc2.pdf');

    const pdf1 = await PDFDocument.load(pdf1Bytes);
    const pdf2 = await PDFDocument.load(pdf2Bytes);

    // 复制第一个PDF的所有页面
    const pdf1Pages = await mergedPdf.copyPages(pdf1, pdf1.getPageIndices());
    pdf1Pages.forEach(page => mergedPdf.addPage(page));

    // 仅复制第二个PDF的指定页面（第0、2、4页）
    const pdf2Pages = await mergedPdf.copyPages(pdf2, [0, 2, 4]);
    pdf2Pages.forEach(page => mergedPdf.addPage(page));

    const mergedPdfBytes = await mergedPdf.save();
    fs.writeFileSync('merged.pdf', mergedPdfBytes);
}
```

---

### pdfjs-dist (Apache 许可证)
PDF.js 是 Mozilla 推出的浏览器端PDF渲染JavaScript库。

#### 示例1：基础PDF加载与渲染
```javascript
import * as pdfjsLib from 'pdfjs-dist';

// 配置worker（对性能很重要）
pdfjsLib.GlobalWorkerOptions.workerSrc = './pdf.worker.js';

async function renderPDF() {
    // 加载PDF
    const loadingTask = pdfjsLib.getDocument('document.pdf');
    const pdf = await loadingTask.promise;

    console.log(`Loaded PDF with ${pdf.numPages} pages`);

    // 获取第一页
    const page = await pdf.getPage(1);
    const viewport = page.getViewport({ scale: 1.5 });

    // 渲染到canvas
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.height = viewport.height;
    canvas.width = viewport.width;

    const renderContext = {
        canvasContext: context,
        viewport: viewport
    };

    await page.render(renderContext).promise;
    document.body.appendChild(canvas);
}
```

#### 示例2：带坐标的文本提取
```javascript
import * as pdfjsLib from 'pdfjs-dist';

async function extractText() {
    const loadingTask = pdfjsLib.getDocument('document.pdf');
    const pdf = await loadingTask.promise;

    let fullText = '';

    // 从所有页面提取文本
    for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const textContent = await page.getTextContent();

        const pageText = textContent.items
            .map(item => item.str)
            .join(' ');

        fullText += `\n--- Page ${i} ---\n${pageText}`;

        // 获取带坐标的文本用于高级处理
        const textWithCoords = textContent.items
