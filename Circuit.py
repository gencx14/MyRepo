class Circuit:
    componentCount = 0
    v_sourceCount = 0
    resistorCount = 0
    loadCount = 0

    def __init__(self, name)
        self.name = name
        self.vItems = []
        self.rItems = []
        self.loadItems = []

    def addVsourceElement(self, vsource):
        self.componentCount += 1
        self.v_sourceCount += 1
        self.vItems.append(vsource)
    def addResistorElement(self, resistor):
        self.componentCount += 1
        self.resistorCount += 1
        self.rItems.append(resistor)
    def addLoadElement(self, load):
        self.componentCount += 1
        self.loadCount += 1
        self.loadItems.append(load)

    def removeVsourceElement(self, vsource):
        self.componentCount -= 1
        self.v_sourceCount -= 1
        self.vItems.remove(vsource)
    def removeResistorElement(self, resistor):
        self.componentCount -= 1
        self.resistorCount -= 1
        self.rItems.remove(resistor)
    def removeLoadElement(self, load):
        self.componentCount -= 1
        self.loadCount -= 1
        self.loadItems.remove(load)

    def getNumComponents(self):
        return self.componentCount
    def getNumVsourceElements(self):
        return self.v_sourceCount
    def getNumResistors(self):
        return self.resistorCount
    def getNumLoads(self):
        return self.loadCount
