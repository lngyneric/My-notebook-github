<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>



```python
# **Agentic Graph-RAG Over Social-Network Knowledge Graphs**

```

Estimated time needed: **60** minutes


## Introduction

Understanding **influence** and **information flow** in social networks requires more than retrieving text snippets or isolated documents. Traditional **Retrieval-Augmented Generation (RAG)** pipelines rely on **vector search** over unstructured text, which works well for semantic similarity but ignores **relational structure**, **community topology**, and the **multi-hop pathways** through which influence spreads. To analyze a social graph meaningfully, an AI system may incorporate **graph structure** directly into the retrieval process.

This lab introduces an extended **Graph-RAG** approach: instead of retrieving documents, the agent retrieves **subgraphs**, neighborhoods of users connected by follow relationships, and treats these graph fragments as the context for downstream reasoning. This shift from document-level retrieval to **graph-aware retrieval** enables the system to capture richer signals such as **connectivity**, **centrality**, and **cross-community interactions**.

The dataset used in this lab is a curated **Facebook Page–Page network** originally derived from the public **MUSAE Facebook dataset**, with additional attributes prepared for **graph-based retrieval** and **influence modeling**. You will work with a real-world dataset containing **over twenty-two thousand users** and **more than three hundred thousand directed edges**, forming a dense and highly interconnected social-network graph. After constructing this graph, you will engineer a variety of **structural features**, including **PageRank**, **degree patterns**, **k-core values**, **clustering coefficients**, and **topic similarity scores**, to describe each node’s position and relevance within the network. These features are then used to train a **Graph Convolutional Network (GCN)** that learns to estimate **influence** based on both **local** and **global** graph structure. The GCN becomes a learned **ranking module** that can distinguish **high-impact users** from **peripheral users**, producing numerical **influence scores** grounded in measurable graph evidence.

Once the graph representation and GCN ranker are in place, you will integrate them into an agent built with **LangGraph**. The agent **plans** its steps, **retrieves** a meaningful subgraph in response to a natural-language query, **scores** the nodes inside that subgraph using the GCN, and **synthesizes** the results through an **LLM**. This creates a full **Agentic Graph-RAG pipeline** where **retrieval is structural**, **ranking is learned**, and **reasoning is generative**.

By the end of the lab, you will have a functioning system capable of identifying **influential nodes**, explaining **why they matter**, and generating concise, actionable **outreach recommendations**, demonstrating how **graph intelligence**, **neural modeling**, and **LLM reasoning** work together to produce deeper, more context-aware insights.


## Objectives

After completing this lab, you will be able to:

- Construct a social-network knowledge graph from CSV data and manage node attributes, directed edges, and graph connectivity using pandas and NetworkX.
- Engineer graph-based features such as PageRank, in/out degree, k-core values, clustering coefficients, and topic similarity, preparing them for use in a neural network model.
- Train and evaluate a Graph Convolutional Network (GCN) that learns to estimate influencer importance based on structural and semantic information across the graph.
- Implement a Graph-RAG retrieval module that extracts relevant neighborhoods in response to a natural-language query and integrates them into an agentic workflow.
- Build a multi-step LangGraph agent that plans, retrieves, scores with the GCN, and synthesizes an LLM-generated summary with actionable insights grounded in graph evidence.


## Overview

The agent in this lab follows a **multi-step, graph-aware reasoning pipeline** that integrates **LangGraph for planning**, **GCN-based ranking for influence estimation**, and **LLM-based synthesis for explanation and decision support**.

The diagram below summarizes the end-to-end system: **Agentic Graph-RAG (LangGraph + GCN + LLM)**.

<p style="text-align:center;">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/9-UIxRFsxZf6XdUzF8ItfQ/Graph-RAG.png"
       alt="Agentic Graph-RAG Pipeline"
       width="90%">
  <br>
  <em>Figure. Overview of the Agentic Graph-RAG Pipeline.</em>
</p>

Rather than retrieving isolated documents, the agent retrieves and reasons over **subgraphs**, allowing structural signals such as connectivity, neighborhood influence, and multi-hop relationships to directly inform the final response.

