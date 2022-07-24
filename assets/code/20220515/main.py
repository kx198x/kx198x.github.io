import rankine_hugoniot as rh

x = rh.AnisotropicMHD()
x.set_param(beta1=1e-2)
x.solve()
x.plot()