---
source: raw/05_代码与项目/skills/skills/skills/docx/SKILL.md
raw_sha256: 0bd90681fcab2e282025ee14acf508b60bbd6c41ac6c3bf83c0dc14d52c37933
compiled_at: 2026-04-14T05:05:13.319Z
---
# DOCX 文档处理技能
> 来源路径：`raw/05_代码与项目/skills/skills/skills/docx/SKILL.md`

> [!TL;DR]
> 本技能用于实现 `.docx` 文档的创建、编辑、分析和格式转换，支持带追踪修订的审阅工作流，覆盖文本提取、内容修改、格式保留、注释处理等多种专业文档处理场景。

---

## 基础信息
| 项目 | 内容 |
|------|------|
| 名称 | `docx` |
| 许可证 | 专有，完整条款见 LICENSE.txt |
| 适用场景 | 新建文档、修改已有文档、处理追踪修订、添加批注及其他专业文档任务 |

---

## 核心要点
1. 工作流按任务类型选择，编辑场景优先使用红lining（带追踪修订）工作流，法定/学术/政务文档强制要求该工作流
2. 新建Word文档使用`docx-js`，编辑现有文档使用基于Python的Document库操作OOXML
3. 带追踪修订的编辑需遵循「最小精确修改」原则，仅标记实际变更内容
4. 变更采用分批处理策略，每批3-10个关联变更，分批测试降低调试难度
5. 所有核心工具文档必须完整通读，禁止设置范围读取

---

## 工作流选择决策树
```mermaid
flowchart TD
    A[DOCX任务] --> B[读取/分析内容]
    A --> C[新建文档]
    A --> D[编辑现有文档]
    B --> E[仅需文本内容 → 文本提取(pandoc)]
    B --> F[需要批注/格式/元数据/媒体 → 原始XML访问]
    C --> G[使用 docx-js 新建工作流]
    D --> H[自有文档+简单修改 → 基础OOXML编辑]
    D --> I[他人文档/法定/学术/政务文档 → 红lining追踪修订工作流<br/>(推荐/强制要求)]
```

---

## 详细流程

### 1. 读取和分析内容

#### 1.1 文本提取
仅需要读取文档文本内容时，使用pandoc转换，支持保留追踪修订：
```bash
# 带全部追踪修订转换为markdown
pandoc --track-changes=all 目标文件.docx -o 输出.md
# 选项说明：--track-changes=accept/reject/all 分别表示接受所有修订/拒绝所有修订/保留全部修订
```

#### 1.2 原始XML访问
需要处理批注、复杂格式、文档结构、嵌入媒体、元数据时，需要解压文档读取原始XML：
- 解压命令：
```bash
python ooxml/scripts/unpack.py <office文件> <输出目录>
```
- 关键文件结构：
  * `word/document.xml` - 文档主内容
  * `word/comments.xml` - 文档引用的批注
  * `word/media/` - 嵌入的图片和媒体文件
  * 追踪修订标签：`<w:ins>` 代表插入，`<w:del>` 代表删除

---

### 2. 新建Word文档
从头新建Word文档使用`docx-js`，通过JavaScript/TypeScript创建：
1. **强制要求：完整通读 [`docx-js.md`](docx-js.md) 全部内容，禁止设置读取范围**，获取完整语法、格式规则和最佳实践后再开始操作
2. 使用`Document`、`Paragraph`、`TextRun`组件创建JS/TS文件（依赖默认已安装，依赖安装见本文末尾）
3. 使用`Packer.toBuffer()`导出为`.docx`文件

---

### 3. 编辑现有Word文档
编辑现有文档使用Python的Document库操作OOXML，支持高级API和底层DOM直接访问：
1. **强制要求：完整通读 [`ooxml.md`](ooxml.md) 全部内容，禁止设置读取范围**，获取Document库API和直接编辑的XML模式
2. 解压文档：`python ooxml/scripts/unpack.py <office文件> <输出目录>`
3. 创建并运行使用Document库的Python脚本（参考ooxml.md的Document库章节）
4. 打包生成最终文档：`python ooxml/scripts/pack.py <输入目录> <输出docx文件>`

