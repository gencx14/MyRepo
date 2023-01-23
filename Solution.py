class Solution:

    def __init__(self, circuit):
        self.circuit = circuit
        self.resistorItems = []
        self.loadItems = []
        self.vSourceItems = []
    def buildCircuit(self):
        if len(self.circuit.getNumVsourceElements()) == 0:
            print("no power flow")
            return
        elif len(self.circuit.getNumVsourceElements()) == 1:
            self.vsItems = self.circuit.getVsourceElement(0)
            self.
            print("one source component\nVoltage Source = " + str(self.vsItem.getVoltage()) + " volts\n")
            self.Vsbus = self.vsItem.getBus1()


    def findCurrent(self):
        # find number of resistive elements
        self.NumImpedances = self.circuit.getNumResistors() + self.circuit.getNumLoads()

        #find number of voltage sources
        self.NumVSources = self.circuit.getNumVsourceElements()

        #find number of loads
        self.NumLoads = self.circuit.getNumLoads()

        #find number of resistors
        self.NumResistors = self.circuit.getNumResistors()

        if self.NumVSources == 0:
            print("No Current")
        elif self.NumVSources == 1:
            #add 1 solution steps for this problem
        else: #add solution for multiple voltage sources
            pass
            i = 0
            while i < self.NumVSources:
                pass