Each stage of the pipeline contributes a distinct capability:

- **User Query → PLAN**  
  LangGraph interprets the natural-language query and infers relevant high-level topics and intent.

- **PLAN → RETRIEVE**  
  A relevant subgraph is extracted from the Facebook Page–Page network by seeding topic-matched nodes and expanding through k-hop neighborhoods.

- **RETRIEVE → SCORE**  
  A trained **Graph Convolutional Network (GCN)** performs message passing over the retrieved subgraph, combining node features and neighborhood structure to produce a **relative influence score** for each node.

- **SCORE → SYNTHESIZE**  
  The LLM generates a structured summary that explains rankings and recommendations using evidence grounded in the graph.

- **SYNTHESIZE → Final Output**  
  The agent produces an actionable, human-readable response that combines graph intelligence with language-based reasoning.

This workflow highlights how **planning, graph retrieval, learned ranking, and generative synthesis** are composed into a single agentic system, forming the foundation for all experiments implemented in this lab.

## GCN-Based Influence Ranking and Modeling

To determine which nodes are most important within a retrieved subgraph, this lab uses a **Graph Convolutional Network (GCN)** as a learned influence-ranking model.

A GCN is a neural network designed to operate directly on graph-structured data. Instead of processing nodes independently, it applies **message passing** along graph edges, allowing each node to aggregate information from its neighbors. Through stacked convolution layers, nodes progressively incorporate **multi-hop structural context**, capturing relational patterns that cannot be expressed by simple heuristics such as degree or PageRank alone.

In this lab, each node is initialized with a feature vector that encodes:
- Structural properties (e.g., in-degree, out-degree, PageRank, k-core value, clustering coefficient),
- Activity signals (e.g., recent posting behavior),
- Query-dependent topic relevance.

The GCN propagates and refines node features through the graph structure, learning latent representations that capture both local and multi-hop context. During training, this propagation occurs over the full social-network graph, while at inference time it is applied to retrieved subgraphs. A final linear layer maps each node’s learned representation to a **scalar influence score**. Importantly, the GCN is used as a **ranking model rather than a classifier**. It learns to order nodes by relative influence within a subgraph, which aligns naturally with downstream tasks such as influencer identification and prioritization.

Within the Agentic Graph-RAG pipeline, the GCN serves as the bridge between retrieval and generation:
- Graph retrieval determines which portion of the network is relevant,
- The GCN determines who is most influential within that subgraph,
- The LLM explains why those nodes matter, grounding its reasoning in graph-based evidence.

This design enables influence estimation that is **learned, context-sensitive, and structurally informed**, providing a stronger foundation for agentic reasoning than purely rule-based or text-only approaches.

## From Influence Scores to Agentic Reasoning

While the GCN produces numerical influence scores, these scores alone are not the final objective. Their primary role is to **ground agentic reasoning in graph evidence**.

Within the Agentic Graph-RAG pipeline, influence scores act as an intermediate signal that guides decision-making rather than a standalone output. They determine which nodes should receive attention, prioritization, and explanation in response to a user query.

The agent uses these scores to:
- Focus reasoning on the most structurally and contextually important nodes,
- Filter noisy or peripheral parts of the graph,
- Provide the LLM with ranked, evidence-backed inputs.

The LLM then synthesizes this information into human-readable explanations, connecting influence scores to observable graph properties such as connectivity, activity, and topical relevance. This separation of responsibilities **learning influence with a GCN and explaining influence with an LLM** ensures that the final output is both **data-driven and interpretable**.

By combining learned influence modeling with agentic planning and language-based synthesis, the system moves beyond static graph analytics and enables **context-aware, query-driven reasoning over large social-network graphs**.


## Experiments

### Installing Libraries

The first step is to install all required Python libraries for this lab. This includes LangGraph for agent construction, PyTorch and PyTorch Geometric for the GCN, NetworkX for graph processing, and several utility packages.  

Run the cell below to install all dependencies. If the notebook prompts you to restart the kernel afterward, go ahead and do so to ensure all packages load correctly.



