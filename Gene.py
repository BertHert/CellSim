class Gene:

    def __init__(self, Cell):
        self.random = Cell.random
        self.settings = Cell.settings
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
        num = self.random.randint(0,100)
        posaThres = self.threshold
        if (num >= 0 and num <= 20):
            print("Changing IN")
            self.initialNode = self.random.randint(1, self.settings.amtOfSensorNodes)
        if (num >= 21 and num <= 50):
            print("Changing THR")
            posaThres += self.random.random() * self.random.randint(-1,1)
            if (posaThres <= 1 and posaThres >= 0):
                self.threshold = posaThres
            else:
                while(not posaThres <= 1 and not posaThres >= 0):
                    posaThres += self.random.random() * self.random.randint(-1,1)
                    if (posaThres <= 1 and posaThres >= 0):
                        self.threshold = posaThres
        if (num >= 51 and num <= 80):
            print("Changing FN")
            self.finalNode = self.random.randint(1, self.settings.amtOfTriggerNodes)
        if (num >= 81 and num <= 100):
            print("Changing TS")
            self.thresSwitch = self.random.randint(0,1)

    def printIt(self, number):
        if (self.thresSwitch == 0):
            switch = ">"
        else:
            switch = "<"
        print(str(number) + "| " + str(self.initialNode) + ":" + str(switch) + ":" + str(self.threshold) + ":" + str(self.finalNode))