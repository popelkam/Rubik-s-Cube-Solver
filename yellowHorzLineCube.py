from side import Side
from cube import Cube

def main():
    cube = horizontalLineCube()
    
def horizontalLineCube():
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
    topSide.setTopCenter('green')
    topSide.setTopRight('green')
    topSide.setMiddleLeft('yellow')
    topSide.setMiddleCenter('yellow')
    topSide.setMiddleRight('yellow')
    topSide.setBottomLeft('red')
    topSide.setBottomCenter('red')
    topSide.setBottomRight('orange')
    return topSide

def makeFrontSide():
    frontSide = Side()
    frontSide.setTopLeft('yellow')
    frontSide.setTopCenter('yellow')
    frontSide.setTopRight('blue')
    frontSide.setMiddleLeft('green')
    frontSide.setMiddleCenter('green')
    frontSide.setMiddleRight('green')
    frontSide.setBottomLeft('green')
    frontSide.setBottomCenter('green')
    frontSide.setBottomRight('green')
    return frontSide

def makeLeftSide():
    leftSide = Side()
    leftSide.setTopLeft('red')
    leftSide.setTopCenter('orange')
    leftSide.setTopRight('green')
    leftSide.setMiddleLeft('red')
    leftSide.setMiddleCenter('red')
    leftSide.setMiddleRight('red')
    leftSide.setBottomLeft('red')
    leftSide.setBottomCenter('red')
    leftSide.setBottomRight('red')
    return leftSide

def makeRightSide():
    rightSide = Side()
    rightSide.setTopLeft('yellow')
    rightSide.setTopCenter('blue')
    rightSide.setTopRight('orange')
    rightSide.setMiddleLeft('orange')
    rightSide.setMiddleCenter('orange')
    rightSide.setMiddleRight('orange')
    rightSide.setBottomLeft('orange')
    rightSide.setBottomCenter('orange')
    rightSide.setBottomRight('orange')
    return rightSide

def makeBackSide():

    backSide = Side()
    backSide.setTopLeft('yellow')
    backSide.setTopCenter('yellow')
    backSide.setTopRight('blue')
    backSide.setMiddleLeft('blue')
    backSide.setMiddleCenter('blue')
    backSide.setMiddleRight('blue')
    backSide.setBottomLeft('blue')
    backSide.setBottomCenter('blue')
    backSide.setBottomRight('blue')
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
