"""
File: solveMiddleLayer.py
Author: Carson Turner
Description: solves the middle layer of the cube
"""
from solveWhiteCross import findEdge, rotateSide, rotateInvert

def solveMiddleLayer(cube):
    sideOrderCCW = {cube.getFront():cube.getRight(), cube.getLeft():cube.getFront(), cube.getRight():cube.getBack(), cube.getBack():cube.getLeft()}
    #There are 4 middle edges to solve
    for i in range(4):
        bottomEdges = makeEdges(cube)
        #If all 4 bottom edges have yellow, removeYellowAlgorithm
        if (isYellowBottom(bottomEdges)):
            side = cube.getFront()
            edgeColor = side.getMiddleRight()[:-1]
            sideColor = side.getMiddleCenter()[:-1]
            nextSide = sideOrderCCW[side]
            nextEdgeColor = nextSide.getMiddleLeft()[:-1]
            nextSideColor = nextSide.getMiddleCenter()[:-1]
            for i in range(5):
                if not (edgeColor == sideColor and nextEdgeColor == nextSideColor):
                    edgeToMiddleRight(cube, side, nextSide)
                    bottomEdges = makeEdges(cube)
                    break
                elif i < 4:
                    cube.bottomTurn()
                    side = nextSide
                    edgeColor = side.getMiddleRight()[:-1]
                    sideColor = side.getMiddleCenter()[:-1]
                    nextSide = sideOrderCCW[side]
                    nextEdgeColor = nextSide.getMiddleLeft()[:-1]
                    nextSideColor = nextSide.getMiddleCenter()[:-1]
                else:
                    #Middle layer is already done
                    return None
        
        #Find an edge without any yellow
        for edge in bottomEdges:
            if not isYellowEdge(edge):
                break
            
        #Turn bottom until that edge's non-bottom tile is on the correct side
        targetColor = edge[1][:-1]
        side = findEdge(edge[1], cube)
        sideColor = side.getMiddleCenter()[:-1]
        while not targetColor == sideColor:
            cube.bottomTurn()
            side = sideOrderCCW[side]
            sideColor = side.getMiddleCenter()[:-1]
            
        #Determine which side the edge bottom tile goes on
        targetColor = edge[0][:-1]
        #Checking if it belongs CenterRight
        targetSide = sideOrderCCW[side]
        sideColor = targetSide.getMiddleCenter()[:-1]
        if targetColor == sideColor:
            #Place edge into CenterRight
            edgeToMiddleRight(cube, side, targetSide)
        else:
            #Place edge into CenterLeft
            targetSide = sideOrderCCW[sideOrderCCW[targetSide]]
            edgeToMiddleLeft(cube, side, targetSide)

def makeEdges(cube):
    edges = []
    edges.append([cube.getBottom().getTopCenter(), cube.getFront().getBottomCenter()])
    edges.append([cube.getBottom().getMiddleLeft(), cube.getLeft().getBottomCenter()])
    edges.append([cube.getBottom().getMiddleRight(), cube.getRight().getBottomCenter()])
    edges.append([cube.getBottom().getBottomCenter(), cube.getBack().getBottomCenter()])
    return edges

def isYellowBottom(edges):
    return (isYellowEdge(edges[0]) and isYellowEdge(edges[1]) and isYellowEdge(edges[2]) and isYellowEdge(edges[3]))

def isYellowEdge(edge):
    return (('yellow' in edge[0]) or ('yellow' in edge[1]))

##def removeYellowBottom(cube):
##    #Normal turns are clockwise, inverse CCW
##    #From video: U, R, Ui, Ri, Ui, Fi, U, F
##    #Translating to standard position (white top, red front)...
##    cube.bottomTurn()
##    cube.leftTurn()
##    cube.bottomInvert()
##    cube.leftInvert()
##    cube.bottomInvert()
##    cube.frontInvert()
##    cube.bottomTurn()
##    cube.frontTurn()

def edgeToMiddleRight(cube, front, right):
    #From video: Ui, Li, U, L, U, F, Ui, Fi
    #Translating to standard position (white top, red front)...
    cube.bottomInvert()
    rotateInvert(right, cube) #rightInvert()
    cube.bottomTurn()
    rotateSide(right, cube) #rightTurn()
    cube.bottomTurn()
    rotateSide(front, cube) #frontTurn()
    cube.bottomInvert()
    rotateInvert(front, cube) #frontInvert()

def edgeToMiddleLeft(cube, front, left):
    #From video: U, R, Ui, Ri, Ui, Fi, U, F
    #Translating to standard position (white top, red front)...
    cube.bottomTurn()
    rotateSide(left, cube) #leftTurn()
    cube.bottomInvert()
    rotateInvert(left, cube) #leftInvert()
    cube.bottomInvert()
    rotateInvert(front, cube) #frontInvert()
    cube.bottomTurn()
    rotateSide(front, cube) #frontTurn()
