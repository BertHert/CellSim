class Gene:

    def __init__(self, CellSim, iN, fN):
        self.random = CellSim.random
        self.settings = CellSim.settings
        self.initialNode = iN
        self.finalNode = fN
        self.threshold = self.random.randrange(0, 10)

    def run(self, cell):
        value = self.initialNode.run(cell)
        value *= self.threshold
        self.finalNode.add(value)


    def mutate(self): 
        posaThres = self.threshold  
        posaThres += self.random.random() * self.random.randint(-1,1)
        if (posaThres <= 10 and posaThres >= -10):
            self.threshold = posaThres
        else:
            while(not posaThres <= 10 and not posaThres >= -10):
                posaThres += self.random.random() * self.random.randint(-1,1)
                if (posaThres <= 10 and posaThres >= -10):
                    self.threshold = posaThres
        

    def printIt(self, number):
        print(str(number) + "| " + str(self.initialNode.active) + ":" + str(self.threshold) + ":" + str(self.finalNode.active))