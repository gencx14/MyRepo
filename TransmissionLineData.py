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
        self.cPrime = 2*cmath.pi*(8.854*10**(-12))/cmath.log(self.deq / bundle.getdsc()) #units of Ferads per meter  C'   ***** Check your units
        self.lPrime = (2*10**(-7)) * cmath.log(self.deq / bundle.getdsl()) #inductance per meter H/m L'
        self.ohmsPerMile = conductor.getrAC() / (bundle.getBundleSize())
        self.cpm = self.cPrime * 1609   #  F / mile
        self.lpm = self.lPrime * 1609   #  H / mile
        self.rPrime = self.ohmsPerMile / 1609  # ohms per meter R'
        self.zseriesperMile = self.ohmsPerMile + 1j * Constants.W * self.lpm  #  Zline per mile
        self.yshuntperMile = 1j * Constants.W * self.cpm  #  Yshunt per mile
        self.zseriesTot = self.zseriesperMile * Constants.MILE
        self.yshuntTot = self.yshuntperMile * Constants.MILE
        self.yseriesperMile = 1 / self.zseriesperMile
        self.yseriesTot = 1/ self.zseriesTot



