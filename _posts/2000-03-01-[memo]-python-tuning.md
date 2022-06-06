---
layout: post
tags: python, tuning
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tuning tools](#tuning-tools)
  - [Calculation time](#calculation-time)
  - [Memory](#memory)
- [Tips](#tips)
  - [numpy](#numpy)
  - [k-shortest-paths](#k-shortest-paths)

<!-- /code_chunk_output -->

## Tuning tools

### Calculation time

+ install

```Python
pip install line_profiler
```

+ run

測定対象関数の前行に `@profile` 追加し実行:

```Shell
kernprof -l ***.py
```

+ check run-time

```Shell
python -m line_profiler ***.lprof
```

### Memory

```Python
pip install memory_profiler
pip install psutil (計測時間向上のため)
```

```Shell
python -m memory_profiler ***.py
```

## Tips

### numpy

```Python
xi = np.zeros(nxi)
for n in range(nxi):
    for i in range(a_nrow):
        xi[n] += np.dot(a[i], self.bitarray[n+i+selfn_bound])
```
x ... for 文

```Python
xi = np.zeros(nxi)
for n in range(nxi):
    vb = self.bitarray[n+self.n_bound:n+self.n_bound+a_nrow].flatten()
    xi[n] = np.dot(a.flatten(), vb)
```
o ... 1次元化して内積

### k-shortest-paths

$(n,m)=(\| V\| ,\| E\| )$
+ Yen's algorithm: $\mathcal{O}(kn(m+n\log n))$[^1] >> networkx
+ Eppstein's algorithm: $\mathcal{O}(m+n\log n + k\log k)$[^2] >> JGraphT
jgrapht.algorithms.shortestpaths.eppstein_k[^3]

```Shell
pip install jgrapht
```
```jgrapht.create_graph()``` >> weighted graph, then Eppstein's algorithm

### Pulp


---

[^1]: Jin Y. Yen, “Finding the K Shortest Loopless Paths in a Network”, Management Science, Vol. 17, No. 11, pp. 712-716, (1971)

[^2]: D. Eppstein, "Finding the k Shortest Paths," SIAM J. Comput. 28 (2): pp. 652–673 (1998)

[^3]: [JGraphT Algorithms Shortest-Paths](https://python-jgrapht.readthedocs.io/en/jgrapht-1.5.0.1/api/algorithms/shortestpaths.html)