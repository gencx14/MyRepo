import ssl
import cmath
import math

class Transformer:
    txCount = 0

    def __init__(self, sRated, vPrimary, vSecondary, zPctTransformer, xrRatio):
        self.sRated = sRated
        self.sBase = sRated
        self.vPrimary = vPrimary
        self.vBasePrim = vPrimary
        self.vSecondary = vSecondary
        self.vBaseSecondary = vSecondary
        self.zPct = zPctTransformer
        self.xrRatio = xrRatio
        self.zPUphasor = self.makeZpuPhasor(self.zPct, self.xrRatio)
        self.zPuRect = self.makeZpuRect(self.zPUphasor)

    def makeZpuPhasor(self, zPCT, xrRatio):
        anglerads = cmath.atan(xrRatio)
        zTransformerPU = (zPCT/100)*cmath.exp(anglerads*1j)*()
        return cmath.polar(zTransformerPU)

    def makeZpuRect(self, zPuPhasor):
        return cmath.rect(zPuPhasor)







