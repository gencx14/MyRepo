class Bus:
    #Class Attribute
    busCount = 0
    Bus.swingCount = 0
    Bus.pq_count = 0
    Bus.pv_count = 0
    def __init__(self, name, vk = None, delta1 = None, pk = None, qk = None, type = None): #where should I set the bus voltage
        self.index = Bus.busCount
        self.name = name
        self.type = None
        self.vk = vk
        self.delta1 = delta1
        self.pk = pk
        self.qk = qk
        Bus.busCount += 1
        self.type = type
        self.getBusTypeCount()

    def getBusTypeCount(self):
        if self.type == "Slack":
            Bus.slackCount += 1
        elif self.type == "Load":
            Bus.load_count += 1
        elif self.type == "VC":
            Bus.vc_count += 1
        else:
            exit("Incorrect Bus Input Values for " + self.name)








