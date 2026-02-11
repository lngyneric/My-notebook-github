---
title: RA Department AI Platform OpenSpec
version: 1.0.0
status: Draft
last_updated: 2026-01-12
authors: [RA Department]
tags: [OpenSpec, Standard, AI]
---

# OpenSpec: RA Department AI Question Answering Platform

## 1. Introduction

This document defines the technical specifications for the **RA Department AI Question Answering Platform** ("Registered Intelligence Star"). It specifies the data schemas, prompt engineering standards, and interaction protocols required to build a compliant and efficient AI assistant for regulatory affairs.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2. Terminology

*   **Knowledge Unit (KU)**: The smallest atomic unit of information in the database (e.g., a specific Q&A pair or a clause from a regulation).
*   **Staging Bot**: A personal WeCom bot used for testing prompt iterations.
*   **Prod Bot**: The enterprise-wide WeCom bot accessible to all RA staff.
*   **Hallucination**: The generation of incorrect or fabricated information by the AI model.

## 3. Data Specification

### 3.1 Tagging Taxonomy Schema

The platform MUST organize data using a hierarchical tagging system to ensure precise retrieval.

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

### 3.2 Knowledge Unit Structure

Each KU imported into the system MUST follow this JSON structure:

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

## 4. Prompt Engineering Specification

### 4.1 System Prompt Constraints

The System Prompt MUST include the following constraint blocks:

#### 4.1.1 Boundary Definition
```text
YOU MUST ONLY answer based on the provided context.
IF the information is not present in the context:
  YOU MUST reply: "Based on current regulations, I cannot find relevant information."
  YOU MUST NOT fabricate or infer answers.
```

#### 4.1.2 Output Formatting Rules
*   **Classification Codes**: MUST match regex `^\d{4}-\d{2}-\d{5}$`.
    *   *Incorrect*: "6840"
    *   *Correct*: "6840-10-10022"
*   **Citations**: MUST include the source document title when providing regulatory advice.

#### 4.1.3 Disambiguation Logic
The prompt SHOULD contain logic to handle ambiguous queries:
```text
IF user query implies "Product Performance Evaluation":
  CHECK product type:
  - CASE "Quantitative": Refer to "IVD Performance Evaluation Guideline - Chapter 3"
  - CASE "Qualitative": Refer to "Rapid Diagnostic Reagent Guideline - Section 2.4"
```

## 5. Interaction Protocol

### 5.1 Query Processing Flow

1.  **Input Analysis**: System receives user query.
2.  **Intent Recognition**:
    *   Extract entities (Product Name, Regulation Type).
    *   Map to Tag Taxonomy.
3.  **Context Retrieval**: Retrieve Top-K KUs based on semantic similarity + Tag filtering.
4.  **Response Generation**: LLM generates response using System Prompt + Retrieved Context.
5.  **Output Validation**: Check against Formatting Rules (4.1.2).

### 5.2 Error Handling

*   **Ambiguity**: If multiple product types are detected, the system MUST ask clarifying questions.
*   **No Match**: If similarity score < Threshold (e.g., 0.75), return fallback message and log for review.

## 6. Maintenance & Operations

### 6.1 Batch Update Workflow

1.  **Generation**: Use AI tools to generate `similar_questions` for new KUs.
    *   *Constraint*: At least 2 variations MUST be in colloquial "RA Specialist" tone.
2.  **Review**: RA Experts MUST review generated questions for semantic accuracy.
3.  **Deployment**:
    *   Deploy to Staging Bot.
    *   Run Regression Test (check against Golden Dataset).
    *   Promote to Prod Bot.

### 6.2 Quality Assurance Metrics

*   **Accuracy Rate**: (Correct Answers / Total Queries) > 95%
*   **Hallucination Rate**: (Fabricated Answers / Total Queries) < 0.1%
*   **Response Time**: < 3 seconds (P95)

## 7. Security & Compliance

*   **Data Privacy**: NO sensitive project data (e.g., unreleased product details) SHALL be used in training/context without anonymization.
*   **Audit Trail**: All queries and answers MUST be logged for 30 days to support compliance audits.
