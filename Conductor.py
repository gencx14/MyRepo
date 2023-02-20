class Conductor:
#once this is ready update TransmissionLineData.py so that conductor information only has to be put in once
    def __int__(self, name: str, outerDiameter, gmr, rAC):
        self.name = name
        self.diameter = outerDiameter
        self.gmr = gmr
        self.rAC = rAC

    def getdiameter(self):
        return self.diameter

    def getgmr(self):
        return self.gmr

    def getrAC(self):
        return self.rAC




