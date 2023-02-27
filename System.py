import Constants
import Bus from Bus
import Resistor from Resistor
import Bundle from Bundle
import Conductor from Conductor
import Generator from Generator
import Geometry from Geometry
import Load from Load
import Transformer from Transformer
import TransformerData from TransformerData
import TransmissionLine from TransmissionLine
import TransmissionLineData from TransmissionLineData



class System:
    componentCount = 0
    SystemCount = 0

    def __init__(self, name: str):
        self.name: str = name
        self.buses_order: List[str] = list() #makes a list of the bus order and ensures that they are entered as strings
        #make a dictionary of string and bus objects
        self.buses: Dict[str, Bus] = dict()
        #make a dictionary of the admittance elements
        self.g_elements: Dict = dict()
        #make a dictionary for voltage source objects. VItemms will only accept Voltage Source objects, if no voltage source is assigned then it will be given the value none
        self.generatorItems: Dict = dict()
        #make a dictionary for the resistor elements
        self.rItems: Dict[str, Resistor] = dict()
        #make a dictionary for the load elements
        self.loadItems: Dict[str, Load] = dict()
        #make a dictionary for your conductor elements
        self.conductors: Dict[str, Conductor] = dict()
        #make a dictionary for the geometries we have
        self.geometries: Dict[str, Geometry] = dict()
        #make a dictinoary for the bundles we have
        self.bundles: Dict[str, Bundle] = dict()
        #make a dictionary for the pure resistor items we have
        self.resistors: Dict[str, Resistor] = dict()
        #make a dictionary for the transformer data entreis
        self.transformerdataItems: Dict[str, TransformerData] = dict()
        #make a dictionary for the transformer items
        self.transformers: Dict[str, Transformer] = dict()
        #make a dictionary for transmission lines
        self.transmissionlines: Dict[str: TransmissionLine] = dict()
        #make a dictionary for transmission line data (Partridge)
        self.transmissionlineDataItems: Dict[str: TransmissionLineData] = dict()
        System.SystemCount += 1

    def add_bus(self, bus):
        if bus not in self.buses.keys():
            self.buses[bus] = Bus(bus)
            self.buses_order.append(bus)

    def addGenerator(self, name, voltage, bus1):
        if name not in self.generatorItems.keys():
            self.generatorItems[name] = Generator(name, voltage, bus1)
            self.add_bus(bus1)
            System.componentCount += 1

    def addResistorElement(self, name, bus1_name, bus2_name, ohms):
        if name not in self.resistors.keys():
            self.resistors[name] = Resistor(name, bus1_name, bus2_name, ohms)
            self.add_bus(bus1_name)
            self.add_bus(bus2_name)
            System.componentCount += 1

    def addLoadElement(self, name, bus_name, power, voltage):
        if name not in self.loadItems.keys():
            self.loadItems[name] = Load(name, bus_name, power, voltage)
            self.add_bus(bus_name)
            System.componentCount += 1

    def addConductor(self, name, outerDiameter, gmr, rAC, ampacity):
        if name not in self.conductors.keys():
            self.conductors[name] = Conductor(name, outerDiameter,gmr, rAC, ampacity)

    def addGeometry(self, name: str, ax, ay, bx, by, cx, cy):
        if name not in self.geometries.keys():
            self.geometries[name] = Geometry(name, ax, ay, bx, by, cx, cy)


    def addBundle(self, name, bundleSize, bundleDistance, conductor: Conductor):
        if name not in self.bundles.keys():
            self.bundles[name] = Bundle(name, bundleSize, bundleDistance, conductor)

    def addTransfromer(self, name: str, bus1, bus2, txData: TransformerData):
        if name not in self.transormers.keys():
            self.transformers[name] = Transformer(name, bus1, bus2, TransformerData)
            self.add_bus(bus1)
            self.add_bus(bus2)
            System.componentCount += 1
    def addTransformerData(self, name, sRated, vPrimary, vSecondary, zPctTransformer, xrRatio):
        if name not in self.transformerdataItems.keys():
            self.transformerdataItems[name] = TransformerData(self, name, sRated, vPrimary, vSecondary, zPctTransformer, xrRatio)
            System.componentCount += 1


    def addTransmissionLine(self, name: str, bus1: Bus, bus2: Bus, lineData: TransmissionLineData):
        if name not in self.transmissionlines.keys():
            self.transmissionlines[name] = TransmissionLine(name, bus1, bus2, lineData)
            self.add_bus(bus1)
            self.add_bus(bus2)
            System.componentCount += 1

    def addTransmissionLineData(self, name, bundle: Bundle, geometry: Geometry, conductor: Conductor, length):
        if name not in self.transmissionlineDataItems.keys():
            self.transmissionlineDataItems[name] = TransmissionLineData(name, bundle, geometry, conductor, length)
