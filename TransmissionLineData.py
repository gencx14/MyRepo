import math
import cmath
import sys
from Geometry import Geometry
from Conductor import Conductor
class TransmissionLineData:

    def __init__(self, name, bundleSize, geometry: Geometry, conductor: Conductor, bundleDisance):
        self.name = name
        self.num = bundleSize
        self.geom = geometry
        self.d_ab = self.geom.getdab()
        self.d_bc = self.geom.getdbc()
        self.dca = self.geom.getdca()
        self.d = bundleDisance          #  distance between conductors in a bundle
        self.gmr = conductor.getgmr()    #  gmr in feet
        self.radius = (conductor.getdiameter()/2)/12    #  conductor radius in feet
        self.ohmsPerMile = conductor.getrAC()/(bundleSize)   #  R = R1/bundlesize      ******THIS MAY NOT BE THE RIGHT UNITS... CHeck if it is per meter or per mile
        self.rPrime = self.ohmsPerMile / 1609    #  ohms per meter R'
        self.deq = self.geom.getdeq()
        self.w = 2 * cmath.pi * 60                                 #    *******Figure out where to input frequency*******

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
            sys.exit()  #   ends the program

        self.cPrime = 2*cmath.pi*(8.854*10**(-12))/cmath.log(self.deq / self.dsc) #units of Ferads per meter  C'   ***** Check your units
        self.lPrime = (2*10**(-7)) * cmath.log(self.deq / self.dsl) #inductance per meter H/m L'
        self.cpm = self.cPrime * 1609 #F / mile
        self.lpm = self.lPrime * 1609 #H / mile
        self.zseries = self.ohmsPerMile + 1j * self.w * self.lpm #Zline per mile
        self.yshunt = 1j * self.w * 1j * self.w * self.cpm #Yshunt per mile

