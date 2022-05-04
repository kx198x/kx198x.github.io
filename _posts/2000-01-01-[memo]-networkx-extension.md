---
layout: post
tags: networkx, extension
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>

pandas dataframe を基本とするグラフデータ処理系の忘備録．

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Networkx memo](#networkx-memo)
- [Third-party IF extension](#third-party-if-extension)
  - [graph-numpy](#graph-numpy)
  - [graph-pandas](#graph-pandas)
    - [graph to pandas](#graph-to-pandas)
    - [pandas to graph](#pandas-to-graph)
  - [pandas-data](#pandas-data)
    - [to/from excel](#tofrom-excel)
    - [to/from csv](#tofrom-csv)
  - [graph-numpy](#graph-numpy-1)
- [pandas dataframe でのグラフ処理](#pandas-dataframe-でのグラフ処理)
  - [地理座標系でのノード間距離計算(WGS84)](#地理座標系でのノード間距離計算wgs84)
- [plot](#plot)
  - [matplotlib](#matplotlib)
  - [graphviz](#graphviz)

<!-- /code_chunk_output -->


## Networkx memo

![fig01](/assets/fig/20000101_01.svg)

---
## Third-party IF extension

### graph-numpy

---
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

#### to/from excel

#### to/from csv

---
### graph-numpy

---
## pandas dataframe でのグラフ処理

### 地理座標系でのノード間距離計算(WGS84)

```Python
>>> aaa = x
```

---
## plot

### matplotlib

---
### graphviz