"""
File: solveWhiteCrossTester.py
Author: Carson Turner
Description: Tests solveWhiteCross.py
"""

from solveWhiteCross import solveWhiteCross, findEdge
from testingCube import initCube, printCube
import random

def solveWhiteCrossTester():
    cube = initCube()
    file = open("WhiteCrossTestFile.txt","w")

##    print(findEdge('white2', cube))
##    print(findEdge('white4', cube))

    print("*"*40)
    print("INITIAL CUBE STATE:")
    printCube(cube)

    messUpCube(cube)
    print("*"*40)
    print("PRE-SOLVE CUBE STATE:")
    printCube(cube)

##    print("*"*40)
##    print(findEdge('white2', cube))
##    if (findEdge('white2', cube) == cube.getTop()):
##        print('True')
##    else:
##        print('False')
##    print(findEdge('white4', cube))
##    findEdge('white4', cube) == cube.getFront()
##    print(findEdge('white6', cube))
##    findEdge('white6', cube) == cube.getTop()
##    print(findEdge('white8', cube))
##    findEdge('white8', cube) == cube.getRight()

    solveWhiteCross(cube, file)
    print("*"*40)
    print("WHITE CROSS SOVLED CUBE STATE:")
    printCube(cube)
    file.close()

def messUpCube(cube):
    random.seed()
    for i in range(20):
        print("Messing up the cube...")
        move = random.randint(0,5)
        if move == 0:
            cube.topTurn()
        elif move == 1:
            cube.frontTurn()
        elif move == 2:
            cube.leftTurn()
        elif move == 3:
            cube.rightTurn()
        elif move == 4:
            cube.backTurn()
        else:
            cube.bottomTurn()

solveWhiteCrossTester()
