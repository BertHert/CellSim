class Survival:
     
    def __init__(self, CellSim):
        self.CellSim = CellSim

    def condition(self, cell):
        if (225 < cell.rect.x < 525):
            return True
        else:
            return False
    
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
        if (225 < cell.rect.x < 525):
            return True
        else:
            return False