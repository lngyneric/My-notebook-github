---
source: raw/04_文档与参考/Markdown文档/RA_AI_Platform.openspec.md
raw_sha256: 2e11ba81293b3c8a1334bdfcfeb34fc13ef58c314f4293af22799411f59cad49
compiled_at: 2026-04-24T06:11:53.949Z
---
# OpenSpec: RA Department AI Question Answering Platform
## Metadata
| Field | Value |
|-------|-------|
| Version | 1.0.0 |
| Status | Draft |
| Last Updated | 2026-01-12 |
| Authors | RA Department |
| Tags | OpenSpec, Standard, AI |

## Summary
This open specification defines the full technical requirements for the RA Department AI Question Answering Platform (internal name: "Registered Intelligence Star"), a compliant AI assistant for regulatory affairs use cases. It covers data schemas, prompt engineering standards, interaction protocols, maintenance workflows, and security compliance rules for implementation.

## Requirement Conventions
All requirement-level keywords ("MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL") in this specification are interpreted per the definitions in RFC 2119.

## 1. Core Terminology
All terms follow the definitions below for consistent interpretation across implementations:
- **Knowledge Unit (KU)**: The smallest atomic unit of information in the platform database (e.g., a specific Q&A pair or a clause from a regulation).
- **Staging Bot**: A personal WeCom bot used for testing prompt iterations and pre-production validations.
- **Prod Bot**: The enterprise-wide production WeCom bot accessible to all RA staff.
- **Hallucination**: The generation of incorrect or fabricated information by the AI model.

## 2. Data Specifications
### 2.1 Tagging Taxonomy Schema
The platform MUST use a 3-level hierarchical tagging system to enable precise data retrieval, defined as follows:
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

### 2.2 Knowledge Unit (KU) Structure
All KUs imported into the system MUST conform to the following JSON schema:
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

## 3. Prompt Engineering Specifications
The platform's System Prompt MUST include the following mandatory constraint blocks:
### 3.1 Boundary Definition
```text
YOU MUST ONLY answer based on the provided context.
IF the information is not present in the context:
  YOU MUST reply: "Based on current regulations, I cannot find relevant information."
  YOU MUST NOT fabricate or infer answers.
```

### 3.2 Output Formatting Rules
- **Classification Codes**: MUST match the regex `^\d{4}-\d{2}-\d{5}$` (e.g., valid: `6840-10-10022`, invalid: `6840`).
- **Citations**: MUST include the full source document title for all regulatory advice responses.

### 3.3 Disambiguation Logic
The System Prompt SHOULD include conditional logic to resolve ambiguous queries, for example:
```text
IF user query implies "Product Performance Evaluation":
  CHECK product type:
  - CASE "Quantitative": Refer to "IVD Performance Evaluation Guideline - Chapter 3"
  - CASE "Qualitative": Refer to "Rapid Diagnostic Reagent Guideline - Section 2.4"
```

## 4. Interaction Protocol
### 4.1 Query Processing Flow
All user queries are processed via the following 5-step workflow:
1. **Input Analysis**: Receive and parse raw user query.
2. **Intent Recognition**: Extract entities (Product Name, Regulation Type) and map to the Tag Taxonomy.
3. **Context Retrieval**: Retrieve Top-K matching KUs using combined semantic similarity scoring and tag filtering.
4. **Response Generation**: LLM generates responses using the approved System Prompt and retrieved context.
5. **Output Validation**: Verify response compliance against the Output Formatting Rules defined in Section 3.2.

### 4.2 Error Handling
- **Ambiguity Handling**: If multiple product types are detected in a single query, the system MUST ask the user clarifying questions.
- **No Match Handling**: If the highest KU similarity score is below the defined threshold (e.g., 0.75), return the standard fallback message and log the query for manual review.

## 5. Maintenance & Operations
### 5.1 Batch KU Update Workflow
New or updated KUs follow this mandatory deployment process:
1. **Generation**: Use AI tools to generate `similar_questions` for new KUs, with a requirement of at least 2 variations in a colloquial "RA Specialist" tone.
2. **Review**: RA domain experts MUST review all generated content for semantic and regulatory accuracy.
3. **Deployment**:
   1. Deploy updated KUs and prompts to the Staging Bot.
   2. Execute regression testing against the platform's Golden Dataset.
   3. Promote validated changes to the Prod Bot.

### 5.2 Quality Assurance (QA) Metrics
The platform MUST meet the following minimum performance thresholds:
- **Accuracy Rate**: ≥ 95% (calculated as Correct Answers / Total Queries)
- **Hallucination Rate**: ≤ 0.1% (calculated as Fabricated Answers / Total Queries)
- **Response Time**: < 3 seconds (P95 percentile)

## 6. Security & Compliance
- **Data Privacy**: No sensitive project data (e.g., unreleased product details) SHALL be used for model training or included in retrieval context without full anonymization.
- **Audit Trail**: All user queries and system responses MUST be logged for a minimum of 30 days to support regulatory compliance audits.
