class Gene:

    def __init__(self, CellSim, iN, fN):
        self.random = CellSim.random
        self.settings = CellSim.settings
        self.initialNode = iN
        self.finalNode = fN
        self.threshold = self.random.random() * self.random.randint(-1,1)

    def run(self, cell):
        value = self.initialNode.run(cell)
        value *= self.threshold
        self.finalNode.add(value)


    def mutate(self): 
        posaThres = self.threshold  
        posaThres += self.random.random() * self.random.randint(-1,1)
<<<<<<< HEAD
        if (posaThres <= 1 and posaThres >= -1):
            self.threshold = posaThres
        else:
            while(not posaThres <= 1 and not posaThres >= -1):
                posaThres += self.random.random() * self.random.randint(-1,1)
                if (posaThres <= 1 and posaThres >= -1):
=======
        if (posaThres <= 10 and posaThres >= 0):
            self.threshold = posaThres
        else:
            while(not posaThres <= 10 and not posaThres >= 0):
                posaThres += self.random.random() * self.random.randint(-1,1)
                if (posaThres <= 1 and posaThres >= 0):
>>>>>>> parent of 37c51be (Add files via upload)
                    self.threshold = posaThres
        

    def printIt(self, number):
        print(str(number) + "| " + str(self.initialNode.active) + ":" + str(self.threshold) + ":" + str(self.finalNode.active))