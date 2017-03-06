from side import Side
from cube import Cube

def main():
    cube = initCube()

    print("*"*40)
    print("INITIAL CUBE STATE:")
    print(cube)

    print("*"*40)
    cube.orientCube("yellow","orange")
    print("CUBE AFTER 'orientCube(yellow, orange':")
    print(cube)

    cube.orientCube("white","red")
    print("CUBE AFTER 'orientCube(white,red)':")
    print(cube)

def initCube():
    aSide = makeSide("white")
    bSide = makeSide("red")
    cSide = makeSide("blue")
    dSide = makeSide("green")
    eSide = makeSide("yellow")
    fSide = makeSide("orange")
    
    
    cube1 = Cube()
    cube1.setTop(aSide)
    cube1.setFront(bSide)
    cube1.setRight(cSide)
    cube1.setLeft(dSide)
    cube1.setBottom(eSide)
    cube1.setBack(fSide)
    return cube1

def makeSide(color):
    aSide = Side()
    aSide.setTopLeft(color + "1")
    aSide.setTopCenter(color + "2")
    aSide.setTopRight(color + "3")
    aSide.setMiddleLeft(color + "4")
    aSide.setMiddleCenter(color + "5")
    aSide.setMiddleRight(color + "6")
    aSide.setBottomLeft(color + "7")
    aSide.setBottomCenter(color + "8")
    aSide.setBottomRight(color + "9")
    return aSide

def printCube(cube):
    print("*"*40)
    print("\nfront:\n" + str(cube.getFront()))
    print("\nright:\n" + str(cube.getRight()))
    print("\nleft:\n" + str(cube.getLeft()))
    print("\ntop:\n" + str(cube.getTop()))
    print("\nbottom:\n" + str(cube.getBottom()))
    print("\nback:\n" + str(cube.getBack()))
    
main()    
