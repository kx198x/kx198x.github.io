import rankine_hugoniot as rh
obj = rh.AnisotropicMHD()

obj.set_param(
    beta1=1e-2,
    eps2=0.6
)
obj.solve()

obj.plot()