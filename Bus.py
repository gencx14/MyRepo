class Bus:
    #Class Attribute
    busCount = 0
    def __init__(self, name):
        Bus.busCount += 1
        Bus.name = name
