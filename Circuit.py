from Resistor import Resistor
from Load import Load
from VoltageSource import VoltageSource




class Circuit:
    componentCount = 0
    CircuitCount = 0

    def __init__(self, name)
        self.name = name
        self.vItems = []
        self.rItems = []
        self.loadItems = []
        self.BusItems = []
        Circuit.CircuitCount += 1

    def addVsourceElement(self, name, bus1, voltage):
        self.componentCount += 1
        vsObject = VoltageSource(name, bus1, voltage)
        self.vItems.append(vsObject)
    def addResistorElement(self, name, bus1, bus2, ohms):
        self.componentCount += 1
        self.resistorCount += 1
        resistorObject = Resistor(name, bus1, bus2, ohms) #creates a resistor object within my circuit object
        self.rItems.append(resistorObject) #
    def addLoadElement(self, load):
        self.componentCount += 1
        self.loadCount += 1
        self.loadItems.append(load)
    def getVsourceElement(self, name):
        return self.vItems.
    def getResistorElement(self, index):
        return self.rItems[index]
    def getLoadElement(self, index):
        return self.loadItems[index]
    def getVitems(self):
        return self.vItems
    def getrItems(self):
        return self.rItems
    def getloadItems(self):
        return self.loadItems

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
