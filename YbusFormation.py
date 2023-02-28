from System import System
import numpy as np
class YbusFormation:

    def __int__(self, name, system: System):
        self.name = name
        self.system = system
        self.numBusses = len(self.system.buses)
        self.yBusMatrix = np.zeros(self.numBusses, self.numBusses, dtype=complex)      # creates an n by n matrix of zeros where

    def fillYbusMatrix(self):
        for n in range(0, self.numBusses - 1):
            for k in range(0, self.numBusses - 1):
                if n == k:
                    #solve the kk method
                    self.yBusMatrix[n][k] = #loop thorugh your tx and tline and loop through to identify the busses, if bus = bus we are searching for then add them
                    #look up lists comprehension
                else:
                    #solve for kn method
                    self.yBusMatrix[n][k] =




#form a [Bus.busCount]i [Bus.busCount]k matrix
#do a loop through k inside a loop through i. In the inner loop have an if statement that if i == k do the Ykk
#  calculation. If i != k then do the Ykn calculation and store the value in the [i][k] spot in the matrix.
