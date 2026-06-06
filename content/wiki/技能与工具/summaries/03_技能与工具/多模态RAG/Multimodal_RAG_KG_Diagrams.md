---
source: raw/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Diagrams.md
raw_sha256: 7b2e0e0fb7156d2b734467dfeb22a4cf289348c2265f1ad963f1bd0934128af7
compiled_at: 2026-04-24T05:35:47.750Z
---
# Multimodal RAG & Knowledge Graph Construction Diagrams
## Metadata
- Date: 2026-01-14
- Tags: Mermaid, Architecture, RAG, KG

## Summary
This document provides structured Mermaid architecture diagrams for two core multimodal AI workflows: a composable four-stage multimodal Retrieval-Augmented Generation (RAG) pipeline, and the OntoMetric end-to-end Knowledge Graph (KG) construction pipeline with dual-phase quality verification.

## 1. Composable Multimodal RAG Architecture
This diagram illustrates a modular four-stage pipeline for multimodal RAG, with configurable strategies and components at each phase:
1. **Pre-retrieval (Indexing)**: Processes raw multimodal data via organization strategies (single-modal embedding, pairwise storage, unified embedding, graph construction) to build vector or graph indexes.
2. **Retrieval**: Optimizes user queries (via expansion or modality transformation) and selects retrieval methods (sparse/BM25, dense/CLIP, hybrid) to return relevant context.
3. **Augmentation**: Refines retrieved context via reranking, compression, and fusion strategies (encoder fusion/FiE, decoder fusion/FiD).
4. **Generation**: Selects appropriate generators (LLM for text, LVM for images, LMM for multimodal output) to produce the final response.

```mermaid
graph TD
    %% Define Styles
    classDef pre fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef ret fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef aug fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;
    classDef gen fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;

    subgraph PreRetrieval ["Phase 1: Pre-retrieval (Indexing)"]
        direction TB
        Input[Raw Multimodal Data] --> Split{Organization Strategy}
        Split -->|Single| Embed1[Single-modal Embedding]
        Split -->|Pair| Embed2[Pairwise Storage]
        Split -->|Unified| Embed3[Unified Embedding]
        Split -->|Graph| Embed4[Graph Construction]
        Embed1 & Embed2 & Embed3 & Embed4 --> Index[Vector/Graph Index]
    end
    class Input,Split,Embed1,Embed2,Embed3,Embed4,Index pre;

    subgraph Retrieval ["Phase 2: Retrieval"]
        direction TB
        Query[User Query] --> Optimize[Query Optimization]
        Optimize -->|Expansion| Q_Exp[Query Expansion]
        Optimize -->|Transform| Q_Trans[Modality Transform]
        
        Q_Exp & Q_Trans --> Retriever{Retriever Selection}
        Retriever -->|BM25| Sparse[Sparse Retrieval]
        Retriever -->|CLIP| Dense[Dense Retrieval]
        Retriever -->|Hybrid| Hybrid[Hybrid Retrieval]
        
        Sparse & Dense & Hybrid --> Results[Retrieved Context]
    end
    class Query,Optimize,Q_Exp,Q_Trans,Retriever,Sparse,Dense,Hybrid,Results ret;

    subgraph Augmentation ["Phase 3: Augmentation"]
        direction TB
        Results --> Rerank[Reranking]
        Rerank --> Compress[Compression/Selection]
        Compress --> Fusion{Fusion Strategy}
        Fusion -->|FiE| EncFuse[Encoder Fusion]
        Fusion -->|FiD| DecFuse[Decoder Fusion]
    end
    class Rerank,Compress,Fusion,EncFuse,DecFuse aug;

    subgraph Generation ["Phase 4: Generation"]
        direction TB
        EncFuse & DecFuse --> Generator{Generator Selection}
        Generator -->|LLM| TextGen[Text Gen (GPT-4)]
        Generator -->|LVM| ImgGen[Image Gen (SD)]
        Generator -->|LMM| MultiGen[Multimodal Gen (Gemini)]
        
        TextGen & ImgGen & MultiGen --> FinalOutput[Final Response]
    end
    class Generator,TextGen,ImgGen,MultiGen,FinalOutput gen;

    Index -.-> Results
```

## 2. OntoMetric Knowledge Graph Construction Pipeline
This diagram visualizes a three-stage "Segmentation-Extraction-Verification" workflow for building high-quality knowledge graphs from long structured documents:
1. **Segmentation**: Applies structure-aware segmentation (TOC analysis, table merging) to split input documents into semantically coherent chunks with preserved structure.
2. **Extraction**: Uses an LLM extractor guided by a pre-defined ontology schema to extract raw JSON triples from chunks.
3. **Verification**: Runs dual-phase validation (LLM-powered semantic check, rule-based schema check) to filter invalid triples before building the final KG.

```mermaid
graph LR
    %% Define Styles
    classDef process fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef artifact fill:#e0f7fa,stroke:#006064,stroke-width:2px,stroke-dasharray: 5 5;
    classDef verify fill:#ffcdd2,stroke:#c62828,stroke-width:2px;

    Doc[Long Document (PDF/Report)] --> Seg[Structure-Aware Segmentation]
    class Doc artifact;
    class Seg process;

    subgraph Segmentation ["Stage 1: Segmentation"]
        Seg -->|TOC Analysis| Chunk1[Chunk 1: Metadata + Content]
        Seg -->|Table Merge| Chunk2[Chunk 2: Merged Table]
    end
    class Chunk1,Chunk2 artifact;

    subgraph Extraction ["Stage 2: Extraction"]
        Ontology[Ontology Schema] -.-> LLM[LLM Extractor]
        Chunk1 & Chunk2 --> LLM
        LLM -->|Prompt Engineering| RawKG[Raw JSON Triples]
    end
    class Ontology artifact;
    class LLM process;
    class RawKG artifact;

    subgraph Verification ["Stage 3: Dual-Phase Verification"]
        RawKG --> SemVer{Phase 1: Semantic Verification}
        SemVer -->|LLM Check| ValidSem[Semantically Valid]
        SemVer -->|Reject| Discard1[Discard/Retry]
        
        ValidSem --> SchemaVer{Phase 2: Schema Verification}
        SchemaVer -->|Rule Check| ValidFinal[Verified Triples]
        SchemaVer -->|Reject| Discard2[Discard]
    end
    class SemVer,SchemaVer verify;
    class ValidSem,ValidFinal,Discard1,Discard2 artifact;

    ValidFinal --> KG[Final Knowledge Graph]
    class KG artifact;
```
