class Settings:
    
    def __init__(self):
        self.fps = 100
        self.delay = False

        '''ScreenSettings'''
        self.scrWidth = 501
        self.scrHeight = 501

        '''GridSettings'''
        self.gridRows = 50
        self.gridCollumns = 50
        self.gridLineWidth = 0

        '''FoodSettings'''
        self.hunger = False
        self.amtOfFoodBlocks = 0

        '''CellSettings''' 
        self.survivalCondition = 2
        self.amtOfFood = 25
        self.genLength = 100
        self.amtOfCells = 50
        self.fixedSR = .1

        self.cellSpeed = 5
        
        self.amtOfSensorNodes = 7
        self.amtOfIMNodes = 4
        self.amtOfIMNodesRows = 5
        self.amtOfTriggerNodes = 6
        self.mutate = True
        self.chanceOfMut = .05
        self.chanceOfRepMut = .10
        self.randPosAfGen = True
        self.asexual = True

        '''SensorGeneToggle'''
        self.lookUp = True
        self.lookRight = True
        self.lookDown = True
        self.lookLeft = True
        self.whereVert = True
        self.whereHor = True
        self.whatTime = True

        '''TriggerGeneToggle'''
        self.moveRandom = True
        self.moveUp = True
        self.moveRight = True
        self.moveDown = True
        self.moveLeft = True
        self.doNothing = True