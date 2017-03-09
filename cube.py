"""
file: cube.py
author: Richard Roberts
Desc: a rubiks cube
"""


from side import Side

class Cube(Side):
    def __init__(self):
        self.front = Side()
        self.left = Side()
        self.right = Side()
        self.back = Side()
        self.top = Side()
        self.bottom = Side()

    #GETTERS
    def getFront(self):
        return self.front

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getBack(self):
        return self.back

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    #SETTERS
    def setFront(self, side):
        self.front = side

    def setLeft(self, side):
        self.left = side

    def setRight(self, side):
        self.right = side

    def setBack(self, side):
        self.back = side

    def setTop(self, side):
        self.top = side

    def setBottom(self, side):
        self.bottom = side
        
########################################################################
    #method to perform "right"
    #5 sides need to be changed
    def rightTurn(self):
        #saving top tiles
        topRight = self.top.getTopRight()
        middleRight = self.top.getMiddleRight()
        bottomRight = self.top.getBottomRight()

        #changing top from front(1 side changed)
        self.top.setTopRight(self.front.getTopRight())
        self.top.setMiddleRight(self.front.getMiddleRight())
        self.top.setBottomRight(self.front.getBottomRight())

        #changing front from bottom(2 side changed)
        self.front.setTopRight(self.bottom.getTopRight())
        self.front.setMiddleRight(self.bottom.getMiddleRight())
        self.front.setBottomRight(self.bottom.getBottomRight())

        #changing bottom from back(3 side changed)
        self.bottom.setTopRight(self.back.getBottomLeft())
        self.bottom.setMiddleRight(self.back.getMiddleLeft())
        self.bottom.setBottomRight(self.back.getTopLeft())

        #changing back from SAVED top tiles(4 side changed)
        self.back.setTopLeft(bottomRight)
        self.back.setMiddleLeft(middleRight)
        self.back.setBottomLeft(topRight)

        #rotating right side tiles(5 side changed)
        self.right.rotateRight()
        
#####################################################################

    def rightInvert(self):
        self.rightTurn()
        self.rightTurn()
        self.rightTurn()

#####################################################################

    def leftTurn(self):
        #saving top tiles
        topLeft = self.top.getTopLeft()
        middleLeft = self.top.getMiddleLeft()
        bottomLeft = self.top.getBottomLeft()
        
        #changing top from front
        self.top.setTopLeft(self.back.getBottomRight())
        self.top.setMiddleLeft(self.back.getMiddleRight())
        self.top.setBottomLeft(self.back.getTopRight())
        
        #changing back from bottom
        self.back.setTopRight(self.bottom.getBottomLeft())
        self.back.setMiddleRight(self.bottom.getMiddleLeft())
        self.back.setBottomRight(self.bottom.getTopLeft())
        
        #changing bottom from front
        self.bottom.setTopLeft(self.front.getTopLeft())
        self.bottom.setMiddleLeft(self.front.getMiddleLeft())
        self.bottom.setBottomLeft(self.front.getBottomLeft())
        
        #changing front from SAVED top tiles
        self.front.setTopLeft(topLeft)
        self.front.setMiddleLeft(middleLeft)
        self.front.setBottomLeft(bottomLeft)
        
        #rotating left side tiles
        self.left.rotateRight()

#####################################################################

    def leftInvert(self):
        self.leftTurn()
        self.leftTurn()
        self.leftTurn()

