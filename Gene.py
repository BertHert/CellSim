class Gene:

    def __init__(self, CellSim):
        self.random = CellSim.random
        self.settings = CellSim.settings
        self.initialNode = self.random.randint(1, self.settings.amtOfSensorNodes)
        self.finalNode = self.random.randint(1, self.settings.amtOfTriggerNodes)
        self.thresSwitch = self.random.randint(0,1)
        self.threshold = self.random.random()

    def testThres(self, input):
        if (self.thresSwitch == 0):
            return self.reachThres(input)
        else:
            return self.belowThres(input)
            
    def reachThres(self, input):
        if (input >= self.threshold):
            return True
        else:
            return False

    def belowThres(self, input):
        if (input < self.threshold):
            return True
        else:
            return False

    def mutate(self):
        num = self.random.randint(1,4)
        if (num == 1):
            self.initialNode = self.random.randint(1, self.settings.amtOfSensorNodes)
        if (num == 2):
            self.threshold = self.random.random()
        if (num == 3):
            self.finalNode = self.random.randint(1, self.settings.amtOfTriggerNodes)
        if (num == 4):
            self.thresSwitch = self.random.randint(0,1)