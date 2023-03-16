from System import System
from Solution import Solution

system = System("system", 200000000, 230000)
system.add_geometry("geometry1", -19.5, 30, 0, 30, 19.5, 30)
system.add_conductor("partridge", 0.642, 0.0217, 0.385)
system.add_bundle("main", 2, 1.5, system.conductors["partridge"])
system.add_transmissionLineData("mainLine", system.bundles["main"], system.geometries["geometry1"], system.conductors["partridge"])
system.add_transmissionLine("L1", "bus2", "bus4", system.transmissionlineDataItems["mainLine"], 10)
system.add_transmissionLine("L2", "bus2", "bus3", system.transmissionlineDataItems["mainLine"], 25)
system.add_transmissionLine("L3", "bus3", "bus5", system.transmissionlineDataItems["mainLine"], 20)
system.add_transmissionLine("L4", "bus4", "bus6", system.transmissionlineDataItems["mainLine"], 20)
system.add_transmissionLine("L5", "bus5", "bus6", system.transmissionlineDataItems["mainLine"], 10)
system.add_transmissionLine("L6", "bus4", "bus5", system.transmissionlineDataItems["mainLine"], 35)
system.add_transformerData("Tx1data", 125000000, 20000, 230000, 0.085, 10)
system.add_transformerData("Tx2data", 200000000, 18000, 230000, 0.105, 12)
system.add_transformer("Tx1", "bus1", "bus2", system.transformerdataItems["Tx1data"])
system.add_transformer("Tx2", "bus6", "bus7", system.transformerdataItems["Tx2data"])

ybusmatrix = Solution(system)