```python
%pip -q install langgraph pydantic pandas networkx matplotlib tqdm scipy openai
%pip -q install torch==2.8.0+cpu torchvision==0.23.0+cpu torchaudio==2.8.0+cpu --index-url https://download.pytorch.org/whl/cpu
%pip -q install torch_geometric==2.6.1

print("✅ Dependencies installed (you may restart the kernel if needed).")

```

### Imports and Reproducibility

Now that all dependencies are installed, we import the libraries used throughout the workflow. We also configure reproducibility by setting global random seeds for Python, NumPy, and PyTorch.  

This ensures that the executions are deterministic and repeatable across runs.



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

### Load and Explore the Social-Network Data

In this lab, we work with a curated Facebook Page–Page social graph. The dataset is derived from the public **MUSAE Facebook network**, where each node represents a Facebook page and edges represent page–page relationships. The raw MUSAE files were preprocessed into two simplified CSVs used throughout this lab. These curated files make it easier to build the Graph-RAG pipeline without running the original preprocessing steps yourself.

We will use two CSVs:
- `users.csv`: page/user attributes such as topics, activity features, and follower statistics  
- `edges_follow.csv`: directed “FOLLOW”-style edges constructed from the original MUSAE page–page links  

The code below sets up URLs to the curated versions of these files and ensures they are stored under the local `data/curated/` directory.

#### Download CSVs (if missing)

Run the cell below. If the CSVs already exist locally, the notebook will simply reuse them.

#### Load into Pandas and Inspect

Once downloaded, the CSVs are loaded into DataFrames so you can examine the first few rows and verify the structure of the Facebook-style social graph before proceeding.




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

```

### Check OpenAI Model and API Key

Next, we verify that an OpenAI API key is available. The Skills Network environment usually provides this automatically via `OPENAI_API_KEY`.  

We also set the preferred LLM model name. If the environment variable is missing, the assertion will raise an error early so you can correct it before continuing.



```python
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# This will raise an error if the key is missing, so you know to fix it early.
assert os.getenv("OPENAI_API_KEY"), "Set OPENAI_API_KEY in your environment."

print("✅ OpenAI model:", OPENAI_MODEL)

```

### Topic Preprocessing

Each user has a `topics` field describing the page’s category. However, these values may appear in several formats including:

- Python lists  
- JSON-like strings  
- Strings with separators  

The helper below normalizes all topic representations into a clean list of lowercase strings. This ensures the modules receive consistent topic fields.



```python
def _topics_field(v):
    if isinstance(v, list): return [str(x).lower() for x in v]
    if isinstance(v, str) and v.startswith("["):
        try: return [str(x).lower() for x in json.loads(v)]
        except Exception: pass
    return [t.strip().lower() for t in str(v).split("|") if t.strip()]

df_users["topics"] = df_users["topics"].apply(_topics_field)
df_users["topics"].head()

```

### Build the Social-Network Graph

Now we convert the `users.csv` and `edges_follow.csv` DataFrames into a directed NetworkX graph.  

- Each node corresponds to a Facebook page and stores attributes such as followers, posts, and assigned topics.  
- Each edge represents a directed “FOLLOW”-style relationship derived from the MUSAE page–page connections.

The resulting graph will serve as the global knowledge graph for Graph-RAG and the GCN ranker.



```python
def build_graph(users_df: pd.DataFrame, edges_df: pd.DataFrame) -> Tuple[nx.DiGraph, pd.DataFrame]:
    G = nx.DiGraph()

    # Add nodes with attributes
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

    # Add directed edges
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

### Feature Engineering for GNN

We first define helper functions for topic vectors and cosine similarity.

To train a GCN that predicts influencer importance, we need numerical feature vectors for each node. Before assembling those feature vectors, we define utility functions for topic vectors and cosine similarity, which allow us to measure topical alignment between a page and a query.