#####################################################################
    def frontTurn(self):
        #save top tiles
        bottomLeft = self.top.getBottomLeft()
        bottomCenter = self.top.getBottomCenter()
        bottomRight = self.top.getBottomRight()
        
        #change top from left
        self.top.setBottomLeft(self.left.getBottomRight())
        self.top.setBottomCenter(self.left.getMiddleRight())
        self.top.setBottomRight(self.left.getTopRight())
        
        #change left from bottom
        self.left.setTopRight(self.bottom.getTopLeft())
        self.left.setMiddleRight(self.bottom.getTopCenter())
        self.left.setBottomRight(self.bottom.getTopRight())
        
        #change bottom from right
        self.bottom.setTopLeft(self.right.getBottomLeft())
        self.bottom.setTopCenter(self.right.getMiddleLeft())
        self.bottom.setTopRight(self.right.getTopLeft())
        
        #change right from saved
        self.right.setTopLeft(bottomLeft)
        self.right.setMiddleLeft(bottomCenter)
        self.right.setBottomLeft(bottomRight)
        
        #rotate front
        self.front.rotateRight()

#####################################################################
    def frontInvert(self):
        self.frontTurn()
        self.frontTurn()
        self.frontTurn()

#####################################################################
    def backTurn(self):
        #save top tiles
        topLeft = self.top.getTopLeft()
        topCenter = self.top.getTopCenter()
        topRight = self.top.getTopRight()
        
        #change top from right
        self.top.setTopLeft(self.right.getTopRight())
        self.top.setTopCenter(self.right.getMiddleRight())
        self.top.setTopRight(self.right.getBottomRight())
        
        #change right from bottom
        self.right.setTopRight(self.bottom.getBottomRight())
        self.right.setMiddleRight(self.bottom.getBottomCenter())
        self.right.setBottomRight(self.bottom.getBottomLeft())
        
        #change bottom from left
        self.bottom.setBottomLeft(self.left.getTopLeft())
        self.bottom.setBottomCenter(self.left.getMiddleLeft())
        self.bottom.setBottomRight(self.left.getBottomLeft())
        
        #change left from saved
        self.left.setTopLeft(topRight)
        self.left.setMiddleLeft(topCenter)
        self.left.setBottomLeft(topLeft)
        
        #rotate back side
        self.back.rotateRight()

#####################################################################
    def backInvert(self):
        self.backTurn()
        self.backTurn()
        self.backTurn()

#####################################################################
    def topTurn(self):
        #save left tiles
        topLeft = self.left.getTopLeft()
        topCenter = self.left.getTopCenter()
        topRight = self.left.getTopRight()

        #change left from front
        self.left.setTopLeft(self.front.getTopLeft())
        self.left.setTopCenter(self.front.getTopCenter())
        self.left.setTopRight(self.front.getTopRight())

        #change front from right
        self.front.setTopLeft(self.right.getTopLeft())
        self.front.setTopCenter(self.right.getTopCenter())
        self.front.setTopRight(self.right.getTopRight())

        #change right from back
        self.right.setTopLeft(self.back.getTopLeft())
        self.right.setTopCenter(self.back.getTopCenter())
        self.right.setTopRight(self.back.getTopRight())

        #change back from left
        self.back.setTopLeft(topLeft)
        self.back.setTopCenter(topCenter)
        self.back.setTopRight(topRight)

        #rotate top
        self.top.rotateRight()

#####################################################################
    def topInvert(self):
        self.topTurn()
        self.topTurn()
        self.topTurn()

#####################################################################
    def bottomInvert(self):
        #save left tiles
        bottomLeft = self.left.getBottomLeft()
        bottomCenter = self.left.getBottomCenter()
        bottomRight = self.left.getBottomRight()
        
        #change left from front
        self.left.setBottomLeft(self.front.getBottomLeft())
        self.left.setBottomCenter(self.front.getBottomCenter())
        self.left.setBottomRight(self.front.getBottomRight())
        
        #change front from right
        self.front.setBottomLeft(self.right.getBottomLeft())
        self.front.setBottomCenter(self.right.getBottomCenter())
        self.front.setBottomRight(self.right.getBottomRight())
        
        #change right from back
        self.right.setBottomLeft(self.back.getBottomLeft())
        self.right.setBottomCenter(self.back.getBottomCenter())
        self.right.setBottomRight(self.back.getBottomRight())
        
        #change back from left
        self.back.setBottomLeft(bottomLeft)
        self.back.setBottomCenter(bottomCenter)
        self.back.setBottomRight(bottomRight)
                                               
        #rotate bottom
        self.bottom.rotateLeft()
        

