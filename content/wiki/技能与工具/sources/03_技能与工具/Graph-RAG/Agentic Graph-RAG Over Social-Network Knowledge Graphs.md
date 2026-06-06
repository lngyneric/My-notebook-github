---
source: raw/03_技能与工具/Graph-RAG/Agentic Graph-RAG Over Social-Network Knowledge Graphs.md
raw_sha256: 8790c8c7fbcf03c69d9782748b952ea6bc23d96a78e61bbe72281ace18b348ba
compiled_at: 2026-04-14T03:54:46.179Z
---
# Agentic Graph-RAG Over Social-Network Knowledge Graphs
> 来源路径：`raw/03_技能与工具/Graph-RAG/Agentic Graph-RAG Over Social-Network Knowledge Graphs.md`

---

## TL;DR
本项目是面向社交网络影响力分析的智能图检索增强生成（Agentic Graph-RAG）实践，将传统RAG的文档级检索升级为子图级检索，结合图卷积网络（GCN）学习的影响力排序模型与LangGraph编排的多步智能代理工作流，可针对自然语言查询识别社交网络中的高影响力节点并输出可解释的 outreach 推荐，相比纯文本RAG能更好利用社交网络的结构、拓扑、多路径传播特性。

---

## 核心要点
### 核心思想
传统基于向量搜索的RAG忽略社交网络的关系结构、社区拓扑、影响力传播的多跳路径，本方案将图结构直接融入检索过程：
1. 从文档级检索升级为**图感知的子图检索**，捕获连通性、中心性、跨社区交互等结构信号
2. 用GCN学习影响力排序，替代纯规则排序，融合节点局部属性与全局图结构
3. 用LangGraph编排多步智能代理工作流，实现规划→检索→打分→生成的端到端推理

### 数据集
使用经过预处理的公开MUSAE Facebook Page-Page网络：
- 包含超过22000个节点（Facebook Page）、30多万条有向关注边
- 节点属性包含：页面主题、粉丝数、近期发文量等信息

### 技术流程
| 阶段 | 核心动作 |
|------|----------|
| 图构建 | 基于CSV数据用NetworkX构建有向社交网络知识图，存储节点属性与边关系 |
| 特征工程 | 为每个节点提取7类特征：PageRank、入度、出度、k-core值、聚类系数、30天发文量、查询主题相似度，归一化后用于GCN训练 |
| GCN训练 | 采用两层GCN架构，用成对排序损失训练，学习节点的相对影响力排序（而非绝对分类） |
| 智能代理流程 | 1. `plan`：解析自然语言查询提取主题<br>2. `retrieve`：从主题匹配种子节点扩展k跳邻居提取相关子图<br>3. `score`：用训练好的GCN对子图内节点打分排序<br>4. `synthesize`：将排序后的节点信息输入LLM生成结构化总结与可操作推荐 |

### 能力输出
最终系统可实现：针对自然语言查询，识别高影响力节点、解释节点影响力的结构依据、生成简洁可操作的 outreach 推荐。

---

## 引用证据片段（完整实验代码）
<details>
<summary>依赖安装</summary>

```python
%pip -q install langgraph pydantic pandas networkx matplotlib tqdm scipy openai
%pip -q install torch==2.8.0+cpu torchvision==0.23.0+cpu torchaudio==2.8.0+cpu --index-url https://download.pytorch.org/whl/cpu
%pip -q install torch_geometric==2.6.1

print("✅ Dependencies installed (you may restart the kernel if needed).")
```
</details>

<details>
<summary>导入与可复现性配置</summary>

```python
import os, json, random
from pathlib import Path
from typing import TypedDict, Dict, Any, Tuple, List

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm

import torch, torch.nn as nn, torch.nn.functional as F
from torch_geometric.utils import from_networkx as pyg_from_nx, add_self_loops
from torch_geometric.nn import GCNConv

from langgraph.graph import StateGraph, START, END
from openai import OpenAI

# Reproducibility
SEED = 42
os.environ["PYTHONHASHSEED"] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.use_deterministic_algorithms(True)

device = torch.device("cpu")  # keep CPU for reproducibility
plt.rcParams["figure.figsize"] = (8, 6)

print("✅ Imports complete | Using device:", device)
```
</details>

<details>
<summary>数据加载与图构建</summary>

```python
# Config
USERS_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/GSNJkoEM3yeeCjJl1l2Jrg/users.csv"
EDGES_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/m9iBI6GCId0XoGEkjwHk3g/edges-follow.csv"

CUR = Path("data/curated"); CUR.mkdir(parents=True, exist_ok=True)
USERS_CSV = CUR / "users.csv"
EDGES_CSV = CUR / "edges_follow.csv"

# download only if missing
if not USERS_CSV.exists():
    pd.read_csv(USERS_URL).to_csv(USERS_CSV, index=False)
if not EDGES_CSV.exists():
    pd.read_csv(EDGES_URL).to_csv(EDGES_CSV, index=False)

df_users = pd.read_csv(USERS_CSV)
df_edges = pd.read_csv(EDGES_CSV)
display(df_users.head(3))
display(df_edges.head(3))
print(f"✅ users={len(df_users):,} | edges={len(df_edges):,}")

# OpenAI API校验
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
assert os.getenv("OPENAI_API_KEY"), "Set OPENAI_API_KEY in your environment."
print("✅ OpenAI model:", OPENAI_MODEL)

# 主题归一化处理
def _topics_field(v):
    if isinstance(v, list): return [str(x).lower() for x in v]
    if isinstance(v, str) and v.startswith("["):
        try: return [str(x).lower() for x in json.loads(v)]
        except Exception: pass
    return [t.strip().lower() for t in str(v).split("|") if t.strip()]

df_users["topics"] = df_users["topics"].apply(_topics_field)

# 构建NetworkX有向图
def build_graph(users_df: pd.DataFrame, edges_df: pd.DataFrame) -> Tuple[nx.DiGraph, pd.DataFrame]:
    G = nx.DiGraph()
    for _, r in users_df.iterrows():
        G.add_node(
            r["login"],
            **dict(
                name=r.get("name") or r["login"],
                company=str(r.get("company", "")),
                followers=int(r.get("followers", 0)),
                following=int(r.get("following", 0)),
                posts_30d=int(r.get("posts_30d", 0)),
                topics=r.get("topics", []),
                bio=str(r.get("bio", "")),
            )
        )
    for _, e in edges_df.iterrows():
        s, d = e["src"], e["dst"]
        if s in G and d in G and s != d:
            G.add_edge(s, d, etype=e.get("etype","FOLLOW"))
    
    return G, users_df

G, users_df = build_graph(df_users, df_edges)
print(f"[graph] |V|={G.number_of_nodes()} |E|={G.number_of_edges()}")
print("Is DAG? ", nx.is_directed_acyclic_graph(G))
print("Weakly connected components:", nx.number_weakly_connected_components(G))
```
</details>

<details>
<summary>特征工程与目标构建</summary>

```python
# 工具函数：主题向量与余弦相似度
def topic_vector(ts, vocab):
    v = np.zeros(len(vocab), dtype=np.float32)
    idx = {t:i for i,t in enumerate(vocab)}
    for t in ts:
        if t in idx: v[idx[t]] = 1.0
    return v

def cosine(a,b):
    na,nb = np.linalg.norm(a), np.linalg.norm(b)
    return 0.0 if na==0 or nb==0 else float(np.dot(a,b)/(na*nb))

# 生成节点特征
def make_features(G: nx.DiGraph, qtopics=None, normalize=True):
    vocab = sorted({t for _, d in G.nodes(data=True) for