```python
def topic_vector(ts, vocab):
    v = np.zeros(len(vocab), dtype=np.float32)
    idx = {t:i for i,t in enumerate(vocab)}
    for t in ts:
        if t in idx: v[idx[t]] = 1.0
    return v

def cosine(a,b):
    na,nb = np.linalg.norm(a), np.linalg.norm(b)
    return 0.0 if na==0 or nb==0 else float(np.dot(a,b)/(na*nb))

```

### Make Node Features

The function below constructs the complete feature matrix for the graph.  
For each node, we compute:

- PageRank  
- In-degree and Out-degree  
- k-core number (structural cohesion)  
- Clustering coefficient  
- Recent posting activity  
- Topic similarity to the query  

The features are optionally normalized to stabilize GCN training.



```python
def make_features(G: nx.DiGraph, qtopics=None, normalize=True):
    vocab = sorted({t for _, d in G.nodes(data=True) for t in d.get("topics", [])})
    qv = topic_vector([t.lower() for t in (qtopics or [])], vocab)

    Gu = G.to_undirected()

    # Deterministic PageRank
    pr = {}
    if G.number_of_nodes():
        nstart = {n: 1.0 / G.number_of_nodes() for n in G}
        pr = nx.pagerank(G, nstart=nstart)

    deg_in, deg_out = dict(G.in_degree()), dict(G.out_degree())
    kcore = nx.core_number(Gu) if G.number_of_nodes() else {n: 0 for n in G}
    clust = nx.clustering(Gu) if G.number_of_nodes() else {n: 0.0 for n in G}

    X, nodes = [], []
    for n, d in G.nodes(data=True):
        nodes.append(n)
        tv = topic_vector(d.get("topics", []), vocab)
        topicality = cosine(tv, qv) if len(qv) else 0.0

        X.append([
            pr.get(n, 0.0),
            deg_in.get(n, 0),
            deg_out.get(n, 0),
            kcore.get(n, 0),
            clust.get(n, 0.0),
            d.get("posts_30d", 0),
            topicality,
        ])

    X = np.asarray(X, dtype=np.float32)
    if normalize and len(X):
        X = (X - X.mean(axis=0, keepdims=True)) / (X.std(axis=0, keepdims=True) + 1e-6)

    names = ["pagerank", "deg_in", "deg_out", "kcore", "clust", "posts_30d", "topic_sim"]
    return nodes, X, names

```

### Define a Simple Influence Target

To train a GCN ranker, we need a target value that reflects “influence.” Because no ground-truth labels exist, we construct a heuristic influence score by combining PageRank, degree ratios, activity, and topic relevance.  

The GCN will learn to approximate this heuristic but later generalize it across different subgraphs.



```python
def simple_target(G, nodes, X, names):
    idx = {f:i for i,f in enumerate(names)}
    s = (0.45*X[:,idx["pagerank"]] +
         0.25*(X[:,idx["deg_in"]] / (1+np.maximum(1.0, X[:,idx["deg_out"]]))) +
         0.15*X[:,idx["posts_30d"]] +
         0.15*X[:,idx["topic_sim"]])
    s = (s - s.min())/(1e-8 + (s.max()-s.min()))
    return s.astype(np.float32)

```

### GCN-Based Influence Ranker

Here we define a simple two-layer Graph Convolutional Network. The model takes the engineered node features and propagates them through graph convolutions, ultimately predicting a scalar influence score for each node. Dropout layers help regularize training.



```python
class InfluenceGCN(nn.Module):
    def __init__(self, in_dim, hid=64, p_drop=0.1):
        super().__init__()
        self.gc1 = GCNConv(in_dim, hid, cached=False, add_self_loops=False)
        self.gc2 = GCNConv(hid, hid, cached=False, add_self_loops=False)
        self.out = nn.Linear(hid, 1)
        self.drop = nn.Dropout(p_drop)

    def forward(self, x, edge_index):
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))
        h = self.gc1(x, edge_index)
        h = F.relu(h)
        h = self.drop(h)
        h = self.gc2(h, edge_index)
        h = F.relu(h)
        h = self.drop(h)
        return self.out(h).squeeze(-1)

```

### Pairwise Ranking Training