#####################################################################
    def bottomTurn(self):
        self.bottomInvert()
        self.bottomInvert()
        self.bottomInvert()
    
#####################################################################

    def __str__(self):
        aString = ""
        aString += "*"*40
        aString += "\nfront:\n" + str(self.getFront())
        aString += "\nright:\n" + str(self.getRight())
        aString += "\nleft:\n" + str(self.getLeft())
        aString += "\ntop:\n" + str(self.getTop())
        aString += "\nbottom:\n" + str(self.getBottom())
        aString += "\nback:\n" + str(self.getBack())
        return aString

####################################################################
    def rollRight(self):
        #rotate front
        self.front.rotateRight()
        
        #rotate back
        self.back.rotateLeft()
        
        #save topSide
        savedSide = Side()
        savedSide.setTopLeft(self.top.getTopLeft())
        savedSide.setTopCenter(self.top.getTopCenter())
        savedSide.setTopRight(self.top.getTopRight())
        savedSide.setMiddleLeft(self.top.getMiddleLeft())
        savedSide.setMiddleCenter(self.top.getMiddleCenter())
        savedSide.setMiddleRight(self.top.getMiddleRight())
        savedSide.setBottomLeft(self.top.getBottomLeft())
        savedSide.setBottomCenter(self.top.getBottomCenter())
        savedSide.setBottomRight(self.top.getBottomRight())
        
        #move left to top
        self.setTop(self.getLeft())
        self.top.rotateRight()
        
        #move bottom to left
        self.setLeft(self.getBottom())
        self.left.rotateRight()
        
        #move right to bottom
        self.setBottom(self.getRight())
        self.bottom.rotateRight()
        
        #move saved top to right
        self.setRight(savedSide)
        self.right.rotateRight()

####################################################################
    def rollLeft(self):
        self.rollRight()
        self.rollRight()
        self.rollRight()

####################################################################

    def rollUp(self):
        #rotate left
        self.left.rotateLeft()
        
        #rotate right
        self.right.rotateRight()

        #save topSide
        savedSide = Side()
        savedSide.setTopLeft(self.top.getTopLeft())
        savedSide.setTopCenter(self.top.getTopCenter())
        savedSide.setTopRight(self.top.getTopRight())
        savedSide.setMiddleLeft(self.top.getMiddleLeft())
        savedSide.setMiddleCenter(self.top.getMiddleCenter())
        savedSide.setMiddleRight(self.top.getMiddleRight())
        savedSide.setBottomLeft(self.top.getBottomLeft())
        savedSide.setBottomCenter(self.top.getBottomCenter())
        savedSide.setBottomRight(self.top.getBottomRight())
        
        #move front to top
        self.setTop(self.getFront())
        
        #move bottom to front
        self.setFront(self.getBottom())
        
        #move back to bottom
        self.setBottom(self.getBack())
        self.bottom.rotateRight()
        self.bottom.rotateRight()
        
        #move saved top to back
        self.setBack(savedSide)
        self.back.rotateRight()
        self.back.rotateRight()


####################################################################

    def rollDown(self):
        self.rollUp()
        self.rollUp()
        self.rollUp()

####################################################################

    def orientCube(self, topColor, frontColor):
        #setting the front color
        frontCounter = 0
        while frontColor.lower() not in self.front.getMiddleCenter().lower():
            if frontCounter  == 3:
                frontCounter = 0
                self.rollRight()
            else:
                self.rollUp()
                frontCounter += 1
                
        #setting the top color
        topCounter = 0
        while topColor.lower() not in self.top.getMiddleCenter().lower():
            self.rollRight()
            topCounter += 1
            if topCounter == 5:
                break
    
