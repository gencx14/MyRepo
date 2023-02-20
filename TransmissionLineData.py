import math
import cmath
import sys
from Geometry import Geometry
class TransmissionLineData:

    def __init__(self, name, bundleSize, geometry: Geometry, gmr, diameter, bundleDisance, rAC):
        self.name = name
        self.num = bundleSize
        self.geom = geometry
        self.d_ab = self.geom.getdab()
        self.d_bc = self.geom.getdbc()
        self.dca = self.geom.getdca()
        self.d = bundleDisance #distance between conductors in a bundle
        self.gmr = gmr #gmr in feet
        self.radius = (diameter/2)/12 #conductor radius in feet
        self.ohmsPerMeter = rAC/(bundleSize) #R = R1/bundlesize      ********THIS MAY NOT BE THE RIGHT UNITS... CHeck if it is per meter or per mile
        self.deq = self.geom.getdeq()

        if bundleSize == 1:
            self.dsl = self.gmr
            self.dsc = self.radius
        elif bundleSize == 2:
            self.dsl = math.sqrt(self.gmr * self.d)
            self.dsc = math.sqrt(self.radius * self.d)
        elif bundleSize == 3:
            self.dsl = math.cbrt(self.gmr * self.d**2)
            self.dsc = math.cbrt(self.radius * self.d**2)
        elif bundleSize == 4:
            self.dsl = 1.0941 * (self.gmr * self.d**3)**(1/4)
            self.dsc = 1.0941 * (self.radius * self.d**3)**(1/4)
        else:
            print("This program can only handle bundleSizes of 4 or less. Please adjust your input")
            sys.exit() #ends the program

        self.cpm = 2*cmath.pi*(8.854*10**(-12))/cmath.log(self.deq / self.dsc) #units of Ferads per meter     ***** Check your units
        self.lpm = (2*10**(-7)) * cmath.log(self.deq / self.dsl) #inductance per meter H/m

