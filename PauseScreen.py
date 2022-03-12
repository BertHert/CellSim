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
        while True:
            input1 = int(input("1: Grab Cell \n2: Quit \n3: Done\n"))
            if(input1 == 1):
                input1 = input("Which cell to grab: ")
                print("Cell "+ input1)
                cell = self.CellSim.cells[int(input1)]
                genes = self.CellSim.cells[int(input1)].genes.copy()
                num = 1
                for gene in genes:
                    gene.printIt(num)
                    num += 1
                input2 = input("Do you want to mutate? y/n\n")
                if(input2.lower() == "y"):
                    cell.mutate()
            elif (input1 == 2):
                input2 = int(input("Are you sure? \n1: Yes \n2: No\n"))
                if (input2 == 1):
                    return False
                else:
                    return True
            elif(input1 == 3):
                self.CellSim.paused = False
