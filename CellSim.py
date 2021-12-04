import sys
import pygame
from Settings import Settings
from Grid import Grid
from Cell import Cell
import random
from Gene import Gene
from Stats import Stats
from Survival import Survival

class CellSim:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.random = random
        self.gene = Gene
        self.cellrects = []
        self.clock = pygame.time.Clock()
        self.stats = Stats()
        self.survival = Survival(self)

        self.screen_width = self.settings.scrWidth
        self.screen_height = self.settings.scrHeight
        self.size = width, height = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.size)
        self.screenRect = self.screen.get_rect()
        self.cells = []
        
        self.grid = Grid(self, self.settings.gridRows, self.settings.gridCollumns, self.settings.gridLineWidth)
        for x in range(0,self.settings.amtOfCells):
            self.cells.append(Cell(self))

        

    def run_game(self):
        frames = 0
        while True:
            if (frames == 100):
                frames = 0
                print("FPS: " + str(int(self.clock.get_fps()*10)/10))
                self.stats.addGen()
                self.nextGen()
            if (self.settings.delay):
                self.clock.tick(self.settings.fps)
            else:
                self.clock.tick(0)
            
            self._check_events()
            self.updPos()
            self.update_screen()
            frames += 1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("______________________________________")
                print("Amount Of Gens:")
                print(self.stats.amountOfGens)
                print("Survival Rate:")
                print(self.stats.survivalRate)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            for cell in self.cells:
                cell.move(1)
            
        if event.key == pygame.K_LEFT:
            for cell in self.cells:
                cell.move(4)
            
        if event.key == pygame.K_RIGHT:
            for cell in self.cells:
                cell.move(2)

        if event.key == pygame.K_DOWN:
            for cell in self.cells:
                cell.move(3)

    def updPos(self):
        self.cellrects = []
        for cell in self.cells:
            self.cellrects.append(cell.rect)

    def survivalList(self):
        survived = []
        for cell in self.cells:
            if (self.survival.condition(cell)):
                survived.append(cell)
        return survived


    def nextGen(self):
        survived = self.survivalList()
        self.stats.addStat(int(len(survived)/len(self.cells)*1000)/10)
        print("SR: " + str(int(len(survived)/len(self.cells)*1000)/10) + "%")
        print("______________________________________")
        print("Gen " + str(self.stats.amountOfGens))
        nextGen = []
        for cell in survived:
            nextGen.append(cell)
        while (len(nextGen) < len(self.cells)):
            cell1I = self.random.randint(0, len(survived)-1)
            cell2I = self.random.randint(0, len(survived)-1)
            cell1 = survived[cell1I]
            cell2 = survived[cell2I]
            genes = []
            x = 0
            if (self.settings.asexual):
                 genes = cell1.genes
            else:
                while(len(genes)<self.settings.amtOfGenes):
                    gene = cell1.genes[x]
                    genes.append(gene)
                    if (len(genes) < self.settings.amtOfGenes and not self.settings.asexual):
                        gene = cell2.genes[x+1]
                        genes.append(gene)
                    x += 1
            
            whichCell = self.random.randint(1,2)
            if (whichCell == 1):
                color = cell1.color
            else:
                color = cell2.color
            randnum = self.random.random()*100
            if (randnum <= self.settings.chanceOfMut):
                randGene = self.random.randint(0, len(genes)-1)
                gene = genes[randGene]
                gene.mutate()
                color = self.random.randint(10, 255), self.random.randint(10, 255), self.random.randint(10, 255)
            newCell = Cell(self)
            newCell.reproduce(color, genes)
            nextGen.append(newCell)       
        self.cells.clear
        self.cells = nextGen
        print("Amount Of Cells")
        print(len(self.cells))
        if (self.settings.randPosAfGen):
            for cell in self.cells:
                cell.randPos()
            

    def update_screen(self):

        color = 97, 237, 223
        self.screen.fill(color)
        self.grid.makeGrid()
        self.random.shuffle(self.cells)
        
        
        for cell in self.cells:
            cell.run(self.cellrects)
        pygame.display.flip()

if __name__ == '__main__':
    cs = CellSim()
    cs.run_game()