import pygame
from pygame.sprite import Sprite
from Gene import Gene
from doesCollide import DoesCollide

class Cell(Sprite):
    
    def __init__(self, CellSim):
        super().__init__()
        self.collide = DoesCollide
        self.CellSim = CellSim
        self.random = CellSim.random
        self.color = CellSim.random.randint(10, 255), CellSim.random.randint(10, 255), CellSim.random.randint(10, 255)
        self.cells = CellSim.cells
        self.gridWidth = CellSim.settings.gridLineWidth
        self.settings = CellSim.settings
        self.screen = CellSim.screen
        self.scrWidth = CellSim.screen_width
        self.scrHeight = CellSim.screen_height
        self.grid = CellSim.grid
        self.rect = pygame.Rect(0, 0 , self.grid.intervalCol, self.grid.intervalRow)
        self.pos = CellSim.random.randrange(0,len(self.grid.points))
        self.point = self.grid.points[self.pos]
        self.x = self.point.x
        self.y = self.point.y
        self.rect.center = self.x, self.y
        self.lastpoint = self.grid.points[-1]
        self.firstpoint = self.grid.points[0]
        self.cellpos = []
        self.prevPos = 0
        
        self.food = self.settings.amtOfFood


        self.genes = []
        for gene in range(0, self.settings.amtOfGenes):
            self.genes.append(Gene(self.CellSim))

    def reproduce(self, color, genes):
        self.color = color
        self.genes.clear()
        self.genes = genes

    def changeColor(self):
        self.color = self.random.randint(10, 255), self.random.randint(10, 255), self.random.randint(10, 255)

    def randPos(self):
        self.pos = self.random.randrange(0,len(self.grid.points))
        self.point = self.grid.points[self.pos]
        self.x = self.point.x
        self.y = self.point.y
        self.rect.center = self.x, self.y

    def move(self, direction):
        if (direction == 1 and not self.y == self.firstpoint.y and not self.collide.collideTop(self, self.rect, self.cellpos) and 0 <= (self.pos-self.settings.gridCollumns) <= len(self.grid.points)):
            self.pos -= self.settings.gridCollumns
            self.prevPos = 1
        if (direction == 2 and not self.x == self.lastpoint.x and not self.collide.collideRight(self, self.rect, self.cellpos) and 0 <= (self.pos + 1) <= len(self.grid.points)):
            self.pos += 1
            self.prevPos = 2
        if (direction == 3 and not self.y == self.lastpoint.y and not self.collide.collideBottom(self, self.rect, self.cellpos) and 0 <= (self.pos - 1) <= len(self.grid.points)):
            self.pos += self.settings.gridCollumns
            self.prevPos = 3
        if (direction == 4 and not self.x == self.firstpoint.x and not self.collide.collideLeft(self, self.rect, self.cellpos) and 0 <= (self.pos+self.settings.gridCollumns) <= len(self.grid.points)):
            self.pos -= 1
            self.prevPos = 4
        self.point = self.grid.points[self.pos]
        self.x = self.point.x
        self.y = self.point.y
        self.rect.center = self.x, self.y

    def upd(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, min(self.grid.intervalRow/2-2, self.grid.intervalCol/2-2))

    def checkPos(self, x, y):
        newCells = self.cells.copy()
        newCells.remove(self)
        for C in newCells:
            if (C.rect.centerx == x and C.rect.centery == y):
                return True
            else:
                return False

    def notOverlap(self):
        samepos = 0
        for cell in self.cellpos:
            if (self.rect.center == cell.center):
                samepos += 1
        if (samepos > 0):
            self.pos = self.random.randrange(0, len(self.grid.points))
            self.point = self.grid.points[self.pos]
            self.x = self.point.x
            self.y = self.point.y
            self.rect.center = self.x, self.y

    def hunger(self):
        if (self.settings.hunger):
            self.food -= 1


    def run(self, cellsrects):
        self.hunger()
        self.cellpos = cellsrects.copy()
        self.cellpos.remove(self.rect)
        self.notOverlap()
        self.runNodes()
        self.upd()


    '''Nodes'''
    def runNodes(self):
        for gene in self.genes:
            active = gene.initialNode
            thresh = 0
            if (self.lookUp(active)):
                thresh = 1
            elif (self.lookRight(active)):
                thresh = 1
            elif (self.lookDown(active)):
                thresh = 1
            elif (self.lookLeft(active)):
                thresh = 1
            elif (self.whereHor(active)):
                thresh = self.x/self.scrWidth
            elif (self.whereVert(active)):
                thresh = self.x/self.scrHeight
            elif (self.isTrue(active)):
                thresh = 1
            elif (self.isFalse(active)):
                thresh = 0


            if (gene.testThres(thresh)):
                active = gene.finalNode
                self.randMove(active)
                self.moveUp(active)
                self.moveRight(active)
                self.moveDown(active)
                self.moveLeft(active)
                self.doNothing(active)


    '''SensorNodes'''
    def lookUp(self, active):
        if (active == 1 and self.settings.lookUp):
            return self.collide.collideTop(self, self.rect, self.cellpos)
    def lookRight(self, active):
        if (active == 2 and self.settings.lookRight):
            return self.collide.collideRight(self, self.rect, self.cellpos)
    def lookDown(self, active):
        if (active == 3 and self.settings.lookDown):
            return self.collide.collideBottom(self, self.rect, self.cellpos)
    def lookLeft(self, active):
        if (active == 4 and self.settings.lookLeft):
            return self.collide.collideLeft(self, self.rect, self.cellpos)
    def whereVert(self, active):
        if (active == 5 and self.settings.whereVert):
            return True
    def whereHor(self, active):
        if (active == 6 and self.settings.whereHor):
            return True
    def isTrue(self, active):
        if (active == 7 and self.settings.isTrue):
            return True
    def isFalse(self, active):
        if (active == 8 and self.settings.isFalse):
            return True

    '''TriggerNodes'''
    def randMove(self, active):
        if (active == 1 and self.settings.moveRandom):
            self.move(self.random.randrange(1, 5))


    def moveUp(self, active):
        if (active == 2 and self.settings.moveUp):
            self.move(1)

    def moveRight(self, active):
        if (active == 3 and self.settings.moveRight):
            self.move(2)

    def moveDown(self, active):
        if (active == 4 and self.settings.moveDown):
            self.move(3)

    def moveLeft(self, active):
        if (active == 5 and self.settings.moveLeft):
            self.move(4)
    
    def doNothing(self, active):
        if (active == 6 and self.settings.doNothing):
            donith = 1
            donith/2 

