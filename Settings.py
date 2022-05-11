class Settings:
    
    def __init__(self):
        self.fps = 10
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
        self.survivalCondition = 1
        self.amtOfFood = 25
        self.genLength = 100
        self.amtOfCells = 25
        self.fixedSR = .1

        self.cellSpeed = 10
        
        self.amtOfSensorNodes = 7
        self.amtOfIMNodes = 8
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

    def chgSettings(self, main):
        while(True):
            input1 = int(input("1: Change Settings  \n2: Restart\n3: Quit\n"))

            if(input1 == 1):
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
                            "\n1: scrWidth: "+ str(self.scrWidth) +
                            "\n2: scrHeight: " + str(self.scrHeight) +
                            "\n3: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: scrWidth = "))
                                self.scrWidth = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: scrHeight = "))
                                self.scrHeight = input1
                            elif(input1 == 3):
                                break
                    
                    elif(input1 == 2):
                        while(True):
                            print("\nGrid Settings" +
                            "\n1: gridRows: " + str(self.gridRows) +
                            "\n2: gridCollumns: " + str(self.gridCollumns) +
                            "\n3: gridLineWidth: " + str(self.gridLineWidth) +
                            "\n4: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: gridRows = "))
                                self.gridRows = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: gridCollumns = "))
                                self.gridCollumns = input1
                            elif(input1 == 3):
                                input1 = int(input("\n3: gridLineWidth = "))
                                self.gridLineWidth = input1
                            elif(input1 == 4):
                                break
                    
                    elif(input1 == 3):
                        while(True):
                            print("\nFood Settings" +
                            "\n1: hunger: " + str(self.hunger) +
                            "\n2: amtOfFoodBlocks: " + str(self.amtOfFoodBlocks) +
                            "\n3: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: hunger = T/F")
                                if(input1.lower == "t"):
                                    self.hunger = True
                                elif(input1.lower == "f"):
                                    self.hunger = False
                            elif(input1 == 2):
                                input1 = int(input("\n2: amtOfFoodBlocks = "))
                                self.amtOfFoodBlocks = input1
                            elif(input1 == 3):
                                break
                    
                    elif(input1 == 4):
                        while(True):
                            print("\nCell Settings" +
                            "\n1: amtOfStartFood: " + str(self.amtOfFood) +
                            "\n2: genLength: " + str(self.genLength) +
                            "\n3: amtOfCells: " + str(self.amtOfCells) +
                            "\n4: fixedSR: " + str(self.fixedSR) +
                            "\n5: amtOfIMNodes: " + str(self.amtOfIMNodes) +
                            "\n6: mutate: " + str(self.mutate) +
                            "\n7: chanceOfMut: " + str(self.chanceOfMut) +
                            "\n8: chanceOfRepMut: " + str(self.chanceOfRepMut) +
                            "\n9: randPosAfGen: " + str(self.randPosAfGen) +
                            "\n10: survivalCondition: " + str(self.survivalCondition) +
                            "\n11: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = int(input("\n1: amtOfStartFood = "))
                                self.amtOfStartFood = input1
                            elif(input1 == 2):
                                input1 = int(input("\n2: genLength = "))
                                self.genLength = input1
                            elif(input1 == 3):
                                input1 = int(input("\n3: amtOfCells = "))
                                self.amtOfCells = input1
                            elif(input1 == 4):
                                input1 = float(input("\n4: fixedSR = "))
                                self.fixedSR = input1
                            elif(input1 == 5):
                                input1 = int(input("\n5: amtOfIMNodes = "))
                                self.amtOfIMNodes = input1
                            elif(input1 == 6):
                                input1 = input("\n6: mutate = T/F")
                                if(input1.lower == "t"):
                                    self.mutate = True
                                elif(input1.lower == "f"):
                                    self.mutate = False
                            elif(input1 == 7):
                                input1 = float(input("\n7: chanceOfMut = "))
                                self.chanceOfMut = input1
                            elif(input1 == 8):
                                input1 = float(input("\n8: chanceOfRepMut = "))
                                self.chanceOfRepMut = input1
                            elif(input1 == 9):
                                input1 = input("\n9: randPosAfGen = T/F")
                                if(input1.lower == "t"):
                                    self.randPosAfGen = True
                                elif(input1.lower == "f"):
                                    self.randPosAfGen = False
                            elif(input1 == 10):
                                input1 = int(input("\n10: survivalCondition = \n1: moveRight\n2: inMiddle\n"))
                                self.survivalCondition = input1
                            elif(input1 == 11):
                                break
                    
                    elif(input1 == 5):
                        while(True):
                            print("\nSensor Gene Toggle" +
                            "\n1: lookUp: " + str(self.lookUp) +
                            "\n2: lookRight: " + str(self.lookRight) +
                            "\n3: lookDown: " + str(self.lookDown) +
                            "\n4: lookLeft: " + str(self.lookLeft) +
                            "\n5: whereVert: " + str(self.whereVert) +
                            "\n6: whereHor: " + str(self.whereHor) +
                            "\n7: whatTime: " + str(self.whatTime) +
                            "\n8: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: lookUp = T/F")
                                if(input1.lower == "t"):
                                    self.lookUp = True
                                elif(input1.lower == "f"):
                                    self.lookUp = False
                            elif(input1 == 2):
                                input1 = input("\n2: lookRight = T/F")
                                if(input1.lower == "t"):
                                    self.lookRight = True
                                elif(input1.lower == "f"):
                                    self.lookRight = False
                            elif(input1 == 3):
                                input1 = input("\n3: lookDown = T/F")
                                if(input1.lower == "t"):
                                    self.lookDown = True
                                elif(input1.lower == "f"):
                                    self.lookDown = False
                            elif(input1 == 4):
                                input1 = input("\n4: lookLeft = T/F")
                                if(input1.lower == "t"):
                                    self.lookLeft = True
                                elif(input1.lower == "f"):
                                    self.lookLeft = False
                            elif(input1 == 5):
                                input1 = input("\n5: whereVert = T/F")
                                if(input1.lower == "t"):
                                    self.whereVert = True
                                elif(input1.lower == "f"):
                                    self.whereVert = False
                            elif(input1 == 6):
                                input1 = input("\n6: whereHor = T/F")
                                if(input1.lower == "t"):
                                    self.whereHor = True
                                elif(input1.lower == "f"):
                                    self.whereHor = False
                            elif(input1 == 7):
                                input1 = input("\n7: whatTime = T/F")
                                if(input1.lower == "t"):
                                    self.whatTime = True
                                elif(input1.lower == "f"):
                                    self.whatTime = False
                            elif(input1 == 8):
                                break
                    
                    elif(input1 == 6):
                        while(True):
                            print("\nTrigger Gene Toggle" +
                            "\n1: moveRandom: " + str(self.moveRandom) +
                            "\n2: moveUp: " + str(self.moveUp) +
                            "\n3: moveRight: " + str(self.moveRight) +
                            "\n4: moveDown: " + str(self.moveDown) +
                            "\n5: moveLeft: " + str(self.moveLeft) +
                            "\n6: doNothing: " + str(self.doNothing) +
                            "\n7: back")
                            input1 = int(input("\n"))
                            if(input1 == 1):
                                input1 = input("\n1: moveRandom = T/F")
                                if(input1.lower == "t"):
                                    self.moveRandom = True
                                elif(input1.lower == "f"):
                                    self.moveRandom = False
                            if(input1 == 2):
                                input1 = input("\n2: moveUp = T/F")
                                if(input1.lower == "t"):
                                    self.moveUp = True
                                elif(input1.lower == "f"):
                                    self.moveUp = False
                            if(input1 == 3):
                                input1 = input("\n3: moveRight = T/F")
                                if(input1.lower == "t"):
                                    self.moveRight = True
                                elif(input1.lower == "f"):
                                    self.moveRight = False
                            if(input1 == 4):
                                input1 = input("\n4: moveDown = T/F")
                                if(input1.lower == "t"):
                                    self.moveDown = True
                                elif(input1.lower == "f"):
                                    self.moveDown = False
                            if(input1 == 5):
                                input1 = input("\n5: moveLeft = T/F")
                                if(input1.lower == "t"):
                                    self.moveLeft = True
                                elif(input1.lower == "f"):
                                    self.moveLeft = False
                            if(input1 == 6):
                                input1 = input("\n6: doNothing = T/F")
                                if(input1.lower == "t"):
                                    self.doNothing = True
                                elif(input1.lower == "f"):
                                    self.doNothing = False
                            if(input1 == 7):
                                break
                    elif(input1 == 7):
                        break
            elif(input1 == 2):
                return True
            elif(input1 == 3):
                return False
