class Bus:
    #Class Attribute
    busCount = 0
    def __init__(self, name):
        Bus.busCount += 1
        Bus.name = name
    def getBusCount(self):
        return self.busCount
    def getName(self):
        return self.name
    def setName(self, name):
        Bus.name = name

