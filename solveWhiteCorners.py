"""
File: solveWhiteCorners.py
Author: Davien Schweitzer
Description: Takes a cube with the white cross completed and solves the white
corners.
"""

from cube import Cube

# white: top, yellow: bottom, red: front, green: left, blue: right, orange: back'

def solveWhiteCorners(cube):
    
    whiteCornersList = [['white1', 'orange3', 'green1'], # top back left
                    ['white3', 'blue3', 'orange1'], # top back right
                    ['white6', 'green3', 'red1'], # top front left
                    ['white9', 'blue1', 'red3']] # top front right
    
    while(incorrectBottom(cube, whiteCornersList)):
        for corner in findCorners('bottom', theCube):
            handleBottom(corner, cube, whiteCornersList)
    while(incorrectTop(cube, whiteCornersList)):
        for corner in findCorners('top', theCube):
            handleTop(corner)
    if incorrectCube(cube):
        solveWhiteCorners(cube)

def incorrectCube(theCube, whiteCorners):
    if findCorners('top', theCube) == whiteCorners:
        return false
    return true

def incorrectBottom(theCube, whiteCorners):
    for corner in findCorners('bottom', theCube):
        if 'white' in corner: #just colors, no numbers, right?
            return true
    return false


def findCorners(face, theCube):
    if face == 'top':
        return [[theCube.getTop.getTopLeft(), theCube.getBack.getTopRight(), theCube.getLeft.getTopLeft()],
               [theCube.getTop.getTopRight(), theCube.getRight.getTopRight(), theCube.getBack.getTopLeft()],
                [theCube.getTop.getBottomLeft(), theCube.getLeft.getTopRight(), theCube.getFront.getTopLeft()],
                [theCube.getTop.getBottomRight(), theCube.getRight.getTopLeft(), theCube.getFront.getTopRight()]]

    elif face == 'bottom':
        return [[theCube.getBottom.getTopLeft(), theCube.getLeft.getBottomLeft(), theCube.getBack.getBottomRight()], #bottom top left
                [theCube.getBottom.getTopRight(), theCube.getRight.getBottomRight(), theCube.getBack.getBottomLeft()], #bottom top right
                [theCube.getBottom.getBottomLeft(), theCube.getLeft.getBottomRight(), theCube.getFront.getBottomLeft()], #bottom bottom left
                [theCube.getBottom.getBottomRight(), theCube.getRight.getBottomLeft(), theCube.getFront.getBottomRight()]] #bottom bottom right
        

def handleBottom(corner, theCube, whiteCorners):
    if 'white' not in corner:
        return
    # elif corner is under the correct top corner
    # else (corner is not under the correct corner)

def handleTop(corner, theCube, whiteCorners):
    return

'''
Things we need to check
1) if on top
    a. in correct position, colors and pattern
    b. in correct position, colors not pattern
    c. in wrong position

2. if on bottom
    a. in correct bottom position
    b. in wrong bottom position

function1: inCorrect
function2: handle bottom (checks first if in correct bottom position then fixes returns T
function3: handle top (if in wrong position, turn to correct color spot then handle case b)
function4: 
topFrontLeft, topFrontRight, topBackLeft, topBackRight
bottomFrontLeft, bottomFrontRight, bottomBackLeft, bottomBackRight
^Necessary for all of these functions??
'''