We train the GCN ranker using a **pairwise ranking loss**. Instead of predicting absolute values, the GCN learns ordering: if node *i* should rank higher than node *j*, the model is penalized unless `score(i) > score(j)`.  

This produces a model optimized for influencer ranking tasks within subgraphs.



```python
def train_ranker(G, qtopics, epochs=100, lr=2e-3, pairs_per_epoch=1024):
    # Build features and heuristic targets
    nodes, X, names = make_features(G, qtopics, normalize=True)
    y = simple_target(G, nodes, X, names)

    # Convert to PyG graph
    H = G.to_directed()
    d = pyg_from_nx(H)
    n2i = {n: i for i, n in enumerate(list(H.nodes()))}

    feat = np.zeros((len(n2i), X.shape[1]), dtype=np.float32)
    for i, n in enumerate(nodes):
        if n in n2i:
            feat[n2i[n]] = X[i]

    d.x = torch.tensor(feat, dtype=torch.float32, device=device)
    d.y = torch.tensor(y, dtype=torch.float32, device=device)
    d.edge_index = d.edge_index.to(device)

    model = InfluenceGCN(d.x.shape[1]).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)

    # Pre-draw pairs using a deterministic generator
    g = torch.Generator(device="cpu").manual_seed(SEED)
    N = d.x.shape[0]
    idx_all = torch.randint(0, N, (epochs, pairs_per_epoch), generator=g)
    jdx_all = torch.randint(0, N, (epochs, pairs_per_epoch), generator=g)

    for ep in range(epochs):
        model.train()
        opt.zero_grad()

        s = model(d.x, d.edge_index)
        idx = idx_all[ep].to(device)
        jdx = jdx_all[ep].to(device)

        mask = (d.y[idx] > d.y[jdx])
        if mask.any():
            loss = -torch.log(torch.sigmoid(s[idx[mask]] - s[jdx[mask]])).mean()
            loss.backward()
            opt.step()
        else:
            loss = torch.tensor(0.0, device=device)

        if ep % 5 == 0:
            print(f"-train- ep {ep:02d} loss {loss.item():.4f}")

    model.eval()
    return model

```


```python
print("[gnn] training GCN ranker…")

trained_model = train_ranker(
    G,
    qtopics=["politician", "company", "tv_show", "news", "brand"],
    epochs=100,
    lr=2e-3,
)

print("✅ Training complete.")

```

### Graph Retrieval for a Query

To support Graph-RAG, we create utilities that:

- Parse a user’s natural-language query and infer coarse topic labels.  
- Extract a relevant subgraph by expanding outward from topic-matched seeds.  
- Prepare subgraphs for GCN scoring.

This enables the agent to retrieve only the portion of the graph relevant to the user query, making the pipeline more efficient and interpretable.



```python
def link_entities(q: str):
    q = (q or "").lower()
    cand = ["politician", "company", "tv_show", "news", "brand", "community", "sports", "music"]
    topics = [t for t in cand if t in q] or ["politician", "company", "tv_show"]
    return {"topics": topics}

```


```python
def graph_retrieve(G, ents, k=2, top_n=800):
    topics = ents.get("topics", [])

    # Seeds: users whose topics intersect the query topics
    seeds = [n for n, d in G.nodes(data=True) if set(d.get("topics", [])) & set(topics)] \
            or list(G)[:200]

    S = set()
    for s in seeds[:100]:
        S.add(s)
        fringe = {s}
        for _ in range(k):
            nxt = set()
            for u in list(fringe):
                nxt |= set(G.successors(u))
                nxt |= set(G.predecessors(u))
            S |= nxt
            fringe = nxt

    return G.subgraph(sorted(list(S))[:top_n]).copy()

```


