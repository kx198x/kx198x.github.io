---
layout: post
tags: networkx, extension
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>

pandas dataframe を基本とするグラフデータ処理系の忘備録．

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Networkx base](#networkx-base)
    - [アトリビュート継承](#アトリビュート継承)
- [Third-party IF extension](#third-party-if-extension)
  - [graph-pandas](#graph-pandas)
    - [graph to pandas](#graph-to-pandas)
    - [pandas to graph](#pandas-to-graph)
  - [pandas-data](#pandas-data)
    - [from/to excel](#fromto-excel)
    - [to/from csv](#tofrom-csv)
  - [graph-numpy](#graph-numpy)
- [pandas グラフデータ処理](#pandas-グラフデータ処理)
  - [地理座標系でのノード間距離計算(WGS84)](#地理座標系でのノード間距離計算wgs84)
- [Other extension](#other-extension)
  - [Linear algebra](#linear-algebra)
    - [distance Laplacian matrix](#distance-laplacian-matrix)
    - [distance Laplacian spectrum](#distance-laplacian-spectrum)
- [plot examples](#plot-examples)
  - [networkx extension](#networkx-extension)
  - [graphviz](#graphviz)

<!-- /code_chunk_output -->


## Networkx base

![fig01](/assets/fig/20000101_01.svg)

#### アトリビュート継承

---
## Third-party IF extension

### graph-pandas

---
#### graph to pandas

```Python
df_nodes, df_edges = pn.graph.ext_networkx.graph_to_dataframe(G)
```

#### pandas to graph

```Python
G = pn.graph.ext_networkx.dataframe_to_graph(
        df_nodes, df_edges, create_using=nx.Graph()
        )
```
---
### pandas-data

#### from/to excel

+ from .xlsx w/o note
```Python
df_nodes, df_edges = pn.graph.io.read_graph(filename)
```

+ from .xlsx w/ note
```Python
df_nodes, df_edges, df_note = pn.graph.io.read_graph(filename, note=True)
```

+ to .xlsx w/o note
```Python
pn.graph.io.write_graph(filename, df_nodes, df_edges)
```

+ to .xlsx w/ note
```Python
note = {'x': 1, 'y': 2}
pn.graph.io.write_graph(filename, df_nodes, df_edges, note=note)
```

#### to/from csv

```Python
df_nodes.to_csv(filename)
```

```Python
df_nodes = pd.read_csv(filename, index_col=0)
```

---
### graph-numpy

---
## pandas グラフデータ処理

### 地理座標系でのノード間距離計算(WGS84)

```Python
>>> 
```

---
## Other extension

### Linear algebra

#### distance Laplacian matrix

#### distance Laplacian spectrum

---
## plot examples

### networkx extension

+ 構造
pre: {fig, axis, map, graph}
optional: {subgraph, path, edge, node}
post: {xylim, ..., show}

---
### graphviz