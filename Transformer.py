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
        self.zPUphasor = [self.makeZpuPhasor(self.zPct, self.xrRatio, self.vPrimary, self.vSecondary, sRated)] #zPUphasor[0] is magnitude while [1] is phase
        self.zPuRect = cmath.rect(*self.zPUphasor)  #has a list be passed in as multiple argurments to a function... so this is mag and phase
        self.txresistancePU = self.zPuRect.real
        self.txreactancePu = self.zPuRect.imag

    def makeZpuPhasor(self, zPCT, xrRatio, vprim, srated): #is it vlow or v primary????
            zTransformerPU = (zPCT / 100) * cmath.exp(cmath.atan(xrRatio) * 1j) * ((vprim**2/srated)/(vprim**2/100))
            return cmath.polar(zTransformerPU)








