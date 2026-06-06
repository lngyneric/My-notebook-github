---
source: raw/04_文档与参考/Markdown文档/RA_AI_Platform.openspec.md
raw_sha256: 2e11ba81293b3c8a1334bdfcfeb34fc13ef58c314f4293af22799411f59cad49
compiled_at: 2026-04-14T03:52:36.591Z
---
> [!INFO]
> 来源路径：`raw/04_文档与参考/Markdown文档/RA_AI_Platform.openspec.md`
> 元数据：版本 `1.0.0` | 状态 `Draft` | 最后更新 `2026-01-12` | 作者 `RA Department` | 标签 `OpenSpec, Standard, AI`

# RA 部门AI问答平台开放规范（RA Department AI Question Answering Platform OpenSpec）

## TL;DR
本文档是**注册事务(RA)部门AI问答平台（代号Registered Intelligence Star）**的开放技术规范，定义了合规高效的RA AI助手所需满足的数据 schema、提示工程标准和交互协议，可用于指导平台开发、知识录入与运维。本文档中关键术语「MUST」「MUST NOT」「REQUIRED」「SHALL」「SHALL NOT」「SHOULD」「SHOULD NOT」「RECOMMENDED」「MAY」「OPTIONAL」遵循RFC 2119定义。

## 要点

### 术语定义
| 术语 | 定义 |
|------|------|
| Knowledge Unit (KU) | 数据库中最小的原子信息单元，例如特定问答对、法规条款 |
| Staging Bot | 用于测试提示迭代的个人企业微信机器人 |
| Prod Bot | 全RA部门员工可访问的企业级企业微信机器人 |
| Hallucination | AI模型生成错误或捏造信息的行为 |

### 数据规范
1. 必须使用三级分层标签体系组织数据，标签分类如下：
   - Level 1：`Product_Type`，可选值：`Reagent (试剂类)`/`Instrument (仪器类)`，根据产品名称关键词划分
   - Level 2：`Regulation_Type`，可选值：`General_Guideline (通用指导原则)`/`Specific_Guideline (专用指导原则)`
   - Level 3：`Scenario`，可选值：`Registration (注册申报)`/`Modification (变更备案)`/`Clinical_Evaluation (临床评价)`
2. 每个知识单元(KU)必须遵循标准JSON结构，包含ID、标准问题、标准答案、标签、来源信息、相似问题变体

### 提示工程规范
1. 系统提示必须包含三类约束块：
   - 边界约束：只能基于提供的上下文回答，无相关信息必须回复固定话术禁止编造
   - 输出格式约束：分类编码必须符合`^\d{4}-\d{2}-\d{5}$`正则格式，提供法规建议必须引用来源文档标题
   - 消歧逻辑：建议包含歧义查询处理逻辑，例如对不同类型产品性能评价对应不同法规依据
2. 歧义处理：如果检测到多个产品类型，必须向用户提问澄清

### 交互协议
查询处理流程：输入分析 → 意图识别（实体抽取+标签映射） → 上下文检索（语义相似度+标签过滤取Top-K） → LLM生成回答 → 输出格式校验
错误处理：
- 歧义：必须要求用户澄清
- 无匹配：相似度低于阈值（示例0.75）返回兜底消息并记录待复审

### 运维规范
批量更新流程：AI生成相似问题 → RA专家人工审核 → 部署到测试机器人 → 回归测试 → 升级到生产机器人
质量要求：准确率>95%、幻觉率<0.1%、P95响应时间<3秒

### 安全合规
- 未脱敏的敏感项目数据（例如未发布产品细节）不得用于训练或上下文
- 所有查询和回答必须记录日志至少30天，支持合规审计

## 引用证据片段

### 分层标签体系原始定义
```yaml
taxonomy:
  level_1:
    name: Product_Type
    values:
      - Reagent (试剂类)
      - Instrument (仪器类)
    logic: "Based on product name keywords (e.g., 'kit' -> Reagent, 'analyzer' -> Instrument)"

  level_2:
    name: Regulation_Type
    values:
      - General_Guideline (通用指导原则)
      - Specific_Guideline (专用指导原则)

  level_3:
    name: Scenario
    values:
      - Registration (注册申报)
      - Modification (变更备案)
      - Clinical_Evaluation (临床评价)
```

### 知识单元(KU)标准结构
```json
{
  "id": "UUID",
  "question": "Standard Question String",
  "answer": "Standard Answer Markdown String",
  "tags": ["Level1_Value", "Level2_Value", "Level3_Value"],
  "source": {
    "document_name": "Name of the source regulation",
    "clause_id": "Section/Article number",
    "effective_date": "YYYY-MM-DD"
  },
  "similar_questions": [
    "Variation 1",
    "Variation 2 (Colloquial)"
  ]
}
```

### 系统提示边界约束原文
```text
YOU MUST ONLY answer based on the provided context.
IF the information is not present in the context:
  YOU MUST reply: "Based on current regulations, I cannot find relevant information."
  YOU MUST NOT fabricate or infer answers.
```

### 消歧逻辑示例原文
```text
IF user query implies "Product Performance Evaluation":
  CHECK product type:
  - CASE "Quantitative": Refer to "IVD Performance Evaluation Guideline - Chapter 3"
  - CASE "Qualitative": Refer to "Rapid Diagnostic Reagent Guideline - Section 2.4"
```

## 冲突标注
当前文档为草稿版本，暂无其他来源交叉验证，无已知冲突。
