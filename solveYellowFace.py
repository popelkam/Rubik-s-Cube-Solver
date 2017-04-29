"""
Author: Matthew Popelka
Project: solveYellowFace.py
Description: Takes in a rubik's cube after the middle layer has been solved and depending on yellow top
             apperance it will either apply turns on the cube to solve the yellow cross. Otherwise, if the
             yellow cross is solved then the cube will have a final set of turns applied to solve the cube.
"""


def solveYellowFace(cube):
    #puts the yellow middle tile at the top
    initCubeOrientation(cube)
    
    while True:
        cubeTop = [cube.getTop().getTopLeft(),cube.getTop().getTopCenter(),cube.getTop().getTopRight(),
                   cube.getTop().getMiddleLeft(),cube.getTop().getMiddleCenter(),cube.getTop().getMiddleRight(),
                   cube.getTop().getBottomLeft(),cube.getTop().getBottomCenter(),cube.getTop().getBottomRight()]
        #Gets the count of the number of yellows on the top
        count = yellowForFaceCount(cubeTop)
        
        if count == 9:
            break
        else:
            case = checkCases(cube,cubeTop,count)
            if case[0] == True:
                solveYellowTop(cube,cubeTop,count)
            elif case[1] == True:
                straightLine(cube)
            elif case[2] == True:
                #vShapeOrientation is used to have the yellow tiles in the shape of a
                #v in the top left or corner.
                vShapeOrientation(cube)
                vShapeOrMiddleYellow(cube)
            #vShapeOrMiddleYellow was used again because the algorithm uses the same
            #moves as the v shape cube tiles.
            elif case[3] == True:
                vShapeOrMiddleYellow(cube)

#Creates a case list to be used in the main function to help with
#calling the correct function depending on the cubes appearance.
def checkCases(cube,cubeTop,count):
    case = [False,False,False,False]
    
    if all(color == "yellow" for color in [cubeTop[1],cubeTop[3],cubeTop[5],cubeTop[7]]):
        case[0] = True
    elif all(color == "yellow" for color in [cubeTop[1],cubeTop[4],cubeTop[7]]):
        cube.rollUp()
        cube.rollRight()
        cube.rollDown()
        case[1] = True
    elif all(color == "yellow" for color in [cubeTop[3],cubeTop[4],cubeTop[5]]):
        case[1] = True
    elif "yellow" in [cubeTop[1],cubeTop[7]] and "yellow" in [cubeTop[3],cubeTop[5]]:
        case[2] = True
    else:
        case[3] = True
    return case

#Counts the number of yellow on top to break out of the program.
def yellowForFaceCount(cubeFace):
    count = 0
    for color in cubeFace:
        if 'yellow' in color:
            count+=1
    return count

#Calls functions to orient the cube depending on number of yellow tiles on top
#and calls the turns needed to solve the yellow face.
def solveYellowTop(cube,cubeTop,count):
    stepTwoCubeOrientation(cube,count)
    finalStageTurns(cube)

#Orients the cube after solving the yellow cross.       
def stepTwoCubeOrientation(cube,count):
    target = False
    cube.rollUp()
    
    while target == False:
        cube.rollRight()
        if cube.getTop().getTopLeft() == "yellow" and count >= 7:
            target = True
        elif cube.getBack().getTopRight() == "yellow" and count == 6:
            target = True
        elif cube.getTop().getTopRight() == "yellow" and count == 5:
            target = True
    cube.rollDown()

#Function to put the yellow center tile at the top.
def initCubeOrientation(cube):
    rollCount = 0
    
    while cube.getTop().getMiddleCenter() != "yellow":
        if rollCount == 4:
            cube.rollUp()
        cube.rollRight()
        rollCount += 1

#orients the cube putting the yellow v shape at the top left.
def vShapeOrientation(cube):
    targetOrientation = False
    cube.rollDown()
    
    while targetOrientation == False:
        vOrienList = [cube.getFront().getTopCenter(),cube.getFront().getMiddleLeft(),
                      cube.getFront().getMiddleRight(),cube.getFront().getMiddleCenter()]
        vCount = yellowForFaceCount(vOrienList)
        if vCount == 3:
            targetOrientation = True
            cube.rollUp()
        else:
            cube.rollRight()

#Turns the cube sides so the cube face can be solved.
def finalStageTurns(cube): 
    cube.rightTurn()
    cube.topTurn()
    cube.rightInvert()
    cube.topTurn()
    cube.rightTurn()
    cube.topTurn()
    cube.topTurn()
    cube.rightInvert()

#If the initial cube received does not have a yellow cross the turns done by straightline
#will solve the yellow cross if there are yellow tiles in a horizontal line.
def straightLine(cube):
    cube.frontTurn()
    cube.rightTurn()
    cube.topTurn()
    cube.rightInvert()
    cube.topInvert()
    cube.frontInvert()

#Similar to the straightLine but the turns performed by the vShapeOrMiddleYellow can be
#used for two different middle and v shape yellow cases
def vShapeOrMiddleYellow(cube):
    cube.frontTurn()
    cube.topTurn()
    cube.rightTurn()
    cube.topInvert()
    cube.rightInvert()
    cube.frontInvert()


        


