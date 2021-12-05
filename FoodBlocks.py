import pygame

class FoodBlocks:

    def __init__(self, CellSim):
        self.CellSim = CellSim
        self.screen = CellSim.screen
        self.grid = CellSim.grid
        self.random = CellSim.random
        self.rect = pygame.Rect(0, 0 , self.grid.intervalCol, self.grid.intervalRow)
        self.color = 0, 255, 0
        self.pos = CellSim.random.randrange(0,len(self.grid.points))
        self.point = self.grid.points[self.pos]
        self.rect.centerx = self.point.x
        self.rect.centery = self.point.y
        self.food = self.random.randint(1, 100)


    def upd(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    