"""
File: solveWhiteCross.py
Author: Carson Turner
Description: Takes a scrambled cube and solves the white cross
"""


def solveWhiteCross(cube):
    #White cross consists of white2, white4, white6 and white8
    whiteCrossDict = {'white2':'orange2','white4':'green2','white6':'blue2','white8':'red2'}
    sideOrderCCW = {cube.getFront():cube.getRight(), cube.getLeft():cube.getFront(), cube.getRight():cube.getBack(), cube.getBack():cube.getLeft()}
    
    #Handle white2 first to set up refrence point for the cross
    target = 'white2'
    side = findEdge(target, cube)
    sideSecond = findEdge(whiteCrossDict[target], cube)
    #White tile is on top of the cube
    
    #White tile is on bottom of the cube
    if side == cube.getBottom():
        rotateSide(sideSecond, cube)
        rotateSide(sideSecond, cube)

    #White tile is on one of the four sides
    elif side != cube.getTop():
        #White tile is middle-top
        if sideSecond == cube.getTop():
            rotateSide(side, cube)
            sideSecond = findEdge(whiteCrossDict[target], cube)
            rotateSide(sideSecond, cube)
            
        #White tile is middle-bottom
        elif sideSecond == cube.getBottom():
            rotateSide(side, cube)
            sideSecond = findEdge(whiteCrossDict[target], cube)
            rotateInvert(sideSecond, cube)
            
        #White tile is middle-middle
        else:
            sideSecond = findEdge(whiteCrossDict[target], cube)
            if target == side.getMiddleLeft():
                rotateInvert(sideSecond, cube)
            else:
                rotateSide(sideSecond, cube)

    #else: white is on top and is already in place
                    
    previousTile = whiteCrossDict[target]

    #Handle the rest of the white cross
    #Looks similar to previous step but includes positionTop function
    for target in ['white6','white8','white4']:
        side = findEdge(target, cube)
        sideSecond = findEdge(whiteCrossDict[target], cube)
        
        #White tile is on top of the cube
        if side == cube.getTop():
            rotateSide(sideSecond, cube)
            positionTop(sideOrderCCW[sideSecond], previousTile, cube)
            rotateInvert(sideSecond, cube)
        
        #White tile is on bottom of the cube
        elif side == cube.getBottom():
            positionTop(sideOrderCCW[sideSecond], previousTile, cube)
            rotateSide(sideSecond, cube)
            rotateSide(sideSecond, cube)

        #White tile is on one of the four sides
        else:
            #White tile is middle-top
            if sideSecond == cube.getTop():
                rotateSide(side, cube)
                sideSecond = findEdge(whiteCrossDict[target], cube)
                positionTop(sideOrderCCW[sideSecond], previousTile, cube)
                rotateSide(sideSecond, cube)
            
            #White tile is middle-bottom
            elif sideSecond == cube.getBottom():
                positionTop(sideOrderCCW[side], previousTile, cube)
                rotateSide(side, cube)
                cube.topTurn()
                sideSecond = findEdge(whiteCrossDict[target], cube)
                rotateInvert(sideSecond, cube)
            
            #White tile is middle-middle
            else:
                sideSecond = findEdge(whiteCrossDict[target], cube)
                if target == side.getMiddleLeft():
                    positionTop(sideOrderCCW[sideSecond], previousTile, cube)
                    rotateInvert(sideSecond, cube)
                else:
                    positionTop(sideOrderCCW[sideSecond], previousTile, cube)
                    rotateSide(sideSecond, cube)
                    
        previousTile = whiteCrossDict[target]

    #Orient the white cross to finish
    while cube.getTop().getTopCenter() != 'white2':
        cube.topTurn()

#Find which side a desired edge tile is on
def findEdge(target, cube):
    for side in [cube.getFront(),cube.getLeft(),cube.getRight(),cube.getBack(),cube.getTop(),cube.getBottom()]:
        for tile in [side.getTopCenter(),side.getMiddleLeft(),side.getMiddleRight(),side.getBottomCenter()]:
            if tile == target:
                return side

#Turn a given side
def rotateSide(side, cube):
    if side == cube.getTop():
        cube.topTurn()
    elif side == cube.getFront():
        cube.frontTurn()
    elif side == cube.getLeft():
        cube.leftTurn()
    elif side == cube.getRight():
        cube.rightTurn()
    elif side == cube.getBack():
        cube.backTurn()
    else:
        cube.bottomTurn()

#Inverse turn of a given side    
def rotateInvert(side, cube):
    if side == cube.getTop():
        cube.topInvert()
    elif side == cube.getFront():
        cube.frontInvert()
    elif side == cube.getLeft():
        cube.leftInvert()
    elif side == cube.getRight():
        cube.rightInvert()
    elif side == cube.getBack():
        cube.backInvert()
    else:
        cube.bottomInvert()

#Takes in the side that will be rotated, and a tile to be used for orientation
def positionTop(targetSide, previousSecondTile, cube):
    previousSideSecond = findEdge(previousSecondTile, cube)
    while  not (previousSideSecond == targetSide):
        cube.topTurn()
        previousSideSecond = findEdge(previousSecondTile, cube)
    