---

### 4. 红lining追踪修订工作流（文档审阅专用）
该工作流用于实现规范的带追踪修订的文档修改，**法定/学术/政务文档强制使用该工作流**。

#### 核心原则
- 分批策略：关联变更分组为3-10个变更每批，平衡调试效率和工作效率，每批测试后再进行下一批
- 最小精确修改：仅标记实际发生变更的文本，保留不变内容的原始RSID，拆分模式为：`[不变文本] + [删除] + [插入] + [不变文本]`

错误和正确示例对比（修改句子中「30天」为「60天」）：
```python
# 错误：替换整个句子，多余标记
'<w:del><w:r><w:delText>The term is 30 days.</w:delText></w:r></w:del><w:ins><w:r><w:t>The term is 60 days.</w:t></w:r></w:ins>'

# 正确：仅标记变更，保留不变文本的原始<w:r>和RSID
'<w:r w:rsidR="00AB12CD"><w:t>The term is </w:t></w:r><w:del><w:r><w:delText>30</w:delText></w:r></w:del><w:ins><w:r><w:t>60</w:t></w:r></w:ins><w:r w:rsidR="00AB12CD"><w:t> days.</w:t></w:r>'
```

#### 完整工作流步骤
1. **获取带修订的markdown版本**：
   ```bash
   pandoc --track-changes=all 原文件.docx -o current.md
   ```

2. **识别和分组变更**：梳理所有需要修改的内容，按逻辑分批。定位变更不使用markdown行号（无法映射到XML结构），可使用：
   - 章节/标题编号（如「3.2节」、「第四条」）
   - 带编号段落的编号
   - 唯一上下文的grep匹配模式
   - 文档结构位置（如「第一段」、「签名块」）

   分批方式：按章节/按变更类型/按复杂度（先简单后复杂）/按页码范围，每批3-10个关联变更

3. **读取文档并解压**：
   - **强制要求：完整通读 [`ooxml.md`](ooxml.md) 全部内容，禁止设置读取范围**，重点阅读Document库和追踪修订模式章节
   - 解压文档：`python ooxml/scripts/unpack.py <file.docx> <输出目录>`
   - 记录解压脚本给出的推荐RSID，用于后续插入的修订

4. **分批实现变更**：按分组依次实现每批变更：
   - a. 文本映射到XML：grep匹配`word/document.xml`中的文本，确认文本在`<w:r>`元素中的拆分方式
   - b. 创建并运行脚本：使用`get_node`查找节点，实现变更后调用`doc.save()`，具体模式参考ooxml.md的Document库章节
   - 注意：每次编写脚本前都需要重新grep确认`word/document.xml`的内容和行号，行号会在每次脚本运行后变化

5. **打包文档**：所有批次完成后，将解压目录打包回docx：
   ```bash
   python ooxml/scripts/pack.py 解压目录 审阅后文档.docx
   ```

6. **最终验证**：完整检查所有变更：
   - 转换最终文档为markdown：
     ```bash
     pandoc --track-changes=all 审阅后文档.docx -o verification.md
     ```
   - 验证所有变更正确应用：
     ```bash
     grep "原文本" verification.md  # 不应匹配到原文本
     grep "替换文本" verification.md  # 应匹配到替换文本
     ```
   - 检查是否引入非预期变更

---

### 5. 文档转换为图片
如需可视化分析Word文档，可转换为图片，步骤如下：
1. DOCX转换为PDF：
```bash
soffice --headless --convert-to pdf document.docx
```

2. PDF分页转换为JPEG图片：
```bash
pdftoppm -jpeg -r 150 document.pdf page
```
生成结果为`page-1.jpg`、`page
