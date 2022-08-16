---
layout: post
tags: Rankine-Hugoniot, shock, anisotropy, MHD
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>

(加筆中)

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

> 温度異方性があり，かつ流体近似が成り立つプラズマ中では，以下の Rankine-Hugoniot 条件が成り立つ [^1]
$$\begin{align*}
\Lambda_a(\epsilon_2,\theta_1,M_{A2}^2)\cdot\epsilon_1^2M_{A1}^4
&+2\Lambda_b(\epsilon_1,\epsilon_2,\theta_1,\beta_1,M_{A2}^2)\cdot\epsilon_1M_{A1}^2\\
&+\Lambda_c(\epsilon_1,\epsilon_2,\theta_1,\beta_1,M_{A2}^2)=0.
\end{align*}$$

ここで $\Lambda_a, \Lambda_b, \Lambda_c$ は以下の関係で決まる．

$$\begin{align*}
\Lambda_a&=\Gamma_{-}\frac{\xi_2}{\cos^2\theta_1}
-\xi_1M_{A2}^2\tan^2\theta_1,\\
%
\Lambda_b&=\xi_2\left[
    \Gamma_{-}\frac{2(1-\epsilon_1)}{3\cos^2\theta_1}
    +\frac{\epsilon_1\beta_1}{2\cos^2\theta_1}
    -\epsilon_2M_{A2}^2
\right]
+\epsilon_1\xi_1M_{A2}^2\tan^2\theta_1,\\
%
\Lambda_c&=M_{A2}^2\left\{
    \epsilon_2^2\xi_2\left[
        \Gamma_{+}M_{A2}^2
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
\xi_1 &= \Gamma_{-}\left(M_{A2}^2-2+\frac{1}{\epsilon_2}\right)
-\frac{1}{3\gamma}\left(2+\frac{1}{\epsilon_2}\right),\\
%
\xi_2&=\left(M_{A2}^2-1\right)^2.
\end{align*}$$

modified intermediate Mach number $M_A=V_n/(\sqrt{\epsilon}V_{An})$, where $V_{An}=B_n/\sqrt{4\pi\rho}$[^2]

##### <u>証明</u>

deHoffman-Teller 系で考える．$x\rightarrow t,x\rightarrow n, y\rightarrow$none, RH relations are as follows[^3]
$$\begin{align}
\left[\rho v_x\right]_2^1&=0,\\
%
\left[\rho v_x^2+\bar{p}+\frac{1}{3}\left(\epsilon+\frac{1}{2}\right)\frac{B^2}{4\pi}-\epsilon\frac{B_x^2}{4\pi}\right]_2^1&=0,\\
%
\left[\rho v_xv_z-\epsilon\frac{B_xB_z}{4\pi}\right]_2^1&=0,\\
%
\left[\rho v_x\left(v^2+\frac{\gamma}{\gamma-1}\frac{\bar{p}}{\rho}\right)+\frac{\epsilon+2}{3}v_x\frac{B^2}{4\pi}
-\epsilon v_x\frac{B_x^2}{4\pi}
-\epsilon v_z\frac{B_xB_z}{4\pi}
\right]_2^1&=0,
\end{align}$$

where $\bar{p}=(p_\parallel+2p_\perp)/3$ and $\epsilon=1-(\beta_\parallel-\beta_\perp)/2$.

(1), x から，
$$\begin{align*}
&\frac{1}{V_{A2}^2}\frac{p_2}{\rho_2}
= \epsilon_1 M_{n1}^2+\frac{\epsilon_1}{\gamma}M_{c1}^2
+\frac{2}{3}\left(\epsilon_2-\epsilon_1\right)
+\frac{1}{3}\left(\epsilon_1+\frac{1}{2}\right)\tan^2\theta_1\\
&\hspace{1cm}-\epsilon_2 M_{A2}^2-\frac{1}{3}\left(\epsilon_2+\frac{1}{2}\right)\tan^2\theta_2.
\end{align*}$$

x,x から，
$$\begin{align*}
\tan^2\theta_2 = \frac{\epsilon_1^2}{\epsilon_2^2}\cdot
\frac{\left(M_{n1}-1\right)^2}{\left(M_{n2}-1\right)^2}\tan^2\theta_1.
\end{align*}$$

x, x から，
$$\begin{align*}
&\left(1+\tan^2\theta_1\right)\left[
    \epsilon_1^2M_{A1}^4 + \frac{4}{3}\epsilon_1\left(1-\epsilon_1\right)M_{A1}^2
\right] + \frac{2\epsilon_1^2}{\gamma-1}M_{c1}^2M_{A1}^2= \\
&\hspace{1cm}\left(1+\tan^2\theta_2\right)\left[
    \epsilon_2^2M_{A2}^4 + \frac{4}{3}\epsilon_2\left(1-\epsilon_2\right)M_{A2}^2
\right] + \frac{2\gamma\epsilon_2}{\gamma-1}M_{A2}^2\frac{1}{V_{A2}^2}\frac{p_2}{\rho_2}.
\end{align*}$$

2 で $\theta_2$ を消去しつつ 1, 3 を整理．
$\Box$

---
##### 物理的解釈

辿る順番

+ 現実が MHD - collisionless - MHD という異なる方程式系の接続である場合に，MHD - MHD という接続関係と同じ結果になると言えるか．
+ Double adiabatic の意味．
+ 波の伝搬と温度異方性．発展性条件．
+ 導出した RH の具体的解釈．

---
##### Python solver

###### download/install



###### example

```Python
import rankine_hugoniot as rh
obj = rh.AnisotropicMHD()
```

```Python
obj.set_param(
    beta1=1e-2,
    eps2=0.6
)
obj.solve()
```

```Python
obj.plot()
```

<img src="/assets/fig/20220515/shock_curve.png" alt="relations" style="width: 100%;" />
<figcaption align = "center"><b>Fig.1: Shock curve</b></figcaption>

---
[^1]: K. Higashimori, M. Hoshino, The relation between ion temperature anisotropy and formation of slow shocks in collisionless magnetic reconnection, Journal of Geophysical Research: Space Physics, 10.1029/2011JA016817, 117, A1, (2012). https://doi.org/10.1029/2011JA016817
[^2]: L.-N. Hau and B.U.O. Sonnerup, "On the structure of resistive MHD intermediate shocks," J. Geophys. Res., 94, 6539–6551, (1989). https://doi.org/10.1029/JA094iA06p06539
[^3]: H. Karimabadi, D. Krauss-Varban, and N. Omidi, "Temperature anisotropy effects and the generation of anomalous slow shocks, Geophys. Res. Lett., 22, 2689–2692, (1995). https://doi.org/10.1029/95GL02788