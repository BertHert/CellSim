import pygame

from Gene import Gene

class Cell():
    
    def __init__(self, CellSim, index):
        self.collide = CellSim.collide
        self.CellSim = CellSim
        self.random = CellSim.random
        self.color = CellSim.random.randint(0, 255), CellSim.random.randint(0, 255), CellSim.random.randint(0, 255)
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
        self.points = 0
        self.index = index
        
        self.food = self.settings.amtOfFood


        self.genes = []
        

    def mutate(self):
        keep = True
        while(keep):
            randGene = self.random.randrange(len(self.genes))
            genes = self.genes.copy()
            self.genes.clear()
            gene = genes[randGene]
            gene.mutate()
            self.chgGenes(genes)
            self.color = self.random.randint(0, 255), self.random.randint(0, 255), self.random.randint(0, 255)
            randnum = self.random.random()
            if (randnum > self.settings.chanceOfRepMut):
                keep = False

    def reproduce(self):
        cell = Cell(self.CellSim, self.index)
        newGenes = []
        for gene in self.genes:
            nwGene = Gene(self.CellSim, gene.initialNode, gene.finalNode)
            nwGene.setTresh(gene.threshold)
            newGenes.append(nwGene)
        cell.chgGenes(newGenes)
        cell.chgColor(self.color)
        return cell


    def chgGenes(self, genes):
        self.genes.clear()
        copy  = genes.copy()
        for gene in copy:
            self.genes.append(gene)

    def chgGene(self, index, gene):
        self.genes[index] = gene

    def chgColor(self, color):
        self.color = color

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

    def addPoint(self):
        self.points += 1

    def clearPoints(self):
        self.points = 0

    def randPos(self):
        self.pos = self.random.randrange(0,len(self.grid.points))
        self.point = self.grid.points[self.pos]
        self.x = self.point.x
        self.y = self.point.y
        self.rect.center = self.x, self.y

    def move(self, direction):
        if (direction == 1 and self.rect.centery - self.settings.cellSpeed >= self.firstpoint.y):
            if(self.settings.collisions):
                if(not self.collide.collideTop(self.rect, self.cellpos)):
                    self.rect.centery -= self.settings.cellSpeed
                    self.prevPos = 1
            else:
                self.rect.centery -= self.settings.cellSpeed
                self.prevPos = 1
        if (direction == 2 and self.rect.centerx + self.settings.cellSpeed <= self.lastpoint.x):
            if(self.settings.collisions):
                if(not self.collide.collideRight(self.rect, self.cellpos)):
                    self.rect.centerx += self.settings.cellSpeed
                    self.prevPos = 2
            else:
                self.rect.centerx += self.settings.cellSpeed
                self.prevPos = 2
            
        if (direction == 3 and self.rect.centery + self.settings.cellSpeed <= self.lastpoint.y):
            if(self.settings.collisions):
                if(not self.collide.collideBottom(self.rect, self.cellpos)):
                    self.rect.centery += self.settings.cellSpeed
                    self.prevPos = 3
            else:
                self.rect.centery += self.settings.cellSpeed
                self.prevPos = 3

            
        if (direction == 4 and self.rect.centerx - self.settings.cellSpeed >= self.firstpoint.x):
            if(self.settings.collisions):
                if(not self.collide.collideLeft(self.rect, self.cellpos)):
                    self.rect.centerx -= self.settings.cellSpeed
                    self.prevPos = 4
            else:
                self.rect.centerx -= self.settings.cellSpeed
                self.prevPos = 4
            

    def upd(self):
        black = 0,0,0
        pygame.draw.circle(self.screen, self.color, self.rect.center, min(self.grid.intervalRow/2-2, self.grid.intervalCol/2-2))
        pygame.draw.circle(self.screen, black, self.rect.center, min(self.grid.intervalRow/2-2, self.grid.intervalCol/2-2), 1)
        
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
