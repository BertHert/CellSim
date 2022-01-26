class Stats:

    def __init__(self):
        self.survivalRate = []
        self.amountOfGens = 1
        self.run = 1
        self.points = []
        self.bestCell = 0

    def addStat(self, SR):
        self.survivalRate.append(SR)

    def addGen(self):
        self.amountOfGens += 1
    
    def addRun(self):
        self.run += 1

    def addPoints(self, point):
        self.points.append(point)

    def setBestCell(self, cell):
        self.bestCell = cell