class Load:
    def __init__(self, name, BusObject, powerRating, VoltageRating):
        self.name = name
        self.bus1 = BusObject
        self.P_rated = powerRating
        self.V_rated = voltageRating

    #set functions
    def setName(self, name):
        self.name = name
    def setbus1(self, BusObject):
        self.bus1 = BusObject
    def setPower(self, power):
        self.P_rated = power
    def setvoltage(self, voltageRating):
        self.V_rated = voltageRating
    #get functions
    def getName(self):
        return self.name
    def getbus1(self):
        return self.bus1

    def getRatedPower(self):
        return self.P_rated
    def getRatedVoltage(self):
        return self.V_rated
