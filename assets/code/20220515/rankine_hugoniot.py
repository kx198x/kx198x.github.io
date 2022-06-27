import math

import numpy as np
import matplotlib.pyplot as plt


class AnisotropicMHD():
    """
    """
    def __init__(self):
        self.set_param()
        
    def set_param(
        self, gam=5/3,
        eps1=1.0, eps2=1.0,
        th1=0.0,
        beta1=1.0,
        Mn2=None):
        self.gam = gam
        self.eps1 = eps1
        self.th1 = th1
        self.beta1 = beta1
        self.eps2 = eps2
        self.Mn2 = Mn2
        
        if Mn2 == None:
            self.Mn2 = np.linspace(0.0,1.0,50)
    
    def solve(self):
        Gamp = (self.gam + 1.)/self.gam
        Gamm = (self.gam - 1.)/self.gam
        
        xi1 = Gamm*(self.Mn2 - 2. + 1./self.eps2) \
            - (2. + 1./self.eps2)/(3.*self.gam)
        xi2 = (self.Mn2 - 1.)**2
        
        Lama = Gamm*xi2/math.cos(self.th1)**2 \
            - xi1*self.Mn2*math.tan(self.th1)**2
            
        Lamb = xi2*(
            Gamm*2.*(1. - self.eps1)/3/math.cos(self.th1)**2 \
            + 0.5*self.eps1*self.beta1 \
            - self.eps2*self.Mn2
        ) + self.eps1*xi1*self.Mn2*math.tan(self.th1)**2
        
        Lamc = self.Mn2*(
            self.eps2**2*xi2*(
                Gamp*self.Mn2 \
                - self.eps1*self.beta1/self.eps2/math.cos(self.th1)**2 \
                + (self.eps1/self.eps2 - 1.) \
                + (4.*Gamm*(self.eps2-1.) 
                   - (2.*self.eps1+1.)*math.tan(self.th1)**2
                )/3./self.eps2
            ) - self.eps1**2*xi1*math.tan(self.th1)**2
        )
        
        self.Mn1m = (Lamb-np.sqrt(Lamb**2-Lama*Lamc))/Lama/self.eps1
        self.Mn1p = (Lamb+np.sqrt(Lamb**2-Lama*Lamc))/Lama/self.eps1
    
    def plot(self):
        plt.plot(self.Mn1m, self.Mn2)
        plt.plot(self.Mn1p, self.Mn2)
        plt.show()
                        