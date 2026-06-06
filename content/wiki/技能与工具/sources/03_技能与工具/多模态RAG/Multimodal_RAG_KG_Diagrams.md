---
source: raw/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Diagrams.md
raw_sha256: 7b2e0e0fb7156d2b734467dfeb22a4cf289348c2265f1ad963f1bd0934128af7
compiled_at: 2026-04-14T03:54:57.865Z
---
> [!INFO]
> 来源路径：`raw/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Diagrams.md`
> 原始资料未修改，无已知冲突

# Multimodal RAG & 知识图谱架构图
## TL;DR
本文提供了两个可复用的Mermaid架构图，分别为可组合多模态RAG的四阶段流水线架构，以及高质量知识图谱构建的「分段-抽取-验证」三段式工作流，可用于架构设计参考与方案展示。

## 要点
1. 可组合多模态RAG架构分为四个标准阶段：预检索（索引）、检索、增强、生成
2. 预检索阶段支持单模态嵌入、成对存储、统一嵌入、图构建四种不同的组织策略，最终生成向量/图索引
3. 检索阶段先对用户查询做扩展或模态变换，再根据场景选择稀疏、稠密或混合检索，得到检索上下文
4. 增强阶段对检索结果做重排序、压缩选择后，支持编码器融合（FiE）、解码器融合（FiD）两种融合策略
5. 生成阶段可根据输出需求选择LLM做文本生成、LVM做图像生成、LMM做多模态生成
6. OntoMetric高质量知识图谱构建采用「分段-抽取-验证」三段流水线：结构感知分段→LLM基于本体抽取→两阶段验证（语义验证+ schema验证）

## 引用证据片段
### 1 可组合多模态RAG架构
该图展示了包含预检索、检索、增强、生成四个阶段的流水线：

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

### 2 OntoMetric 知识图谱构建流水线
该图可视化了高质量知识图谱构建的「分段-抽取-验证」工作流：

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

## 冲突记录
无已知冲突。
