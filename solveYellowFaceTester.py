"""
Author: Matthew Popelka
Project: solveYellowFaceTester.py
Description: Takes in several different rubik's cubes to solve the yellow side of the cube
             since the yellow tiles could be in multiple positions after solving the middle layer.
"""


from yellowCrossCube import yellowCrossCube,printCube
from yellowVShapeCube import vShapeCube
from yellowMiddleCube import middleYellowCube
from yellowHorzLineCube import horizontalLineCube
from solveYellowFace import solveYellowFace


def solveYellowFaceTester():
    #This tester contains several cubes that have different intial set ups of the 
    typesOfCube = [["Horizontal Line",horizontalLineCube()],["V Shape",vShapeCube()],
                   ["Middle Only",middleYellowCube()],["Yellow Cross",yellowCrossCube()]]
    
    for cubes in typesOfCube:
        print("*"*40)
        print("START STATE FOR: "+cubes[0])
        printCube(cubes[1])

        print("*"*40)
        print("SOLVED YELLOW CUBE STATE:")
        solveYellowFace(cubes[1])
        printCube(cubes[1])
        if cubes != typesOfCube[-1]:
            print("-"*60)
            print()


solveYellowFaceTester()
    
        

