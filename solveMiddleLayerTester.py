"""
File: solveMiddleLayerTester.py
Author: Carson Turner
Description: Tests solveMiddleLayer.py
"""

from solveMiddleLayer import solveMiddleLayer
from solveWhiteCross import solveWhiteCross
from testingCube import initCube, printCube
import random

def solveMiddleLayerTester():
    cube = initCube()

    print("*"*40)
    print("INITIAL CUBE STATE:")
    printCube(cube)

    messUpCube(cube)
    print("*"*40)
    print("PRE-SOLVE CUBE STATE:")
    printCube(cube)

    solveWhiteCross(cube)
    print("*"*40)
    print("WHITE CROSS SOVLED CUBE STATE:")
    printCube(cube)

    solveMiddleLayer(cube)
    print("*"*40)
    print("MIDDLE LAYER SOVLED CUBE STATE:")
    printCube(cube)

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

solveMiddleLayerTester()
