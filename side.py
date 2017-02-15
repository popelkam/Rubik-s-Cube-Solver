from tile import Tile

class Side(Tile):
    def __init__(self):
        self.topLeft = Tile()
        self.topCenter = Tile()
        self.topRight = Tile()
        self.middleLeft = Tile()
        self.middleCenter = Tile()
        self.middleRight = Tile()
        self.bottomLeft = Tile()
        self.bottomCenter = Tile()
        self.bottomRight = Tile()

    
    #GETTERS
    def getTopLeft(self):
        return self.topLeft.getColor()

    def getTopCenter(self):
        return self.topCenter.getColor()

    def getTopRight(self):
        return self.topRight.getColor()

    def getMiddleLeft(self):
        return self.middleLeft.getColor()

    def getMiddleCenter(self):
        return self.middleCenter.getColor()

    def getMiddleRight(self):
        return self.middleRight.getColor()

    def getBottomLeft(self):
        return self.bottomLeft.getColor()

    def getBottomCenter(self):
        return self.bottomCenter.getColor()

    def getBottomRight(self):
        return self.bottomRight.getColor()
    
    #SETTERS
    def setTopLeft(self, aColor):
        self.topLeft.setColor(aColor)

    def setTopCenter(self, aColor):
        self.topCenter.setColor(aColor)

    def setTopRight(self, aColor):
        self.topRight.setColor(aColor)

    def setMiddleLeft(self, aColor):
        self.middleLeft.setColor(aColor)

    def setMiddleCenter(self, aColor):
        self.middleCenter.setColor(aColor)

    def setMiddleRight(self, aColor):
        self.middleRight.setColor(aColor)

    def setBottomLeft(self, aColor):
        self.bottomLeft.setColor(aColor)

    def setBottomCenter(self, aColor):
        self.bottomCenter.setColor(aColor)

    def setBottomRight(self, aColor):
        self.bottomRight.setColor(aColor)

    def rotateRight(self):
        topLeft = self.topLeft.getColor()
        self.topLeft.setColor(self.bottomLeft.getColor())
        self.bottomLeft.setColor(self.bottomRight.getColor())
        self.bottomRight.setColor(self.topRight.getColor())
        self.topRight.setColor(topLeft)

        topCenter = self.topCenter.getColor()
        self.topCenter.setColor(self.middleLeft.getColor())
        self.middleLeft.setColor(self.bottomCenter.getColor())
        self.bottomCenter.setColor(self.middleRight.getColor())
        self.middleRight.setColor(topCenter)

    def rotateLeft(self):
        self.rotateRight()
        self.rotateRight()
        self.rotateRight()

    def __str__(self):
        myString = "Top Row:    "
        myString += str(self.topLeft.getColor()) + " "
        myString += str(self.topCenter.getColor())+ " "
        myString += str(self.topRight.getColor())+ "\n"

        myString += "Middle Row: "
        myString += str(self.middleLeft.getColor()) + " "
        myString += str(self.middleCenter.getColor()) + " "
        myString += str(self.middleRight.getColor()) + "\n"

        myString += "Bottom Row: "
        myString += str(self.bottomLeft.getColor()) + " "
        myString += str(self.bottomCenter.getColor()) + " "
        myString += str(self.bottomRight.getColor()) + "\n"
        return myString

    
