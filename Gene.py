class Gene:

    def __init__(self, CellSim, iN, fN):
        self.random = CellSim.random
        self.settings = CellSim.settings
        self.initialNode = iN
        self.finalNode = fN
        self.threshold = self.random.random()

    def run(self, cell):
        value = self.initialNode.run(cell)
        value *= self.threshold
        self.finalNode.add(value)


    def mutate(self): 
        self.threshold = self.random.randrange(0, 10)
        """posaThres = self.threshold  
        posaThres += self.random.random() * self.random.randint(-1,1)
        if (posaThres <= 1 and posaThres >= 0):
            self.threshold = posaThres
        else:
            while(not posaThres <= 10 and not posaThres >= 0):
                posaThres += self.random.random() * self.random.randint(-1,1)
                if (posaThres <= 1 and posaThres >= 0):
                    self.threshold = posaThres"""
        

    def printIt(self, number):
        if (self.thresSwitch == 0):
            switch = ">"
        else:
            switch = "<"
        print(str(number) + "| " + str(self.initialNode) + ":" + str(switch) + ":" + str(self.threshold) + ":" + str(self.finalNode))