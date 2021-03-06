from cgitb import lookup


class Nodes:

    def __init__(self, CellSim, assignment, active):
        self.CellSim = CellSim
        self.settings = CellSim.settings
        self.sum = 0
        self.assignment = assignment
        self.active = active


    def run(self, cell):
        if(self.assignment == 1):
            active = self.active
            thresh = 0
            if (active == 1 and self.settings.lookUp):
                thresh = self.tf(self.lookUp(cell))
            elif (active == 2 and self.settings.lookRight):
                thresh = self.tf(self.lookRight(cell))
            elif (active == 3 and self.settings.lookDown):
                thresh = self.tf(self.lookDown(cell))
            elif (active == 4 and self.settings.lookLeft):
                thresh = self.tf(self.lookDown(cell))
            elif (self.whereHor(active, cell)):
                thresh = cell.x/self.settings.scrWidth
            elif (self.whereVert(active, cell)):
                thresh = cell.x/self.settings.scrHeight
            elif (self.whatTime(active, cell)):
                thresh = self.CellSim.frames/self.settings.genLength
            return thresh
        if(self.assignment == 2):
            return self.sum
        if(self.assignment == 3):
            active = self.active
            self.randMove(active, cell)
            self.moveUp(active, cell)
            self.moveRight(active, cell)
            self.moveDown(active, cell)
            self.moveLeft(active, cell)
            self.doNothing(active, cell)

    def add(self, value):
        self.sum += value

    def clearSum(self):
        self.sum = 0


    '''SensorNodes'''
    def lookUp(self, cell):
        return cell.collide.collideTop(cell.rect, cell.cellpos)
    def lookRight(self, cell):
        return cell.collide.collideRight(cell.rect, cell.cellpos)
    def lookDown(self, cell):
        return cell.collide.collideBottom(cell.rect, cell.cellpos)
    def lookLeft(self, cell):
        return cell.collide.collideLeft(cell.rect, cell.cellpos)
    def whereVert(self, active, cell):
        if (active == 5 and self.settings.whereVert):
            return True
    def whereHor(self, active, cell):
        if (active == 6 and self.settings.whereHor):
            return True
    def whatTime(self, active, cell):
        if (active == 7 and self.settings.whatTime):
            return True

    '''TriggerNodes'''
    def randMove(self, active, cell):
        if (active == 1 and self.settings.moveRandom):
            cell.move(cell.random.randrange(1, 5))
    def moveUp(self, active, cell):
        if (active == 2 and self.settings.moveUp):
            cell.move(1)
    def moveRight(self, active, cell):
        if (active == 3 and self.settings.moveRight):
            cell.move(2)
    def moveDown(self, active, cell):
        if (active == 4 and self.settings.moveDown):
            cell.move(3)
    def moveLeft(self, active, cell):
        if (active == 5 and self.settings.moveLeft):
            cell.move(4)
    def doNothing(self, active, cell):
        if (active == 6 and self.settings.doNothing):
            donith = 1
            donith/2 

    def tf(self, b):
        if(b):
            return 1
        else:
            return 0