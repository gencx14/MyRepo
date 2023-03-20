import cmath
from BaseValues import BaseValues


class TransformerData:
    txCount = 0

    def __init__(self, name: str, s_rated, v_primary, v_secondary, zpct_transformer, xr_ratio, bases: BaseValues):
        self.name = name
        self.srated = s_rated
        self.sbase = bases.pbase
        self.vprimary = v_primary
        self.vsecondary = v_secondary
        self.zpct = zpct_transformer
        self.xr_ratio = xr_ratio
        self.zPUphasor = None
        self.zPuRect = None
        self.makeZpu(self.zpct, self.xr_ratio, self.vprimary, self.srated)
        self.txRpu = self.zPuRect.real
        self.txXpu = self.zPuRect.imag
        self.txYpu = 1 / (self.txRpu + 1j * self.txXpu)


    def makeZpu(self, zPCT, xrRatio, vprim, srated):  # is it vlow or v primary????
        self.zPuRect = (zPCT / 100) * cmath.exp(cmath.atan(xrRatio) * 1j) * (
                    (vprim ** 2 / srated) / (vprim ** 2 / 100))
        self.zPUphasor = cmath.polar(self.zPuRect)


    def gettxYpu(self):
        return self.txYpu

    def gettxRpu(self):
        return self.txRpu

    def gettxXpu(self):
        return self.txXpu
