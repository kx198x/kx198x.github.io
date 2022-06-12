---
layout: post
tags: Rankine-Hugoniot, shock, anisotropy, MHD
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [補題](#補題)
- [証明](#u証明u)
- [物理的解釈](#物理的解釈)
- [Python solver](#python-solver)
  - [download/install](#downloadinstall)
  - [example](#example)

<!-- /code_chunk_output -->

---
##### 補題

温度異方性があり，かつ流体近似が成り立つプラズマ中では，以下の Rankine-Hugoniot 条件が成り立つ [^1]

$$\begin{align*}
\Lambda_a(\epsilon_2,\theta_1,M_{n2}^2)\cdot\epsilon_1^2M_{n1}^4
&+2\Lambda_b(\epsilon_1,\epsilon_2,\theta_1,\beta_1,M_{n2}^2)\cdot\epsilon_1M_{n1}^2\\
&+\Lambda_c(\epsilon_1,\epsilon_2,\theta_1,\beta_1,M_{n2}^2)=0,
\end{align*}$$

ここで $\Lambda_a, \Lambda_b, \Lambda_c$ は以下の関係で決まる．

$$\begin{align*}
\Lambda_a&=\Gamma_{-}\frac{\xi_2}{\cos^2\theta_1}
-\xi_1M_{n2}^2\tan^2\theta_1,\\
\Lambda_b&=\xi_2\left[
    \Gamma_{-}\frac{2(1-\epsilon_1)}{3\cos^2\theta_1}
    +\frac{\epsilon_1\beta_1}{2\cos^2\theta_1}
    -\epsilon_2M_{n2}^2
\right]
+\epsilon_1\xi_1M_{n2}^2\tan^2\theta_1,\\
\Lambda_c&=M_{n2}^2\left\{
    \epsilon_2^2\xi_2\left[
        \Gamma_{+}M_{n2}^2
        -\frac{\epsilon_1\beta_1}{\epsilon_2\cos^2\theta_1}
        +\left(\frac{\epsilon_1}{\epsilon_2}-1\right)\right.\right.\\
    &\left.\left.\hspace{5mm}
        +\frac{4\Gamma_{-}\left(\epsilon_2-1\right)
        -\left(2\epsilon_1+1\right)\tan^2\theta_1}{3\epsilon_2}
    \right]
    -\epsilon_1^2\xi_1\tan^2\theta_1
\right\},
\end{align*}$$

$\Gamma_\pm, \xi_1, \xi_2$ は以下の関係で決まる．

$$\begin{align*}
\Gamma_\pm &= \frac{\gamma\pm 1}{\gamma},\\
\xi_1 &= \Gamma_{-}\left(M_{n2}^2-2+\frac{1}{\epsilon_2}\right)
-\frac{1}{3\gamma}\left(2+\frac{1}{\epsilon_2}\right),\\
\xi_2&=\left(M_{n2}^2-1\right)^2.
\end{align*}$$

modified intermediate Mach number $M_n=V_n/(\sqrt{\epsilon}V_{An})$, where $V_{An}=B_n/\sqrt{4\pi\rho}$[^2]

##### <u>証明</u>

deHoffman-Teller 系で考える．$x\rightarrow t,x\rightarrow n, y\rightarrow$none, RH relations are as follows[^3]
$$\begin{align}
\left[\rho V_n\right]_2^1&=0,\\
\left[\rho V_n^2+\bar{p}+\frac{1}{3}\left(\epsilon+\frac{1}{2}\right)\frac{\left|\bm{B}^2\right|}{4\pi}-\epsilon\frac{B_n^2}{4\pi}\right]_2^1&=0,\\
\left[\rho V_nV_t-\epsilon\frac{B_nB_t}{4\pi}\right]_2^1&=0,\\
\left[\rho V_n\left(V^2+\frac{\gamma}{\gamma-1}\frac{\bar{p}}{\rho}\right)+\frac{\epsilon+2}{3}V_n\frac{\left|\bm{B}^2\right|}{4\pi}
-\epsilon V_n\frac{B_n^2}{4\pi}
-\epsilon V_t\frac{B_nB_t}{4\pi}
\right]_2^1&=0,
\end{align}$$
where $\bar{p}=(p_\parallel+2p_\perp)/3$ and $\epsilon=1-(\beta_\parallel-\beta_\perp)/2$.

$$\begin{align}
\frac{1}{V_{A2}^2}\cdot\frac{p_2}{\rho_2}
&= \epsilon_1 M_{n1}^2+\cdots,\\
\tan^2\theta_2 &= \frac{\epsilon_1^2}{\epsilon_2^2}\cdot
\frac{\left(M_{n1}-1\right)^2}{\left(M_{n2}-1\right)^2}\tan^2\theta_1,\\
\left(1+\tan^2\theta_1\right)\cdots &= \cdots. 
\end{align}$$

$\Box$

---
##### 物理的解釈

辿る順番は

+ 温度異方性のある Rankine-Hugoniot 条件
+ b
+ c


---
##### Python solver

###### download/install



###### example

```Python
```

---
[^1]: Higashimori
[^2]: Hau and Sonnerup
[^3]: Karimabadi