```python
def score_subgraph(Gsub, qtopics, model):
    nodes, X, names = make_features(Gsub, qtopics, normalize=True)

    H = Gsub.to_directed()
    d = pyg_from_nx(H)
    n2i = {n: i for i, n in enumerate(list(H.nodes()))}

    feat = np.zeros((len(n2i), X.shape[1]), dtype=np.float32)
    for i, n in enumerate(nodes):
        if n in n2i:
            feat[n2i[n]] = X[i]

    d.x = torch.tensor(feat, dtype=torch.float32, device=device)
    d.edge_index = d.edge_index.to(device)

    with torch.no_grad():
        s = trained_model(d.x, d.edge_index).detach().cpu().numpy()

    return {n: float(s[n2i[n]]) for n in nodes if n in n2i}

```

### LLM Summarization of Top Influencers

Once the subgraph is scored, we use an LLM to summarize the top influencers. This helper function formats the evidence lines and sends them to the OpenAI model, asking it to rank key influencers, justify each ranking, and propose an outreach plan.

We now connect to the OpenAI client:

- Packs the top-K scored nodes into evidence lines.
- Asks the LLM to:
  - Rank 3–5 key influencers,
  - Provide one-sentence rationales,
  - Suggest a short outreach plan.



```python
client = OpenAI()

def llm_summarize(query, topk, Gsub):
    bullets = []
    for i, (u, sc, _) in enumerate(topk[:8], 1):
        d = Gsub.nodes[u]
        bullets.append(
            f"{i}. node={u} | score={sc:.2f} | "
            f"in={Gsub.in_degree(u)} out={Gsub.out_degree(u)} | "
            f"topics={','.join(d.get('topics', []))} | "
            f"posts_30d={d.get('posts_30d', 0)}"
        )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a precise social-graph analyst. Use only the given evidence. "
                "Return: (1) ranked list (3–5), (2) one-sentence rationale each, "
                "(3) a short outreach plan grounded in the graph."
            ),
        },
        {
            "role": "user",
            "content": f"User query: {query}\nEvidence lines:\n" + "\n".join(bullets),
        },
    ]

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.0,
        top_p=1,
        max_tokens=500,
        seed=SEED,
    )
    return resp.choices[0].message.content.strip()

```

### Agentic Graph-RAG with LangGraph

Now we wrap the entire workflow into a LangGraph agent. 

The agent consists of four nodes:

- **plan**: infer query topics  
- **retrieve**: extract a relevant subgraph  
- **score**: apply the GCN ranker  
- **synthesize**: generate a final natural-language summary  

LangGraph coordinates the flow between these steps to form a coherent agent.



```python
class AgentState(TypedDict, total=False):
    query: str
    plan: str
    entities: Dict[str, Any]
    subgraph: nx.DiGraph
    scores: Dict[str, float]
    answer: str


def _plan(s: AgentState) -> AgentState:
    s["plan"] = "rank_influencers_and_explain"
    s["entities"] = link_entities(s.get("query", ""))
    return s


def _retrieve(s: AgentState) -> AgentState:
    s["subgraph"] = graph_retrieve(G, s["entities"], k=2, top_n=800)
    return s


def _score(s: AgentState) -> AgentState:
    q = s.get("entities", {}).get("topics", [])
    s["scores"] = score_subgraph(s["subgraph"], q, model=trained_model)
    return s


def _synthesize(s: AgentState) -> AgentState:
    q = s.get("entities", {}).get("topics", [])
    nodes, X, names = make_features(s["subgraph"], q)

    # PageRank on the subgraph for extra explanation features
    pr = (
        nx.pagerank(
            s["subgraph"],
            nstart={n: 1 / max(1, s["subgraph"].number_of_nodes()) for n in s["subgraph"]},
        )
        if s["subgraph"].number_of_nodes()
        else {}
    )

    triples = []
    for u in nodes:
        sc = s["scores"].get(u, 0.0)
        d = s["subgraph"].nodes[u]
        why = (
            f"PR~{pr.get(u, 0):.2f}, "
            f"deg_in={s['subgraph'].in_degree(u)}, "
            f"posts={d.get('posts_30d', 0)}, "
            f"topics={','.join(d.get('topics', []))}"
        )
        triples.append((u, sc, why))

    triples.sort(key=lambda x: (-x[1], str(x[0])))
    topk = triples[:10]

    s["answer"] = llm_summarize(s.get("query", ""), topk, s["subgraph"])
    s["scores"] = {u: sc for u, sc, _ in topk}
    return s


graph = StateGraph(AgentState)
graph.add_node("plan", _plan)
graph.add_node("retrieve", _retrieve)
graph.add_node("score", _score)
graph.add_node("synthesize", _synthesize)

graph.add_edge(START, "plan")
graph.add_edge("plan", "retrieve")
graph.add_edge("retrieve", "score")
graph.add_edge("score", "synthesize")
graph.add_edge("synthesize", END)

app = graph.compile()

print("✅ LangGraph agent compiled.")

```

