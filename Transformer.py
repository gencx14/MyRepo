from TransformerData import TransformerData
from Bus import Bus
class Transformer:
    #you will need to have already created a tx data object to pass into this class.
    def __init__(self, name: str, bus1: Bus, bus2: Bus, txData: TransformerData):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.data = txData
