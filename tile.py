class Tile:
    def __init__(self, aColor = None):
        self.color = aColor

    def getColor(self):
        return self.color
    
    def setColor(self, aColor):
        self.color = aColor

    def __str__(self):
        print(str(self.color))
        
