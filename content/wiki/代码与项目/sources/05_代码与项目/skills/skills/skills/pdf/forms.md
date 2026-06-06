---
source: raw/05_代码与项目/skills/skills/skills/pdf/forms.md
raw_sha256: 0ab10e9095deb1c1f9f79eb04254589f55c1d16e095cb53191e03f9fc3184449
compiled_at: 2026-04-14T05:07:09.218Z
---
# PDF表单处理流程
> 来源路径：`raw/05_代码与项目/skills/skills/skills/pdf/forms.md`

## TL;DR
处理PDF表单必须按顺序完成所有步骤，禁止跳过前置步骤直接编写代码。首先检查PDF是否包含可填充表单域，再根据结果分别走可填充域/不可填充域两套处理流程生成填写完成的PDF。

## 通用前置步骤
> [!IMPORTANT] 强制要求
> 必须按顺序完成步骤，禁止跳过步骤直接编写代码。

1. 首先检查目标PDF是否带有可填充表单域，在当前文件目录执行脚本：
```bash
python scripts/check_fillable_fields <file.pdf>
```
2. 根据脚本结果选择对应流程：[可填充表单域流程](#可填充表单域流程) / [不可填充表单域流程](#不可填充表单域流程)

## 要点
### 可填充表单域流程
1. **提取表单域信息**：在当前目录执行脚本提取所有表单域信息到JSON文件，输出格式包含`field_id`、页码、 bounding box、域类型等信息，不同类型域会附带额外属性：
   | 域类型       | 额外属性说明                     |
   |--------------|----------------------------------|
   | checkbox     | 包含`checked_value`/`unchecked_value` |
   | radio_group  | 包含`radio_options`选项列表      |
   | choice       | 包含`choice_options`选项列表     |
   脚本命令：
   ```bash
   python scripts/extract_form_field_info.py <input.pdf> <field_info.json>
   ```
   提取出的JSON格式见[附录：可填充域提取输出格式](#附录可填充域提取输出格式)

2. **PDF转图片**：将PDF每一页转换为PNG图片，用于人工分析每个域的用途：
   ```bash
   python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>
   ```
   > 注意：需要将PDF坐标转换为图片坐标来匹配域位置

3. **创建填写值文件**：创建`field_values.json`，按照要求格式记录每个域需要填写的内容，`field_id`和`page`必须和提取出的`field_info.json`匹配，格式见[附录：可填充域填写值格式](#附录可填充域填写值格式)

4. **生成填写完成的PDF**：执行脚本自动填写，脚本会自动验证域ID和值的合法性，如果输出错误需要修正后重新执行：
   ```bash
   python scripts/fill_fillable_fields.py <input pdf> <field_values.json> <output pdf>
   ```

---

### 不可填充表单域流程
必须严格按顺序完成全部4个步骤，保证表单填写准确。整体流程为：转图片分析位置 → 创建字段配置 → 验证框位置 → 生成填写PDF

#### Step 1：可视化分析（必填）
1. PDF转PNG图片，每页生成一张：
   ```bash
   python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>
   ```
2. 识别所有需要填写的域，要求：
   - 文本域需要分别标注标签的 bounding box 和填写区域的 bounding box
   - 标签框和填写框**不能相交**
   - 填写框仅包含需要输入数据的区域，尺寸足够容纳输入文本
   - 不同布局的标注规则：
     | 布局类型         | 填写区域标注规则 |
     |------------------|------------------|
     | 标签在框内       | 填写区域为标签右侧到框边缘 |
     | 标签在前下划线在后 | 填写区域覆盖下划线整宽，位于线上方 |
     | 标签在下划线在上 | 填写区域覆盖下划线整宽，位于线上方（签名/日期常用） |
     | 标签在上下划线在下 | 填写区域从标签底部到下划线，覆盖整宽 |
   - 复选框标注规则：仅将小方框作为填写框（红色标注），标签文本放入标签框（蓝色标注），填写框不能包含文本

#### Step 2：创建`fields.json`和验证图（必填）
`fields.json`格式包含页面信息和所有表单域信息，示例格式见[附录：不可填充域配置格式](#附录不可填充域配置格式)
- 文本域可配置字体大小、字体颜色，默认值为12号黑色
- 复选框默认填写`X`标记

创建完配置后，为每页生成验证图（红色框为填写区域，蓝色框为标签区域）：
```bash
python scripts/create_validation_image.py <page_number> <path_to_fields.json> <input_image_path> <output_image_path>
```

#### Step 3：验证 bounding box（必填）
分为自动验证和人工验证两步，全部通过才能进入下一步：
1. **自动相交验证**：运行脚本检查是否存在框相交、填写框高度不足的问题：
   ```bash
   python scripts/check_bounding_boxes.py <JSON file>
   ```
   如有错误需要调整 bounding box 后重新验证，直到无错误。

2. **人工检查验证图**（强制要求，不能跳过），验证规则：
   - 红色框仅覆盖输入区域，不能包含任何文本
   - 蓝色框完整包含标签文本
   - 复选框的红色框必须居中对齐复选框小方框
   如果不符合要求，修改`fields.json`重新生成验证图再次检查，直到完全准确。

#### Step 4：生成填写完成的PDF
运行脚本根据`fields.json`添加文本注释，生成最终PDF：
```bash
python scripts/fill_pdf_form_with_annotations.py <input_pdf_path> <path_to_fields.json> <output_pdf_path>
```

---

## 冲突标注
当前来源未与其他现有流程产生已知冲突。

## 引用证据片段
> **CRITICAL: You MUST complete these steps in order. Do not skip ahead to writing code.**

---

## 附录：格式参考
### 附录：可填充域提取输出格式
```json
[
  {
    "field_id": "(unique ID for the field)",
    "page": "(page number, 1-based)",
    "rect": "([left, bottom, right, top] bounding box in PDF coordinates, y=0 is the bottom of the page)",
    "type": "("text", "checkbox", "radio_group", or "choice")"
  },
  {
    "field_id": "(unique ID for the field)",
    "page": "(page number, 1-based)",
    "type": "checkbox",
    "checked_value": "(Set the field to this value to check the checkbox)",
    "unchecked_value": "(Set the field to this value to uncheck the checkbox)"
  },
  {
    "field_id": "(unique ID for the field)",
    "page": "(page number, 1-based)",
    "type": "radio_group",
    "radio_options": [
      {
        "value": "(set the field to this value to select this radio option)",
        "rect": "(bounding box for the radio button for this option)"
      }
    ]
  },
  {
    "field_id": "(unique ID for the field)",
    "page": "(page number, 1-based)",
    "type": "choice",
    "choice_options": [
      {
        "value": "(set the field to this value to select this option)",
        "text": "(display text of the option)"
      }
    ]
  }
]
```

### 附录：可填充域填写值格式
```json
[
  {
    "field_id": "last_name",
    "description": "The user's last name",
    "page": 1,
    "value": "Simpson"
  },
  {
    "field_id": "Checkbox12",
    "description": "Checkbox to be checked if the user is 18 or over",
    "page": 1,
    "value": "/On"
  }
]
```

### 附录：不可填充域配置格式
```json
{
  "pages": [
    {
      "page_number": 1,
      "image_width": "(first page image width in pixels)",
      "image_height": "(first page image height in pixels)"
    },
    {
      "page_number": 2,
      "image_width": "(second page image width in pixels)",
      "image_height": "(second page image height in pixels)"
    }
  ],
  "form_fields": [
    {
      "page_number": 1,
      "description": "The user's last name should be entered here",
      "field_label": "Last name",
      "label_bounding_box": [30, 125, 95, 142],
