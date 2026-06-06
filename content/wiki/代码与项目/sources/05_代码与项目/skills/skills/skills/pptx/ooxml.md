---
source: raw/05_代码与项目/skills/skills/skills/pptx/ooxml.md
raw_sha256: 09868e9f1786765421ecf3f0f49c77006738efda82a76df43ed87f7a9bfe2467
compiled_at: 2026-04-14T05:08:42.032Z
---
> [!info]
> 来源路径：`raw/05_代码与项目/skills/skills/skills/pptx/ooxml.md`

# Office Open XML (PowerPoint 格式) 技术参考

## TL;DR
本文是PPTX（Office Open XML 格式）开发的技术参考，规定了PowerPoint文档XML的结构规范、元素要求、常见操作流程和需要避免的错误，用于生成符合规范、可被PowerPoint正常打开的PPTX文件。

## 技术规范要点
### 核心合规要求
| 规则项 | 具体要求 |
|--------|----------|
| `<p:txBody>`元素顺序 | 必须按照 `<a:bodyPr>` → `<a:lstStyle>` → `<a:p>` 排序 |
| 首尾空白处理 | 包含首尾空格的`<a:t>`元素必须添加`xml:space='preserve'`属性 |
| Unicode转义 | ASCII内容中特殊字符需要转义，例如 `"` 需要转义为 `&#8220;` |
| 图片存储 | 图片放入`ppt/media/`目录，在幻灯片XML中引用，尺寸适配幻灯片边界 |
| 资源关联 | 每个幻灯片的资源必须更新`ppt/slides/_rels/slideN.xml.rels`关系文件 |
| 文本状态标记 | 在`<a:rPr>`和`<a:endParaRPr>`元素添加`dirty="0"`标记干净文本状态 |

### 常见操作流程要点
1. **新增幻灯片**：创建文件→更新内容类型→更新演示关系→添加幻灯片ID→创建关系文件→更新统计
2. **复制幻灯片**：复制文件修改唯一ID→走新增流程→清除无效注释/资源引用
3. **重排幻灯片**：仅修改`ppt/presentation.xml`中`<p:sldIdLst>`内元素顺序，无需修改原有ID和文件名
4. **删除幻灯片**：删除所有入口条目、对应文件，更新统计，清理未使用资源

## 完整结构与代码示例
### 演示文稿结构
#### 基础幻灯片结构
```xml
<!-- ppt/slides/slide1.xml -->
<p:sld>
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr>...</p:nvGrpSpPr>
      <p:grpSpPr>...</p:grpSpPr>
      <!-- Shapes go here -->
    </p:spTree>
  </p:cSld>
</p:sld>
```

#### 带文本的文本框/形状
```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="2" name="Title"/>
    <p:cNvSpPr>
      <a:spLocks noGrp="1"/>
    </p:cNvSpPr>
    <p:nvPr>
      <p:ph type="ctrTitle"/>
    </p:nvPr>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="838200" y="365125"/>
      <a:ext cx="7772400" cy="1470025"/>
    </a:xfrm>
  </p:spPr>
  <p:txBody>
    <a:bodyPr/>
    <a:lstStyle/>
    <a:p>
      <a:r>
        <a:t>Slide Title</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

#### 文本格式示例
```xml
<!-- Bold -->
<a:r>
  <a:rPr b="1"/>
  <a:t>Bold Text</a:t>
</a:r>

<!-- Italic -->
<a:r>
  <a:rPr i="1"/>
  <a:t>Italic Text</a:t>
</a:r>

<!-- Underline -->
<a:r>
  <a:rPr u="sng"/>
  <a:t>Underlined</a:t>
</a:r>

<!-- Highlight -->
<a:r>
  <a:rPr>
    <a:highlight>
      <a:srgbClr val="FFFF00"/>
    </a:highlight>
  </a:rPr>
  <a:t>Highlighted Text</a:t>
</a:r>

<!-- Font and Size -->
<a:r>
  <a:rPr sz="2400" typeface="Arial">
    <a:solidFill>
      <a:srgbClr val="FF0000"/>
    </a:solidFill>
  </a:rPr>
  <a:t>Colored Arial 24pt</a:t>
</a:r>

<!-- Complete formatting example -->
<a:r>
  <a:rPr lang="en-US" sz="1400" b="1" dirty="0">
    <a:solidFill>
      <a:srgbClr val="FAFAFA"/>
    </a:solidFill>
  </a:rPr>
  <a:t>Formatted text</a:t>
</a:r>
```

#### 列表示例
```xml
<!-- Bullet list -->
<a:p>
  <a:pPr lvl="0">
    <a:buChar char="•"/>
  </a:pPr>
  <a:r>
    <a:t>First bullet point</a:t>
  </a:r>
</a:p>

<!-- Numbered list -->
<a:p>
  <a:pPr lvl="0">
    <a:buAutoNum type="arabicPeriod"/>
  </a:pPr>
  <a:r>
    <a:t>First numbered item</a:t>
  </a:r>
</a:p>

<!-- Second level indent -->
<a:p>
  <a:pPr lvl="1">
    <a:buChar char="•"/>
  </a:pPr>
  <a:r>
    <a:t>Indented bullet</a:t>
  </a:r>
</a:p>
```

#### 形状示例
```xml
<!-- Rectangle -->
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="3" name="Rectangle"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="1000000" y="1000000"/>
      <a:ext cx="3000000" cy="2000000"/>
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="FF0000"/>
    </a:solidFill>
    <a:ln w="25400">
      <a:solidFill>
        <a:srgbClr val="000000"/>
      </a:solidFill>
    </a:ln>
  </p:spPr>
</p:sp>

<!-- Rounded Rectangle -->
<p:sp>
  <p:spPr>
    <a:prstGeom prst="roundRect">
      <a:avLst/>
    </a:prstGeom>
  </p:spPr>
</p:sp>

<!-- Circle/Ellipse -->
<p:sp>
  <p:spPr>
    <a:prstGeom prst="ellipse">
      <a:avLst/>
    </a:prstGeom>
  </p:spPr>
</p:sp>
```

#### 图片示例
```xml
<p:pic>
  <p:nvPicPr>
    <p:cNvPr id="4" name="Picture">
      <a:hlinkClick r:id="" action="ppaction://media"/>
    </p:cNvPr>
    <p:cNvPicPr>
      <a:picLocks noChangeAspect="1"/>
    </p:cNvPicPr>
    <p:nvPr/>
  </p:nvPicPr>
  <
