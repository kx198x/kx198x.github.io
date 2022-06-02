import math


class AnisotropicMHD():
    """
    """
    def __init__(self, gam=5/3):
        self.gam = gam
        
    def set_param(self,
                  eps1=1.,
                  th1=0.,
                  beta1=1.,
                  eps2=1.
                  ):
        self.eps1 = eps1
        self.th1 = th1
        self.beta1 = beta1
        self.eps2 = eps2
    
    def solve(self):
        gam1 = (self.gam - 1.)/self.gam
        gam2 = (self.gam + 1.)/self.gam
        
        xi1 = gam1*(mn2sq - 2. + 1./self.eps2) \
            - (2. + 1./self.eps2)/(3.*self.gam)
        xi2 = (mn2sq - 1.)**2
        
        lama = gam1*xi2/math.cos(self.th1) \
            - xi1*mn2sq*math.tan(self.th1)**2