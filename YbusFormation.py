from System import System
import numpy as np
class YbusFormation:

    def __int__(self, name, system: System):
        self.name = name
        self.system = system
        self.numBusses = len(self.system.buses)
        self.yBusMatrix = np.zeros(self.numBusses, self.numBusses, dtype=complex)      # creates an n by n matrix of zeros where

    def fillYbusMatrix(self):
        for n in range(len(self.system.buses)):
            for k in range(len(self.system.buses)):
                if n == k:
                    #solve the kk method
                    #loop through all of the transmission lines **** NEED TO MAKE TLINES PU BEFORE THIS********
                    tline_y = 0
                    tx_y = 0
                    for i in range(len(self.system.transmissionlines)):
                        #if the bus for the tLine is the bus we are currently on then add its series and 1/2 its shunt to the node
                        if ((self.system.transmissionlines[tline_order[n]].bus1 == self.system.buses_order[n]) and (self.system.transmissionlines[tline_order[k]].bus1 == self.system.buses_order[k])) or ((self.system.transmissionlines[tline_order[n]].bus2 == self.system.buses_order[n]) and (self.system.transmissionlines[tline_order[k]].bus2 == self.system.buses_order[k])):
                            tline_y = tline_y + self.system.transmissionlines[tline_order[n]].totalYseries + self.system.transmissionlines[tline_order[n]].halfYshunt
                    for i in range(len(self.system.transformers))
                        if ((self.system.transformers[tx_order[n]].bus1 == self.system.buses_order[n]) and (self.system.transformers[tx_order[k]].bus1 == self.system.buses_order[k])) or ((self.system.transformers[tx_order[n]].bus2 == self.system.buses_order[n]) and (self.system.transformers[tx_order[k]].bus2 == self.system.buses_order[k])):
                            tx_y = tx_y + self.system.transformers[tx_order[n]].data.txYpu
                    self.yBusMatrix[n][k] = tline_y + tx_y
                        #loop thorugh your tx and tline and loop through to identify the busses, if bus = bus we are searching for then add them
                        #look up lists comprehension
                else:
                    #solve for kn method
                    self.yBusMatrix[n][k] =




#form a [Bus.busCount]i [Bus.busCount]k matrix
#do a loop through k inside a loop through i. In the inner loop have an if statement that if i == k do the Ykk
#  calculation. If i != k then do the Ykn calculation and store the value in the [i][k] spot in the matrix.
