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
from Nodes import Nodes
from PauseScreen import PauseScreen

class CellSim:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CellSim")
        self.settings = Settings()
        self.pauseScreen = PauseScreen(self)
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
        """self.walls.append(Wall(self, 18, 10, 1, 30))
        self.walls.append(Wall(self, 32, 10, 1, 30))"""
        print("Press ESC to access settings\n")
        
        """Make Nodes here"""
        self.nodes = []
        self.SNodes = []
        self.IMNodes = []
        self.TNodes = []
        active = 1
        while(len(self.SNodes) < self.settings.amtOfSensorNodes):
            node = Nodes(self, 1, active)
            self.SNodes.append(node)
            self.nodes.append(node)
            active += 1
        while(len(self.IMNodes) < self.settings.amtOfIMNodes):
            node = Nodes(self, 2,1)
            self.IMNodes.append(node)
            self.nodes.append(node)
        active = 1
        while(len(self.TNodes) < self.settings.amtOfTriggerNodes):
            node = Nodes(self, 3,active)
            self.TNodes.append(node)
            self.nodes.append(node)
            active += 1

        """Make Food Blocks""" 
        while(len(self.foodBlocks)< self.settings.amtOfFoodBlocks):
            self.foodBlocks.append(FoodBlock(self))

        """Make Cells and Genes"""
        while(len(self.cells)< self.settings.amtOfCells):
            cellI = 0
            cell = 0
            cell = Cell(self, cellI)
            for sNode in self.SNodes:
                for IMNode in self.IMNodes:
                    cell.genes.append(Gene(self, sNode, IMNode))
            for Node in self.IMNodes:
                for TNode in self.TNodes:
                    cell.genes.append(Gene(self, Node, TNode))
            cellI += 1
            self.cells.append(cell)

        

    def run_game(self):
        self.frames = 0
        while True:
            if (self.paused):
                self.pauseScreen.run()

            for cell in self.cells:
                if (cell.food <= 0):
                    self.cells.remove(cell)
                if (self.survival.condition(cell)):
                    cell.addPoint()
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
                print("Avg Points:")
                print(self.stats.points)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
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
        
    def sortCells(self, cell):
        return cell.points

    def survivalList(self):
        survived = []
        self.cells.sort(key = self.sortCells)
        self.cells.reverse()
        copyCell = self.cells.copy()
        notSur = self.cells.copy()
        x = 0
        for cell in self.cells:
            if(self.survival.condition(cell)):
                survived.append(copyCell[x])
                notSur.remove(cell)
            x += 1
                
        x = 0
        while (len(survived) < self.settings.fixedSR*self.settings.amtOfCells):
            survived.append(notSur[x])
            x += 1
        copyCell.clear()
        notSur.clear()
        return survived


    def nextGen(self):
        mutated = 0
        survived = self.survivalList().copy()
        cells = self.cells.copy()
        self.stats.addStat(int(len(survived)/len(self.cells)*1000)/10)
        self.prevSR = int(len(survived)/len(self.cells)*1000)/10
        print("SR: " + str(int(len(survived)/len(self.cells)*1000)/10) + "%")
        scoreT = 0
        for cell in cells:
            scoreT += cell.points
        avgScore = int(scoreT/len(cells))
        print("Avg Score: " + str(avgScore))
        
        if(len(self.stats.points) > 2 and avgScore > self.stats.points[-1]):
            bcell = cells[0]
            for cell in cells:
                if(cell.points > bcell.points):
                    bcell = cell
            self.stats.setBestCell(bcell)
        self.stats.addPoints(avgScore)
        
        for cell in cells:
            cell.clearPoints
        print("______________________________________")
        nextGen = []
        while (len(nextGen) < len(cells)):
            randnum = self.random.randint(0, len(survived)-1)
            parent = survived[randnum]
            cell = parent.reproduce()

            nextGen.append(cell)
        self.cells.clear() 
        cells.clear()     
        for x in range(len(nextGen)):
            cell = nextGen[x]
            randnum = self.random.random()
            if (randnum <= self.settings.chanceOfMut and self.settings.mutate):
                cell.mutate()
                mutated += 1
            self.cells.append(cell)
        nextGen.clear()
        if (self.settings.randPosAfGen):
            for cell in self.cells:
                cell.randPos()
        print("Mutated: " + str(mutated))

    def dataPrint(self):
        self.genFPS.append(int(self.clock.get_fps()*10)/10)
        if (self.frames == self.settings.genLength):
            print("Press ESC to access settings\n")
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


cs = CellSim()
cs.run_game()