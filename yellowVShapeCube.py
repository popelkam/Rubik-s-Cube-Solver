from side import Side
from cube import Cube

def main():
    cube = vShapeCube()

def vShapeCube():
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
    topSide.setTopCenter('orange')
    topSide.setTopRight('orange')
    topSide.setMiddleLeft('yellow')
    topSide.setMiddleCenter('yellow')
    topSide.setMiddleRight('green')
    topSide.setBottomLeft('yellow')
    topSide.setBottomCenter('yellow')
    topSide.setBottomRight('orange')
    return topSide

def makeFrontSide():
    frontSide = Side()
    frontSide.setTopLeft('green')
    frontSide.setTopCenter('blue')
    frontSide.setTopRight('yellow')
    frontSide.setMiddleLeft('orange')
    frontSide.setMiddleCenter('orange')
    frontSide.setMiddleRight('orange')
    frontSide.setBottomLeft('orange')
    frontSide.setBottomCenter('orange')
    frontSide.setBottomRight('orange')
    return frontSide

def makeLeftSide():
    leftSide = Side()
    leftSide.setTopLeft('red')
    leftSide.setTopCenter('red')
    leftSide.setTopRight('red')
    leftSide.setMiddleLeft('green')
    leftSide.setMiddleCenter('green')
    leftSide.setMiddleRight('green')
    leftSide.setBottomLeft('green')
    leftSide.setBottomCenter('green')
    leftSide.setBottomRight('green')
    return leftSide

def makeRightSide():
    rightSide = Side()
    rightSide.setTopLeft('green')
    rightSide.setTopCenter('yellow')
    rightSide.setTopRight('blue')
    rightSide.setMiddleLeft('blue')
    rightSide.setMiddleCenter('blue')
    rightSide.setMiddleRight('blue')
    rightSide.setBottomLeft('blue')
    rightSide.setBottomCenter('blue')
    rightSide.setBottomRight('blue')
    return rightSide

def makeBackSide():

    backSide = Side()
    backSide.setTopLeft('yellow')
    backSide.setTopCenter('yellow')
    backSide.setTopRight('blue')
    backSide.setMiddleLeft('red')
    backSide.setMiddleCenter('red')
    backSide.setMiddleRight('red')
    backSide.setBottomLeft('red')
    backSide.setBottomCenter('red')
    backSide.setBottomRight('red')
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
