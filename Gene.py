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
        self.threshold  = self.random.random() * self.random.randint(-1,1)
        

    def printIt(self, number):
        print(str(number) + "| " + str(self.initialNode.active) + ":" + str(self.threshold) + ":" + str(self.finalNode.active))

    def setTresh(self, thresh):
        self.threshold = thresh