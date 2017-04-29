from side import Side
from cube import Cube

def main():
    cube = middleYellowCube()

def middleYellowCube():
    topSide = makeTopSide()
    frontSide = makeFrontSide()
    leftSide = makeLeftSide()
    rightSide = makeRightSide()
    backSide = makeBackSide()
    bottomSide = makeBottomSide()
    
    
    cube1 = Cube()
    cube1.setTop(topSide)
    cube1.setFront(frontSide)
    cube1.setRight(rightSide)
    cube1.setLeft(leftSide)
    cube1.setBottom(bottomSide)
    cube1.setBack(backSide)
    return cube1


def makeTopSide():
    topSide = Side()
    topSide.setTopLeft('yellow')
    topSide.setTopCenter('blue')
    topSide.setTopRight('orange')
    topSide.setMiddleLeft('red')
    topSide.setMiddleCenter('yellow')
    topSide.setMiddleRight('green')
    topSide.setBottomLeft('yellow')
    topSide.setBottomCenter('orange')
    topSide.setBottomRight('red')
    return topSide

def makeFrontSide():
    frontSide = Side()
    frontSide.setTopLeft('red')
    frontSide.setTopCenter('yellow')
    frontSide.setTopRight('green')
    frontSide.setMiddleLeft('blue')
    frontSide.setMiddleCenter('blue')
    frontSide.setMiddleRight('blue')
    frontSide.setBottomLeft('blue')
    frontSide.setBottomCenter('blue')
    frontSide.setBottomRight('blue')
    return frontSide

def makeLeftSide():
    leftSide = Side()
    leftSide.setTopLeft('blue')
    leftSide.setTopCenter('yellow')
    leftSide.setTopRight('blue')
    leftSide.setMiddleLeft('orange')
    leftSide.setMiddleCenter('orange')
    leftSide.setMiddleRight('orange')
    leftSide.setBottomLeft('orange')
    leftSide.setBottomCenter('orange')
    leftSide.setBottomRight('orange')
    return leftSide

def makeRightSide():
    rightSide = Side()
    rightSide.setTopLeft('yellow')
    rightSide.setTopCenter('yellow')
    rightSide.setTopRight('yellow')
    rightSide.setMiddleLeft('red')
    rightSide.setMiddleCenter('red')
    rightSide.setMiddleRight('red')
    rightSide.setBottomLeft('red')
    rightSide.setBottomCenter('red')
    rightSide.setBottomRight('red')
    return rightSide

def makeBackSide():
    backSide = Side()
    backSide.setTopLeft('green')
    backSide.setTopCenter('yellow')
    backSide.setTopRight('orange')
    backSide.setMiddleLeft('green')
    backSide.setMiddleCenter('green')
    backSide.setMiddleRight('green')
    backSide.setBottomLeft('green')
    backSide.setBottomCenter('green')
    backSide.setBottomRight('green')
    return backSide

def makeBottomSide():
    

    bottomSide = Side()
    bottomSide.setTopLeft('white')
    bottomSide.setTopCenter('white')
    bottomSide.setTopRight('white')
    bottomSide.setMiddleLeft('white')
    bottomSide.setMiddleCenter('white')
    bottomSide.setMiddleRight('white')
    bottomSide.setBottomLeft('white')
    bottomSide.setBottomCenter('white')
    bottomSide.setBottomRight('white')
    return bottomSide
