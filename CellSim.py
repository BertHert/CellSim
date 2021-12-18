import sys
import pygame
from Settings import Settings
from Grid import Grid
from Cell import Cell
import random
from Gene import Gene
from Stats import Stats
from Survival import Survival
from FoodBlocks import FoodBlock
from Walls import Wall

class CellSim:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CellSim")
        self.settings = Settings()
        self.random = random
        self.gene = Gene
        self.cellrects = []
        self.collisionObjs = []
        self.clock = pygame.time.Clock()
        self.stats = Stats()
        self.survival = Survival(self)
        self.genFPS = []
        self.frames = 0
        self.prevSR = 0
        self.paused = False

        self.screen_width = self.settings.scrWidth
        self.screen_height = self.settings.scrHeight
        self.size = width, height = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.size)
        self.screenRect = self.screen.get_rect()
        self.grid = Grid(self, self.settings.gridRows, self.settings.gridCollumns, self.settings.gridLineWidth)
        self.cells = []
        self.foodBlocks = []
        self.walls = []
        """self.walls.append(Wall(self, 10, 10, 30, 1))
        self.walls.append(Wall(self, 10, 40, 30, 1))"""

        while(len(self.foodBlocks)< self.settings.amtOfFoodBlocks):
            self.foodBlocks.append(FoodBlock(self))

        while(len(self.cells)< self.settings.amtOfCells):
            cell = Cell(self)
            while(len(cell.genes) < self.settings.amtOfGenes):
                cell.genes.append(Gene(self))
            self.cells.append(cell)

        

    def run_game(self):
        self.frames = 0
        while True:
            if (self.paused):
                grabedCell = input("Which cell to grab: ")
                print("Cell "+ grabedCell)
                genes = self.cells[int(grabedCell)].genes.copy()
                num = 1
                for gene in genes:
                    gene.printIt(num)
                    num += 1
                self.paused = False

            for cell in self.cells:
                if (cell.food <= 0):
                    self.cells.remove(cell)
            self.dataPrint()
            self._check_events()
            self.updPos()
            self.update_screen()
            self.frames += 1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("======================================")
                print("Amount Of Gens:")
                print(self.stats.amountOfGens)
                print("Survival Rate:")
                print(self.stats.survivalRate)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_p:
            self.paused = True

    def updPos(self):
        self.collisionObjs = []
        self.cellrects = []
        for cell in self.cells:
            self.collisionObjs.append(cell.rect)
        for block in self.foodBlocks:
            self.collisionObjs.append(block.rect)
        for wall in self.walls:
            for seg in wall.rects:
                self.collisionObjs.append(seg)
        

    def survivalList(self):
        survived = []
        for cell in self.cells:
            if (self.survival.condition(cell)):
                survived.append(cell)
        return survived


    def nextGen(self):
        survived = self.survivalList()
        self.stats.addStat(int(len(survived)/len(self.cells)*1000)/10)
        self.prevSR = int(len(survived)/len(self.cells)*1000)/10
        print("SR: " + str(int(len(survived)/len(self.cells)*1000)/10) + "%")
        print("______________________________________")
        nextGen = []
        while (len(nextGen) < len(self.cells)):
            cell1I = self.random.randint(0, len(survived)-1)
            cell2I = self.random.randint(0, len(survived)-1)
            cell1 = survived[cell1I]
            cell2 = survived[cell2I]
            x = 0
            if (self.settings.asexual):
                genes = cell1.genes.copy()
            else:
                c1Genes = cell1.genes.copy()
                c2Genes = cell2.genes.copy()
                genes = []
                while(len(genes)<self.settings.amtOfGenes):
                    
                    gene = c1Genes[x]
                    genes.append(gene)
                    if (len(genes) < self.settings.amtOfGenes and not self.settings.asexual):
                        gene = c2Genes[x+1]
                        genes.append(gene)
                    x += 1
            
            whichCell = self.random.randint(1,2)
            if (self.settings.asexual):
                color = cell1.getColor()
            if (whichCell == 1):
                color = cell1.getColor()
            else:
                color = cell2.getColor()
            randnum = self.random.random()*100
            if (randnum <= self.settings.chanceOfMut and self.settings.mutate):
                randGene = self.random.randint(0, len(genes)-1)
                genes[randGene].mutate()
                print("Mutated")
                color = self.random.randint(0, 200), self.random.randint(0, 200), self.random.randint(0, 200)
            newCell = Cell(self)
            newCell.reproduce(color, genes.copy())
            genes.clear()
            nextGen.append(newCell)
            """newCell.printSelf()"""
        self.cells.clear()       
        for cell in nextGen:
            self.cells.append(cell)
        nextGen.clear()
        if (self.settings.randPosAfGen):
            for cell in self.cells:
                cell.randPos()

    def dataPrint(self):
        self.genFPS.append(int(self.clock.get_fps()*10)/10)
        if (self.frames == self.settings.genLength):
            print("")
            print("Gen " + str(self.stats.amountOfGens))
            fps = 0
            for ifps in self.genFPS:
                fps += ifps
            fps = fps/len(self.genFPS)
            self.genFPS = []
            self.frames = 0
            print("FPS: " + str(int(fps*10)/10))
            self.stats.addGen()
            self.nextGen()
        if (self.settings.delay):
            self.clock.tick(self.settings.fps)
        else:
            self.clock.tick(0)

    def textUpd(self):
        font1 = pygame.font.Font("D:/VSCode/PythonVSC/Cell/typwrterReg.ttf", 50)
        font2 = pygame.font.Font("D:/VSCode/PythonVSC/Cell/typwrterReg.ttf", 25)
        textColor1 = 87, 242, 15
        textColor2 = 24, 57, 110
        text = font1.render("Gen: "+ str(self.stats.amountOfGens) + " ", True, textColor1, textColor2)
        text2 = font2.render("Prev SR: "+ str(self.prevSR) + " ", True, textColor1, textColor2)
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        
        textRect.topleft = 0, -10
        textRect2.topleft = textRect.bottomleft
        textRect2.y += -5
        self.screen.blit(text2, textRect2)
        self.screen.blit(text, textRect)

    def update_screen(self):
        

        color = 97, 237, 223
        self.screen.fill(color)
        self.grid.makeGrid()
        self.random.shuffle(self.cells)

        for block in self.foodBlocks:
            block.upd()

        for wall in self.walls:
            wall.run()
        
        for cell in self.cells:
            cell.run(self.collisionObjs)
        
        self.textUpd()
        pygame.display.flip()

if __name__ == '__main__':
    cs = CellSim()
    cs.run_game()