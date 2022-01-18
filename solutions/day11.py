from operator import mod
from textwrap import fill
import numpy as np

#def countFilledSeats(surroundingArea):
#    surroundingAreaFilled = [seat == '#' for row in surroundingArea for seat in row]
#    return surroundingAreaFilled.count(True)

#def incrementIfValid(filledNeighbourCount, indexX, indexY):
#    if 0 <= indexX and indexX < len(filledNeighbourCount) and 0 <= indexY and indexY < len(filledNeighbourCount[0]):
#        filledNeighbourCount[indexX, indexY] += 1

#def filledCheck(layout, pos):
#    if 0 <= pos[0] and pos[0] < len(layout) and 0 <= pos[1] and pos[1] < len(layout[0]):

def checkNeighbours(layout, x, y):
    neighbourCount = 0



    lowerX = x-1 >= 0
    upperX = x+1 < len(layout)
    lowerY = y-1 >= 0
    upperY = y+1 < len(layout[0])

    if lowerX:
        if layout[x-1, y] == "#":
            neighbourCount += 1

        if lowerY:
            if layout[x-1, y-1] == "#":
                neighbourCount += 1


def changeSeats(layout, newLayout, filledNeighbourCount):
    # calculate neighbour count
    for x in range(len(layout)):
        for y in range(len(layout[0])):

            for x2 in range(max(x-1, 0), min(x+2, len(layout))):
                for y2 in range(max(y-1, 0), min(y+2, len(layout[0]))):

                    if x2 != x or y2 != y:
                        if layout[x2, y2] == "#":
                            filledNeighbourCount[x, y] += 1
                
    #print(filledNeighbourCount)

    # use neighbour count to check whether to change seats
    for x in range(len(layout)):
        for y in range(len(layout[0])):
            if layout[x, y] == "L" and filledNeighbourCount[x, y] == 0:
                newLayout[x, y] = "#"

            if layout[x, y] == "#" and filledNeighbourCount[x, y] >= 4:
                newLayout[x, y] = "L"

    #print(newLayout)


#def spiderCrawl(pos, dir, ):

def changeSeatsSpiderStyle(layout, newLayout, filledNeighbourCount):

    # calculate neighbour count
    for x in range(len(layout)):
        for y in range(len(layout[0])):
            checkActive = [True, True, True, True, True, True, True, True]

            for modifier in range(1, 100):
                #print(checkActive)
                if not any(checkActive):
                    break

                if checkActive[0]:
                    if x-modifier < 0 or y-modifier < 0 or layout[x-modifier, y-modifier] == "L":
                        checkActive[0] = False
                    
                    elif layout[x-modifier, y-modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[0] = False
                
                if checkActive[1]:
                    if x-modifier < 0 or layout[x-modifier, y] == "L":
                        checkActive[1] = False
                    
                    elif layout[x-modifier, y] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[1] = False

                if checkActive[2]:
                    if x-modifier < 0 or y+modifier >= len(layout[0]) or layout[x-modifier, y+modifier] == "L":
                        checkActive[2] = False
                    
                    elif layout[x-modifier, y+modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[2] = False

                if checkActive[3]:
                    if y-modifier < 0 or layout[x, y-modifier] == "L":
                        checkActive[3] = False
                    
                    elif layout[x, y-modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[3] = False

                if checkActive[4]:
                    if y+modifier >= len(layout[0]) or layout[x, y+modifier] == "L":
                        checkActive[4] = False
                    
                    elif layout[x, y+modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[4] = False

                if checkActive[5]:
                    if x+modifier >= len(layout) or y-modifier < 0 or layout[x+modifier, y-modifier] == "L":
                        checkActive[5] = False
                    
                    elif layout[x+modifier, y-modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[5] = False

                if checkActive[6]:
                    if x+modifier >= len(layout) or layout[x+modifier, y] == "L":
                        checkActive[6] = False
                    
                    elif layout[x+modifier, y] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[6] = False

                if checkActive[7]:
                    if x+modifier >= len(layout) or y+modifier >= len(layout[0]) or layout[x+modifier, y+modifier] == "L":
                        checkActive[7] = False
                    
                    elif layout[x+modifier, y+modifier] == "#":
                        filledNeighbourCount[x, y] += 1
                        checkActive[7] = False


    # use neighbour count to check whether to change seats
    for x in range(len(layout)):
        for y in range(len(layout[0])):
            if layout[x, y] == "L" and filledNeighbourCount[x, y] == 0:
                newLayout[x, y] = "#"

            if layout[x, y] == "#" and filledNeighbourCount[x, y] >= 5:
                newLayout[x, y] = "L"




with open("day11input.txt") as file:
    original = np.array([[char for char in line.strip()] for line in file])
    print(original.shape)
    

    layout = original.copy()
    newLayout = original.copy()
    filledNeighbourCount = np.zeros(original.shape, int)
    changeSeats(layout, newLayout, filledNeighbourCount)
    

    loops = 0

    while not np.all(newLayout == layout):
        layout[:] = newLayout
        filledNeighbourCount.fill(0)
        changeSeats(layout, newLayout, filledNeighbourCount)
        loops+=1
    
        print("step: " + str(loops) + "\r", end="")

    #with open("day11results.txt", "w") as results:
    #    for row in layout:
    #        for char in row:
    #            results.write(char)
    #        results.write("\n")

    
    surroundingAreaFilled = [seat == '#' for row in layout for seat in row]
    print("\nclose neighbour result: " + str(surroundingAreaFilled.count(True)))

    layout = original.copy()
    newLayout = original.copy()
    filledNeighbourCount = np.zeros(original.shape, int)
    changeSeatsSpiderStyle(layout, newLayout, filledNeighbourCount)

    loops = 0

    while not np.all(newLayout == layout):
        layout[:] = newLayout
        filledNeighbourCount.fill(0)
        changeSeatsSpiderStyle(layout, newLayout, filledNeighbourCount)
        loops+=1
    
        print("step: " + str(loops) + "\r", end="")
        #print(filledNeighbourCount)
        #print(layout)
    
    surroundingAreaFilled = [seat == '#' for row in layout for seat in row]
    print("\ndistant neighbour result: " + str(surroundingAreaFilled.count(True)))