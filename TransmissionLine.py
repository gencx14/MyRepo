from Bus import Bus
from TransmissionLineData import TransmissionLineData
class TransmissionLine:
 #when calling this class the user bus insert a string name, bus object Busses, and an object of the transmission line Data class for the data
    def __init__(self, name: str, bus1: Bus, bus2: Bus, lineData: TransmissionLineData, length):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.data = lineData
