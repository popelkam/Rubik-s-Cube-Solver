from side import Side
from cube import Cube

def main():
    cube = yellowCrossCube()
##    print("*"*40)
##    print("INITIAL CUBE STATE:")
##    printCube(cube)
##    print("*"*40)
##    cube.bottomTurn()
##    print("CUBE AFTER 'bottomTurn':")
##    printCube(cube)
##    cube.bottomInvert()
##    print("CUBE AFTER 'bottomInvert':")
##    printCube(cube)
    
def yellowCrossCube():
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
    topSide.setTopLeft('red')
    topSide.setTopCenter('yellow')
    topSide.setTopRight('green')
    topSide.setMiddleLeft('yellow')
    topSide.setMiddleCenter('yellow')
    topSide.setMiddleRight('yellow')
    topSide.setBottomLeft('orange')
    topSide.setBottomCenter('yellow')
    topSide.setBottomRight('green')
    return topSide

def makeFrontSide():
    frontSide = Side()
    frontSide.setTopLeft('yellow')
    frontSide.setTopCenter('orange')
    frontSide.setTopRight('orange')
    frontSide.setMiddleLeft('orange')
    frontSide.setMiddleCenter('orange')
    frontSide.setMiddleRight('orange')
    frontSide.setBottomLeft('orange')
    frontSide.setBottomCenter('orange')
    frontSide.setBottomRight('orange')
    return frontSide

def makeLeftSide():

    leftSide = Side()
    leftSide.setTopLeft('blue')
    leftSide.setTopCenter('green')
    leftSide.setTopRight('blue')
    leftSide.setMiddleLeft('green')
    leftSide.setMiddleCenter('green')
    leftSide.setMiddleRight('green')
    leftSide.setBottomLeft('green')
    leftSide.setBottomCenter('green')
    leftSide.setBottomRight('green')
    return leftSide

def makeRightSide():
    
    rightSide = Side()
    rightSide.setTopLeft('yellow')
    rightSide.setTopCenter('blue')
    rightSide.setTopRight('yellow')
    rightSide.setMiddleLeft('blue')
    rightSide.setMiddleCenter('blue')
    rightSide.setMiddleRight('blue')
    rightSide.setBottomLeft('blue')
    rightSide.setBottomCenter('blue')
    rightSide.setBottomRight('blue')
    return rightSide

def makeBackSide():

    backSide = Side()
    backSide.setTopLeft('red')
    backSide.setTopCenter('red')
    backSide.setTopRight('yellow')
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



def printCube(cube):
    print("*"*40)
    print("front:\n" + str(cube.getFront()))
    print("right:\n" + str(cube.getRight()))
    print("left:\n" + str(cube.getLeft()))
    print("top:\n" + str(cube.getTop()))
    print("bottom:\n" + str(cube.getBottom()))
    print("back:\n" + str(cube.getBack()))
    
    
main()
        

