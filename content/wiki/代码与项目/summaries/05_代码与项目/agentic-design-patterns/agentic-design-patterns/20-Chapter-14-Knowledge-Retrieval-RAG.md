---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/20-Chapter-14-Knowledge-Retrieval-RAG.md
raw_sha256: 2f933d5223429ea3de1baf2fe89cee207d20d9f4970d0886e4f579b553a27d08
compiled_at: 2026-04-24T07:49:07.223Z
---
<wiki>
# Chapter 14: Knowledge Retrieval (RAG) | <mark>第 14 章：知识检索（RAG）</mark>
[[19-Chapter-13-Human-in-the-Loop|< Previous Chapter]] | [[000-Home|Home]] | [[21-Chapter-15-Inter-Agent-Communication|Next Chapter >]]

## 摘要
LLMs exhibit substantial capabilities in generating human-like text, but their knowledge base is confined to static training data, limiting access to real-time, proprietary, or specialized information. Knowledge Retrieval (RAG, or Retrieval Augmented Generation) addresses this limitation by enabling LLMs to access and integrate external, current, context-specific information, enhancing output accuracy, relevance, and factual basis. For AI agents, RAG grounds actions and responses in verifiable real-time data, transforming them from simple conversationalists into effective data-driven tools for complex tasks.
<mark>大语言模型（LLM）在生成类人文本方面表现出强大的能力，但其知识库受限于静态训练数据，无法获取实时、专有或高度专业化的信息。知识检索（RAG，即检索增强生成）通过使LLM能够访问并整合外部的、最新的、特定上下文的信息解决了这一局限，从而增强其输出的准确性、相关性和事实基础。对于AI智能体而言，RAG将其行动和响应建立在可验证的实时数据之上，将其从简单的对话者转变为可执行复杂任务的高效数据驱动工具。</mark>

---
## Knowledge Retrieval (RAG) Pattern Overview | <mark>知识检索（RAG）模式概述</mark>
The Knowledge Retrieval (RAG) pattern enhances LLM capabilities by granting access to external knowledge bases before response generation. Instead of relying solely on pre-trained internal knowledge, RAG allows LLMs to "look up" information like humans consulting references, enabling more accurate, up-to-date, verifiable answers.
<mark>知识检索（RAG）模式通过在生成响应前授予LLM访问外部知识库的权限，从而显著增强其能力。RAG允许LLM「查找」信息，而非仅依赖内部预训练知识，就像人类查阅参考资料一样，使其能够提供更准确、最新且可验证的答案。</mark>

### Core Workflow
When a user submits a query to a RAG-enabled AI system:
1. The query is not sent directly to the LLM; instead, the system first performs a semantic search of a structured external knowledge base (documents, databases, web pages) to understand user intent beyond simple keyword matching.
2. The most relevant information snippets ("chunks") are extracted.
3. These chunks are augmented to the original prompt to create a context-rich query.
4. The enhanced prompt is sent to the LLM, which generates a fluent, factually grounded response.
<mark>当用户向带RAG的AI系统提出查询时：
1. 查询不会直接发送给LLM，系统首先对结构化外部知识库（文档、数据库、网页）执行语义搜索，超越简单关键词匹配理解用户意图。
2. 提取最相关的信息片段（「信息块」）。
3. 将这些信息块增强到原始提示词中，创建内容丰富的上下文查询。
4. 增强后的提示词发送给LLM，生成流畅、有事实依据的响应。</mark>

### Key Benefits
- Access to up-to-date information, overcoming static training data constraints
- Reduced risk of "hallucination" (false information generation) by grounding responses in verifiable data
- Support for specialized knowledge from internal company documents/wikis
- Ability to provide citations for information sources, enhancing response trustworthiness and verifiability
<mark>RAG框架的核心优势：
- 可访问最新信息，克服静态训练数据的限制
- 通过将响应建立在可验证数据基础上，降低「幻觉」（生成虚假信息）的风险
- 支持使用公司内部文档或wiki中的专业知识
- 可提供信息来源的引用，增强AI响应的可信度和可验证性</mark>

---
## Core RAG Concepts | <mark>RAG核心概念</mark>
To understand RAG functionality, the following core concepts are foundational:

