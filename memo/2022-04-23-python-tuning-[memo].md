---
layout: post
tags: x
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>

## Calculation time

```Python
pip install line_profiler
```

```Shell
kernprof -l -v ***.py
```

## Memory

```Python
pip install memory_profiler
pip install psutil (計測時間向上のため)
```

```Shell
python -m memory_profiler ***.py
```