class Bus:
    #Class Attribute
    busCount = 0
    def __init__(self, name): #where should I set the bus voltage
        self.index = Bus.busCount
        Bus.busCount += 1
        self.name = name
        self.voltage = None


    def get_buscount(self):
        return Bus.busCount
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    #sets the bus voltage
    def set_busvoltage(self, v):
        self.voltae = v


