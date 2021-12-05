import pygame


class Wall:

    def __init__(self, CellSim, x, y, width, height):
        self.CellSim = CellSim
        self.settings = CellSim.settings
        self.screen = CellSim.screen
        self.pos = x + y * self.settings.gridCollumns
        self.width = width
        self.height = height
        self.grid = CellSim.grid
        self.rects = []
        self.make()
        
        

    def make(self):
        pos = self.pos
        for y in range(0, self.height):
            for x in range(0, self.width):
                rect = pygame.Rect(0, 0, self.grid.intervalCol, self.grid.intervalRow)
                point = self.grid.points[pos]
                rect.center = point.x, point.y
                self.rects.append(rect)
                pos += 1
            pos += self.settings.gridCollumns - 1

    def run(self):
        color = 0, 0, 0
        for rect in self.rects:
            pygame.draw.rect(self.screen, color, rect)