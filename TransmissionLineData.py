import math
import cmath
import sys
from Geometry import Geometry
from Conductor import Conductor
from Bundle import Bundle
import Constants

class TransmissionLineData:

    def __init__(self, name, bundle: Bundle, geometry: Geometry, conductor: Conductor, length):
        self.name = name
        self.geom = geometry
        self.deq = self.geom.getdeq()
        self.w = 2 * cmath.pi * 60
        self.cPrime = 2*cmath.pi*(8.854*10**(-12))/cmath.log(self.deq / bundle.getdsc()) #units of Ferads per meter  C'   ***** Check your units
        self.lPrime = (2*10**(-7)) * cmath.log(self.deq / bundle.getdsl()) #inductance per meter H/m L'
        self.ohmsPerMile = conductor.getrAC() / (bundleSize)
        self.cpm = self.cPrime * 1609   #  F / mile
        self.lpm = self.lPrime * 1609   #  H / mile
        self.rPrime = self.ohmsPerMile / 1609  # ohms per meter R'
        self.zseriesperMile = self.ohmsPerMile + 1j * self.w * self.lpm  #  Zline per mile
        self.yshunt = 1j * self.w * self.cpm  #  Yshunt per mile
        self.zseriesTot = zseriesperMile * MILE

