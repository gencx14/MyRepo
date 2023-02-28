class Bus:
    #Class Attribute
    busCount = 0
    def __init__(self, name): #where should I set the bus voltage
        self.index = Bus.busCount
        Bus.busCount += 1
        self.name = name
        self.voltage = None


    def getBusCount(self):
        return Bus.busCount
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    #sets the bus voltage
    def setBusVoltage(self, v):
        self.voltae = v


