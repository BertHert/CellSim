class Survival:
     
    def __init__(self, CellSim):
        self.CellSim = CellSim
        self.settings = CellSim.settings

    def condition(self, cell):
        active = self.settings.survivalCondition

        if(active == 1):
            return self.moveRight(cell)
        elif(active == 2):
            return self.inMiddle(cell)
    
    def isSaftey(self, cell):
        r = 212
        g = 121
        b = 36
        isR = 20 > abs(cell.color[0] - r)
        isG = 20 > abs(cell.color[1] - g)
        isB = 20 > abs(cell.color[2] - b)
        if (isR and isG and isB):
            return True
        else:
            return False

    def moveRight(self, cell):
        if (600 < cell.rect.x):
            return True
        else:
            return False

    def inMiddle(self, cell):
        gap = 255
        if (gap < cell.rect.x < self.settings.scrWidth - gap):
            return True
        else:
            return False
    
    def outMiddle(self, cell):
        gap = 255
        if (gap < cell.rect.y > self.settings.scrWidth - gap):
            return True
        else:
            return False