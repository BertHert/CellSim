import pygame
from point import Point

class Grid:

    def __init__(self, cellSim, rows, collumns, width):
        self.screen = cellSim.screen
        self.settings = cellSim.settings
        self.scrWidth = cellSim.screen_width
        self.scrHeight = cellSim.screen_height
        self.scrRect = cellSim.screen.get_rect()
        self.rows = rows
        self.collumns = collumns
        self.intervalCol = int(self.scrWidth/collumns)
        self.intervalRow = int(self.scrWidth/rows)
        self.lineWidth = width
        self.points = []
        self.makeGridPoints()

    def makeGrid(self):
        black = 0, 0, 0
        for x in range(int(0 - self.lineWidth/2), self.scrWidth, self.intervalCol):
            strPos = x, 0
            endPos = x, self.scrHeight
            pygame.draw.line(self.screen, black, strPos, endPos, self.lineWidth)

        for y in range(int(0 - self.lineWidth/2), self.scrHeight, self.intervalRow):
            strPos = 0, y
            endPos = self.scrWidth, y
            pygame.draw.line(self.screen, black, strPos, endPos, self.lineWidth)

    def getFirstPointX(self):
        return self.intervalCol/2

    def getFirstPointY(self):
        return self.intervalRow/2

    def makeGridPoints(self):
        y = self.getFirstPointY()
        
        for col in range(1, self.settings.gridCollumns+1):  
            x = self.getFirstPointX()      
            for row in range(1, self.settings.gridRows+1):
                point = Point(x,y)
                self.points.append(point)
                x += self.intervalCol
            y += self.intervalRow