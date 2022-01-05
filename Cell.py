import pygame

from Gene import Gene
from doesCollide import DoesCollide

class Cell():
    
    def __init__(self, CellSim):
        super().__init__()
        self.collide = DoesCollide
        self.CellSim = CellSim
        self.random = CellSim.random
        self.color = CellSim.random.randint(50, 255), CellSim.random.randint(50, 255), CellSim.random.randint(50, 255)
        self.cells = CellSim.cells
        self.nodes = CellSim.nodes
        self.TNodes = CellSim.TNodes
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
        

    def reproduce(self, color, genes):
        self.color = color
        self.genes = genes

    def printSelf(self):
        print(self.color)
        x = 1
        for gene in self.genes:
            gene.printIt(x)
            x += 1

    def getColor(self):
        return self.color

    def getGenes(self):
        return self.genes.copy()

    def randPos(self):
        self.pos = self.random.randrange(0,len(self.grid.points))
        self.point = self.grid.points[self.pos]
        self.x = self.point.x
        self.y = self.point.y
        self.rect.center = self.x, self.y

    def move(self, direction):
        if (direction == 1 and not self.y == self.firstpoint.y and not self.collide.collideTop(self.rect, self.cellpos) and 0 <= (self.pos-self.settings.gridCollumns) <= len(self.grid.points)):
            self.pos -= self.settings.gridCollumns
            self.prevPos = 1
        if (direction == 2 and not self.x == self.lastpoint.x and not self.collide.collideRight(self.rect, self.cellpos) and 0 <= (self.pos + 1) <= len(self.grid.points)):
            self.pos += 1
            self.prevPos = 2
        if (direction == 3 and not self.y == self.lastpoint.y and not self.collide.collideBottom(self.rect, self.cellpos) and 0 <= (self.pos - 1) <= len(self.grid.points)):
            self.pos += self.settings.gridCollumns
            self.prevPos = 3
        if (direction == 4 and not self.x == self.firstpoint.x and not self.collide.collideLeft(self.rect, self.cellpos) and 0 <= (self.pos+self.settings.gridCollumns) <= len(self.grid.points)):
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
        self.runNetwork()
        self.upd()


    '''Nodes'''
    def runNetwork(self):
        for node in self.nodes:
            node.clearSum()

        for gene in self.genes:
            gene.run(self)

        max = self.nodes[len(self.nodes)-1]
        for node in self.TNodes: 
            if(node.sum > max.sum):
                max = node
        max.run(self)
        for node in self.nodes:
            node.clearSum()
