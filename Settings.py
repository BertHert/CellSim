class Settings:
    
    def __init__(self):
        self.fps = 20
        self.delay = False

        '''ScreenSettings'''
        self.scrWidth = 751
        self.scrHeight = 751

        '''GridSettings'''
        self.gridRows = 50
        self.gridCollumns = 50
        self.gridLineWidth = 2

        '''FoodSettings'''
        self.hunger = False
        self.amtOfFoodBlocks = 0

        '''CellSettings''' 
        self.amtOfFood = 25
        self.genLength = 100
        self.amtOfCells = 150
        
        self.amtOfSensorNodes = 7
        self.amtOfIMNodes = 3
        self.amtOfTriggerNodes = 6
        self.mutate = True
        self.chanceOfMut = 5
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