### Embeddings | <mark>嵌入</mark>
In the context of LLMs, embeddings are numerical vector representations of text (words, phrases, entire documents) designed to capture semantic meaning and relationships between text pieces in a mathematical space. Text with similar meanings has embeddings that are closer in the vector space; while simple examples use 2D coordinates, real-world embeddings use hundreds to thousands of dimensions for nuanced language understanding.
<mark>在LLM的语境中，嵌入是文本（词语、短语、整个文档）的数值向量表示，用于在数学空间中捕捉不同文本片段之间的语义含义和关系。含义相近的文本，其嵌入在向量空间中的距离更近；简单示例使用二维坐标，实际应用中的嵌入拥有数百到数千个维度，以实现对语言的细致理解。</mark>

### Text Similarity | <mark>文本相似度</mark>
Text similarity is a measure of how alike two pieces of text are, ranging from surface-level lexical similarity (word overlap) to deeper meaning-based similarity. It is critical for finding relevant knowledge base content matching user queries in RAG systems. For example, two differently worded questions asking for France's capital will receive a high similarity score from effective models, calculated using text embeddings.
<mark>文本相似度是衡量两段文本相似程度的指标，可分为表层的词汇相似度（词语重叠）和更深层次的基于含义的相似度。RAG系统中，文本相似度对于在知识库中找到与用户查询最相关的信息至关重要。例如，两个措辞不同但均询问法国首都的问题，会被有效模型赋予很高的相似度得分，这通常通过计算文本嵌入实现。</mark>

### Semantic Similarity and Distance | <mark>语义相似度与距离</mark>
Semantic similarity is an advanced text similarity form focused purely on text meaning and context, rather than wording, to determine if two pieces of text convey the same concept. Semantic distance is the inverse: high semantic similarity implies low semantic distance, and vice versa. RAG semantic search relies on finding documents with the smallest semantic distance to user queries, enabling "smart search" that finds relevant content even when user wording does not match knowledge base text exactly.
<mark>语义相似度是一种更高级的文本相似度形式，纯粹关注文本的含义和上下文而非措辞，用于判断两段文本是否传达相同的概念。语义距离与语义相似度相反：高语义相似度意味着低语义距离，反之亦然。RAG的语义搜索依赖于找到与用户查询语义距离最小的文档，实现「智能搜索」，即使用户措辞与知识库文本不完全匹配，也能找到相关内容。</mark>

![](images/chapter14_fig1.png "RAG Core Concepts")
Fig.1: RAG Core Concepts: Chunking, Embeddings, and Vector Database
<mark><strong>图 1：</strong>RAG 核心概念：分块、嵌入和向量数据库</mark>

### Chunking of Documents | <mark>文档分块</mark>
Chunking is the process of breaking large documents into smaller, manageable pieces ("chunks") to enable efficient RAG operation, as entire large documents cannot be fed to LLMs. Chunking strategy is critical for preserving information context and meaning: for example, a 50-page user manual may be split into sections like "Troubleshooting" and "Installation Guide" as separate chunks, allowing retrieval of only relevant content for user queries, improving speed and relevance.
<mark>分块是将大型文档分解成更小、更易于管理的片段（「块」）的过程，以实现RAG系统的高效运行，因为完整的大型文档无法直接输入给LLM。分块策略对于保留信息的上下文和含义非常重要：例如，一份50页的用户手册可被拆分为「故障排除」「安装指南」等独立块，仅检索与用户查询相关的内容，提升速度和相关性。</mark>

### Retrieval Techniques | <mark>检索技术</mark>
After document chunking, RAG systems use retrieval techniques to find the most relevant chunks:
1. **Vector Search**: The primary method, using embeddings and semantic distance to find conceptually similar chunks to user queries.
2. **BM25**: An older but valuable keyword-based algorithm that ranks chunks by term frequency, without semantic understanding.
3. **Hybrid Search**: Combines BM25's keyword precision with semantic search's contextual understanding to capture both literal matches and conceptual relevance for more robust results.
<mark>文档分块后，RAG系统采用以下检索技术查找最相关的片段：
1. **向量搜索**：主要方法，利用嵌入和语义距离查找与用户问题概念相似的块。
2. **BM25**：较早但仍有价值的基于关键字的算法，根据词频对块排序，不具备语义理解能力。
3. **混合搜索**：结合BM25的关键字精度与语义搜索的上下文理解，同时捕捉字面匹配和概念相关性