### Run the Agent on a Sample Query

Let’s run the full Agentic Graph-RAG pipeline on a sample query. This will show how the agent retrieves a subgraph, scores influencers, and produces a well-structured natural-language response.

Let’s try a query that mixes *politician* and *company* contexts and inspect the agent’s answer.



```python
query = "Find influencers for politician and company pages"

res = app.invoke({"query": query})

print(f"\n=== Agent Answer (model: {OPENAI_MODEL}) ===\n")
print(res["answer"])

```

### Visualize Top Influencer Neighborhoods

Finally, we visualize the local neighborhoods around the top-ranked influencers. This helps us understand why these nodes matter by showing their 1-hop connections and relative structural influence within the subgraph.



```python
def plot_top3(G, scores, hops=1, title="Top-3 influencer neighborhoods"):
    top = [u for u, _ in sorted(scores.items(), key=lambda x: (-x[1], str(x[0])))[:3]]

    H = nx.DiGraph()
    for c in top:
        if c not in G:
            continue
        H.add_node(c, **G.nodes[c])
        fringe = {c}
        for _ in range(hops):
            nxt = set()
            for u in list(fringe):
                for v in G.successors(u):
                    H.add_node(v, **G.nodes[v])
                    H.add_edge(u, v)
                    nxt.add(v)
                for v in G.predecessors(u):
                    H.add_node(v, **G.nodes[v])
                    H.add_edge(v, u)
                    nxt.add(v)
            fringe = nxt

    if H.number_of_nodes() == 0:
        print("[viz] empty")
    else:
        pos = nx.spring_layout(H, seed=SEED)
        ns = [6 + 2 * H.in_degree(n) for n in H.nodes()]
        nx.draw_networkx_nodes(H, pos, node_size=ns, alpha=0.85)
        nx.draw_networkx_edges(H, pos, alpha=0.25, arrows=True)
        nx.draw_networkx_labels(H, pos, font_size=7)
        plt.title(title)
        plt.axis("off")
        plt.show()


plot_top3(G, res.get("scores", {}), hops=1)

```

## Conclusion

This lab showed how graph structure, neural ranking, and agentic LLM reasoning can be combined to analyze influence in a social network. By building a Page–Page graph, engineering features, and training a GCN ranker, we created a model that captures both local and global patterns of connectivity. Integrating the ranker into a LangGraph agent enabled a full Graph-RAG workflow: planning from a natural-language query, retrieving a meaningful subgraph, and generating actionable summaries.

The final system demonstrates how graph-aware retrieval and learned influence modeling provide deeper, more interpretable insights than text-only RAG approaches. Visualizations such as the top influencer neighborhoods highlight how structural patterns drive the agent’s decisions. This foundation can be extended with richer GNNs, temporal analysis, or more advanced agentic behaviors.


## Reference

- Kipf, T. N., & Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks. International Conference on Learning Representations (ICLR).
- The social-network dataset used in this lab is based on the **MUSAE Facebook Page–Page network**: https://snap.stanford.edu/data/facebook-large-page-page-network.html


## Authors


[Zikai Dou](https://author.skills.network/instructors/zikai_dou)


## Contributors


[Joseph Santarcangelo](https://author.skills.network/instructors/joseph_santarcangelo) 

[Wojciech "Victor" Fulmyk](https://author.skills.network/instructors/wojciech_fulmyk)


Copyright © IBM Corporation. All rights reserved.

