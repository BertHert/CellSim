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

class PauseScreen:

    def __init__(self, CellSim):
        self.CellSim = CellSim
        self.settings = CellSim.settings

    def run(self):
        while(True):
            input1 = int(input("1: Grab Cell \n2: Change Settings \n3: Restart and Apply Settings \n4: Done\n"))
            if(input1 == 1):
                input1 = input("Which cell to grab: ")
                print("Cell "+ input1)
                cell = self.CellSim.cells[int(input1)]
                genes = self.CellSim.cells[int(input1)].genes.copy()
                num = 1
                for gene in genes:
                    gene.printIt(num)
                    num += 1
                input1 = input("Do you want to mutate? y/n\n")
                if(input1.lower() == "y"):
                    cell.mutate()

            if(input1 == 2):
                while(True):
                    """Change Settings code"""
                    print("1: Screen Settings" +
                    "\n2: Grid Settings" +
                    "\n3: Food Settings" +
                    "\n4: Cell Settings" +
                    "\n5: Sensor Gene Toggle" +
                    "\n6: Trigger Gene Toggle" +
                    "\n7: back")
                    input1 = int(input("\n"))
                    if(input1 == 1):
                        while(True):
                            print("Screen Settings" +
                            "\n1: scrWidth: "+ str(self.settings.scrWidth) +
                            "\n2: scrHeight: " + str(self.settings.scrHeight) +
                            "\n3: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: scrWidth = "))
                                self.settings.scrWidth = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: scrHeight = "))
                                self.settings.scrHeight = input1
                            elif(input1 == 3):
                                break
                    
                    elif(input1 == 2):
                        while(True):
                            print("\nGrid Settings" +
                            "\n1: gridRows: " + str(self.settings.gridRows) +
                            "\n2: gridCollumns: " + str(self.settings.gridCollumns) +
                            "\n3: gridLineWidth: " + str(self.settings.gridLineWidth) +
                            "\n4: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: gridRows = "))
                                self.settings.gridRows = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: gridCollumns = "))
                                self.settings.gridCollumns = input1
                            elif(input1 == 3):
                                input1 = int(input("\n3: gridLineWidth = "))
                                self.settings.gridLineWidth = input1
                            elif(input1 == 4):
                                break
                    
                    elif(input1 == 3):
                        while(True):
                            print("\nFood Settings" +
                            "\n1: hunger: " + str(self.settings.hunger) +
                            "\n2: amtOfFoodBlocks: " + str(self.settings.amtOfFoodBlocks) +
                            "\n3: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: hunger = T/F")
                                if(input1.lower == "t"):
                                    self.settings.hunger = True
                                elif(input1.lower == "f"):
                                    self.settings.hunger = False
                            elif(input1 == 2):
                                input1 = int(input("\n2: amtOfFoodBlocks = "))
                                self.settings.amtOfFoodBlocks = input1
                            elif(input1 == 3):
                                break
                    
                    elif(input1 == 4):
                        while(True):
                            print("\nCell Settings" +
                            "\n1: amtOfStartFood: " + str(self.settings.amtOfFood) +
                            "\n2: genLength: " + str(self.settings.genLength) +
                            "\n3: amtOfCells: " + str(self.settings.amtOfCells) +
                            "\n4: fixedSR: " + str(self.settings.fixedSR) +
                            "\n5: amtOfIMNodes: " + str(self.settings.amtOfIMNodes) +
                            "\n6: mutate: " + str(self.settings.mutate) +
                            "\n7: chanceOfMut: " + str(self.settings.chanceOfMut) +
                            "\n8: chanceOfRepMut: " + str(self.settings.chanceOfRepMut) +
                            "\n9: randPosAfGen: " + str(self.settings.randPosAfGen) +
                            "\n10: survivalCondition: " + str(self.settings.survivalCondition) +
                            "\n11: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: amtOfStartFood = "))
                                self.settings.amtOfStartFood = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: genLength = "))
                                self.settings.genLength = input1
                            elif(input1 == 3):
                                input1 = int(input("\n3: amtOfCells = "))
                                self.settings.amtOfCells = input1
                            elif(input1 == 4):
                                input1 = float(input("\n4: fixedSR = "))
                                self.settings.fixedSR = input1
                            elif(input1 == 5):
                                input1 = int(input("\n5: amtOfIMNodes = "))
                                self.settings.amtOfIMNodes = input1
                            elif(input1 == 6):
                                input1 = input("\n6: mutate = T/F")
                                if(input1.lower == "t"):
                                    self.settings.mutate = True
                                elif(input1.lower == "f"):
                                    self.settings.mutate = False
                            elif(input1 == 7):
                                input1 = float(input("\n7: chanceOfMut = "))
                                self.settings.chanceOfMut = input1
                            elif(input1 == 8):
                                input1 = float(input("\n8: chanceOfRepMut = "))
                                self.settings.chanceOfRepMut = input1
                            elif(input1 == 9):
                                input1 = input("\n9: randPosAfGen = T/F")
                                if(input1.lower == "t"):
                                    self.settings.randPosAfGen = True
                                elif(input1.lower == "f"):
                                    self.settings.randPosAfGen = False
                            elif(input1 == 10):
                                input1 = int(input("\n10: survivalCondition = \n1: moveRight\n2: inMiddle\n"))
                                self.settings.survivalCondition = input1
                            elif(input1 == 11):
                                break
                    
                    elif(input1 == 5):
                        while(True):
                            print("\nSensor Gene Toggle" +
                            "\n1: lookUp: " + str(self.settings.lookUp) +
                            "\n2: lookRight: " + str(self.settings.lookRight) +
                            "\n3: lookDown: " + str(self.settings.lookDown) +
                            "\n4: lookLeft: " + str(self.settings.lookLeft) +
                            "\n5: whereVert: " + str(self.settings.whereVert) +
                            "\n6: whereHor: " + str(self.settings.whereHor) +
                            "\n7: whatTime: " + str(self.settings.whatTime) +
                            "\n8: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: lookUp = T/F")
                                if(input1.lower == "t"):
                                    self.settings.lookUp = True
                                elif(input1.lower == "f"):
                                    self.settings.lookUp = False
                            elif(input1 == 2):
                                input1 = input("\n2: lookRight = T/F")
                                if(input1.lower == "t"):
                                    self.settings.lookRight = True
                                elif(input1.lower == "f"):
                                    self.settings.lookRight = False
                            elif(input1 == 3):
                                input1 = input("\n3: lookDown = T/F")
                                if(input1.lower == "t"):
                                    self.settings.lookDown = True
                                elif(input1.lower == "f"):
                                    self.settings.lookDown = False
                            elif(input1 == 4):
                                input1 = input("\n4: lookLeft = T/F")
                                if(input1.lower == "t"):
                                    self.settings.lookLeft = True
                                elif(input1.lower == "f"):
                                    self.settings.lookLeft = False
                            elif(input1 == 5):
                                input1 = input("\n5: whereVert = T/F")
                                if(input1.lower == "t"):
                                    self.settings.whereVert = True
                                elif(input1.lower == "f"):
                                    self.settings.whereVert = False
                            elif(input1 == 6):
                                input1 = input("\n6: whereHor = T/F")
                                if(input1.lower == "t"):
                                    self.settings.whereHor = True
                                elif(input1.lower == "f"):
                                    self.settings.whereHor = False
                            elif(input1 == 7):
                                input1 = input("\n7: whatTime = T/F")
                                if(input1.lower == "t"):
                                    self.settings.whatTime = True
                                elif(input1.lower == "f"):
                                    self.settings.whatTime = False
                            elif(input1 == 8):
                                break
                    
                    elif(input1 == 6):
                        while(True):
                            print("\nTrigger Gene Toggle" +
                            "\n1: moveRandom: " + str(self.settings.moveRandom) +
                            "\n2: moveUp: " + str(self.settings.moveUp) +
                            "\n3: moveRight: " + str(self.settings.moveRight) +
                            "\n4: moveDown: " + str(self.settings.moveDown) +
                            "\n5: moveLeft: " + str(self.settings.moveLeft) +
                            "\n6: doNothing: " + str(self.settings.doNothing) +
                            "\n7: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: moveRandom = T/F")
                                if(input1.lower == "t"):
                                    self.settings.moveRandom = True
                                elif(input1.lower == "f"):
                                    self.settings.moveRandom = False
                            if(input1 == 2):
                                input1 = input("\n2: moveUp = T/F")
                                if(input1.lower == "t"):
                                    self.settings.moveUp = True
                                elif(input1.lower == "f"):
                                    self.settings.moveUp = False
                            if(input1 == 3):
                                input1 = input("\n3: moveRight = T/F")
                                if(input1.lower == "t"):
                                    self.settings.moveRight = True
                                elif(input1.lower == "f"):
                                    self.settings.moveRight = False
                            if(input1 == 4):
                                input1 = input("\n4: moveDown = T/F")
                                if(input1.lower == "t"):
                                    self.settings.moveDown = True
                                elif(input1.lower == "f"):
                                    self.settings.moveDown = False
                            if(input1 == 5):
                                input1 = input("\n5: moveLeft = T/F")
                                if(input1.lower == "t"):
                                    self.settings.moveLeft = True
                                elif(input1.lower == "f"):
                                    self.settings.moveLeft = False
                            if(input1 == 6):
                                input1 = input("\n6: doNothing = T/F")
                                if(input1.lower == "t"):
                                    self.settings.doNothing = True
                                elif(input1.lower == "f"):
                                    self.settings.doNothing = False
                            if(input1 == 7):
                                break
                    elif(input1 == 7):
                        break
            elif(input1 == 3):
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
                self.IMNodes = [[0 for i in range(self.settings.amtOfIMNodes)] for j in range(self.settings.amtOfIMNodesRows)]
                self.TNodes = []
                self.BNode = Nodes(self, 4, "B")
                active = 1
                while(len(self.SNodes) < self.settings.amtOfSensorNodes):
                    node = Nodes(self, 1, active)
                    self.SNodes.append(node)
                    self.nodes.append(node)
                    active += 1
                active = 1
                for row in range(len(self.IMNodes)):
                    for col in range(len(self.IMNodes[row])):
                        node = Nodes(self, 2,"IM-" + str(active))
                        self.IMNodes[row][col] = node
                        self.nodes.append(node)
                        active += 1
                

                """while(len(self.IMNodes) < self.settings.amtOfIMNodes):
                    node = Nodes(self, 2,"IM" + str(active))
                    self.IMNodes.append(node)
                    self.nodes.append(node)
                    active += 1"""
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
                        for IMNode in self.IMNodes[0]:
                            cell.genes.append(Gene(self, sNode, IMNode))
                    for row in range(len(self.IMNodes)-1):
                        for col in range(len(self.IMNodes[row])):
                            node = self.IMNodes[row][col]
                            for IMNode in self.IMNodes[row+1]:
                                cell.genes.append(Gene(self, node, IMNode))
                    for Node in self.IMNodes[len(self.IMNodes)-1]:
                        for TNode in self.TNodes:
                            cell.genes.append(Gene(self, Node, TNode))
                    for TNode in self.TNodes:
                        cell.genes.append(Gene(self, self.BNode, TNode))
                    cellI += 1
                    self.cells.append(cell)

                print("Restarted")
            elif(input1 == 4):
                break

        self.CellSim.paused = False