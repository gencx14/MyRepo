class Solution:
    def __init__(self, circuit):
        self.circuit = circuit
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

