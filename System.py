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
        self.generatorItems: Optional[Generator] = None
        #make a dictionary for the resistor elements
        self.rItems: Dict[str, Resistor] = dict()
        #make a dictionary for the load elements
        self.loadItems: Dict[str, Load] = dict()jj
        System.SystemCount += 1

    def add_bus(self, bus):
        if bus not in self.buses.keys():
            self.buses[bus] = Bus(bus)
            self.buses_order.append(bus)

    def addGenerator(self, name, voltage, bus1):
        System.componentCount += 1
        self.generator = Generator(name, voltage, bus1)
        self.add_bus(bus1)
        self.generatorItems[name] = self.generator
        #access the bus in the buses dictionary with the key bus1 and set its voltage to V
        self.buses[bus1].setBusVoltage(voltage)
    def addResistorElement(self, name, bus1_name, bus2_name, ohms):
        System.componentCount += 1
        bus1 = Bus(bus1_name)
        bus2 = Bus(bus2_name)
        resistorObject = Resistor(name, bus1, bus2, ohms) #creates a resistor object within my System object
        self.rItems.append(resistorObject)
    def addLoadElement(self, name, bus_name, power, voltage):
        System.componentCount += 1
        bus1 = Bus(bus_name)
        loadObject = Load(name, bus1, power, voltage)
        self.loadItems.append(loadObject)