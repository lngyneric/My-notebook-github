---
source: raw/05_代码与项目/skills/skills/skills/xlsx/SKILL.md
raw_sha256: 020ccdb5932257b66c638ec1157ea248d57fa52c8c01f1f68b559b5970c7df35
compiled_at: 2026-04-14T05:18:05.104Z
---
# xlsx
> 来源路径：`raw/05_代码与项目/skills/skills/skills/xlsx/SKILL.md`

---

## TL;DR
本技能定义了处理电子表格文件（`.xlsx`/`.xlsm`/`.csv`/`.tsv`等）的操作规范、输出要求和工作流，支持电子表格新建、编辑、数据分析与可视化，核心要求是**必须使用Excel公式而非硬编码计算值、输出文件必须零公式错误，修改后必须通过`recalc.py`脚本调用LibreOffice重新计算公式**。

---

## 基础信息
| 项目 | 内容 |
|------|------|
| 名称 | `xlsx` |
| 描述 | 支持公式、格式、数据分析和可视化的全功能电子表格创建、编辑和分析能力，适用于以下场景：<br>1. 新建带公式和格式的电子表格<br>2. 读取或分析数据<br>3. 在保留公式的前提下修改现有电子表格<br>4. 电子表格内的数据分析和可视化<br>5. 重新计算公式 |
| 协议 | 专有协议，完整条款见`LICENSE.txt` |

---

## 输出要求要点
### 所有Excel文件通用要求
1. 必须交付**零公式错误**的文件，不允许存在`#REF!`/`#DIV/0!`/`#VALUE!`/`#N/A`/`#NAME?`等错误
2. 修改现有模板时：必须严格匹配现有格式、样式和规范，不得对已有固定模式的文件强制标准化格式，现有模板规范优先级高于本指南

### 财务模型额外规范
#### 颜色编码标准（无用户要求或现有模板约定时生效）
遵循行业标准颜色约定：
- 蓝色文本（RGB: `0,0,255`）：硬编码输入，用户会根据场景修改的数字
- 黑色文本（RGB: `0,0,0`）：所有公式和计算结果
- 绿色文本（RGB: `0,128,0`）：同一工作簿内其他工作表的链接
- 红色文本（RGB: `255,0,0`）：指向其他文件的外部链接
- 黄色背景（RGB: `255,255,0`）：需要关注的关键假设或需要更新的单元格

#### 数字格式标准
| 类型 | 格式要求 |
|------|----------|
| 年份 | 文本格式，例如`2024`而非`2,024` |
| 货币 | 采用`$#,##0`格式，表头必须标注单位（例如`Revenue ($mm)`） |
| 零值 | 通过数字格式将所有零显示为`-`，格式示例：`$#,##0;($#,##0);-`，百分比零值也遵循此规则 |
| 百分比 | 默认使用`0.0%`格式（保留一位小数） |
| 估值倍数 | 格式为`0.0x`（例如EV/EBITDA、P/E） |
| 负数 | 使用括号`(123)`而非负号`-123` |

#### 公式构建规则
1. 假设放置：所有假设（增长率、利润率、倍数等）必须放在单独的假设单元格，公式中必须使用单元格引用而非硬编码值，例如用`=B5*(1+$B$6)`代替`=B5*1.05`
2. 错误预防：必须验证单元格引用正确、检查范围偏移错误、确保预测周期内公式一致、用边缘案例（零值、负数）测试、确认不存在意外循环引用
3. 硬编码文档要求：硬编码值必须添加来源注释（可放在单元格注释或表格旁的单元格），格式：`Source: [来源系统/文档], [日期], [具体引用], [如有则添加URL]`

---

## 工作流与开发规范要点
1. **核心规则：永远使用Excel公式，不硬编码Python计算值**，保证电子表格动态可更新
2. **工具选择**：pandas适合数据分析、批量操作；openpyxl适合处理公式、格式和Excel原生特性
3. **强制要求**：使用公式后必须用`recalc.py`脚本调用LibreOffice重新计算公式，该脚本会自动扫描所有错误并返回JSON格式的错误详情
4. 公式验证：必须做引用测试、列行映射检查、边缘案例测试，重点规避引用错误、除零错误等常见问题

---

## 引用证据片段
### 核心要求原文
> **CRITICAL: Use Formulas, Not Hardcoded Values**
> 
> **Always use Excel formulas instead of calculating values in Python and hardcoding them.** This ensures the spreadsheet remains dynamic and updateable.
> 
> This applies to ALL calculations - totals, percentages, ratios, differences, etc. The spreadsheet should be able to recalculate when source data changes.

### 常见工作流原文
> 1. **Choose tool**: pandas for data, openpyxl for formulas/formatting
> 2. **Create/Load**: Create new workbook or load existing file
> 3. **Modify**: Add/edit data, formulas, and formatting
> 4. **Save**: Write to file
> 5. **Recalculate formulas (MANDATORY IF USING FORMULAS)**: Use the recalc.py script
>    ```bash
>    python recalc.py output.xlsx
>    ```
> 6. **Verify and fix any errors**: 
>    - The script returns JSON with error details
>    - If `status` is `errors_found`, check `error_summary` for specific error types and locations
>    - Fix the identified errors and recalculate again

### recalc.py调用示例
```bash
python recalc.py <excel_file> [timeout_seconds]
# 示例
python recalc.py output.xlsx 30
```

### 错误输出格式示例
```json
{
  "status": "success",           // or "errors_found"
  "total_errors": 0,              // Total error count
  "total_formulas": 42,           // Number of formulas in file
  "error_summary": {              // Only present if errors found
    "#REF!": {
      "count": 2,
      "locations": ["Sheet1!B5", "Sheet1!C10"]
    }
  }
}
```

### 新建Excel文件示例（openpyxl）
```python
# Using openpyxl for formulas and formatting
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# Add data
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
sheet.append(['Row', 'of', 'data'])

# Add formula
sheet['B2'] = '=SUM(A1:A10)'

# Formatting
sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')

# Column width
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

### 编辑现有Excel文件示例（openpyxl）
```python
# Using openpyxl to preserve formulas and formatting
from openpyxl import load_workbook

# Load existing file
wb = load_workbook('existing.xlsx')
sheet = wb.active  # or wb['SheetName'] for specific sheet

# Working with multiple sheets
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]
    print(f"Sheet: {sheet_name}")

# Modify cells
sheet['A1'] = 'New Value'
sheet.insert_rows(2)  # Insert row at position 2
sheet.delete_cols(3)  # Delete column 3

# Add new sheet
new_sheet = wb.create_sheet('NewSheet')
new_sheet['A1'] = 'Data'

wb.save('modified.xlsx')
```

### pandas数据分析示例
```python
import pandas as pd

# Read Excel
df = pd.read_excel('file.xlsx')  # Default: first sheet
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets as dict

# Analyze
df.head()      # Preview data
df.info()      # Column info
df.describe()  # Statistics

# Write Excel
df.to_excel('output.xlsx', index=False)
```

---

> [!WARNING]
> 冲突：本技能仅为`xlsx`操作的自有规范，未标注与其他Excel处理技能规范的兼容性，若存在其他同名或同类技能规范可能存在格式、工作流要求分歧。
