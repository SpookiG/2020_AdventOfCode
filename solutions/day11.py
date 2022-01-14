import numpy as np




def countFilledSeats(surroundingArea):
    surroundingAreaFilled = [seat == '#' for row in surroundingArea for seat in row]
    return surroundingAreaFilled.count(True)

def changeSeats(layout):
    newLayout = layout.copy() #np.array([row.copy() for row in layout])

    for x in range(len(layout)):
        for y in range(len(layout[0])):
            if (layout[x, y] == "L" and
                countFilledSeats(layout[max(x-1, 0):min(x+2, len(layout)), max(y-1, 0):min(y+2, len(layout))]) == 0):
                newLayout[x, y] = "#"
                continue

            if (layout[x, y] == "#" and
                countFilledSeats(layout[max(x-1, 0):min(x+2, len(layout)), max(y-1, 0):min(y+2, len(layout))]) >= 5):
                newLayout[x, y] = "L"
                continue
            
            newLayout[x, y] = layout[x, y]
    
    return newLayout


def countNeighbours(layout, slap):
    neighbourCount = np.zeros(layout.shape, np.int32)

    for x in layout.shape[0]:
        for y in layout.shape[1]:
            neighbourCount += slap(layout, x, y)
        
    return neighbourCount


def proximitySlap(layout, x, y):
    slapped = np.zeros(layout.shape, np.int32)
    if (layout[x, y] == "#"):
        slapped[max(x-1, 0):min(x+2, len(layout)), max(y-1, 0):min(y+2, len(layout))] = 1
    
    return slapped

def spiderSlap(layout, x, y):
    slapped = np.zeros(layout.shape, np.int32)
    if (layout[x, y] == "#"):
        slapped[:, y] = 1
        slapped[x, :] = 1

        c = y - x

        xmin = 0
        xmax = layout.shape[0] + 1
        ymin = 0
        ymax = layout.shape[1] + 1

        if c < 0:
            xmin = 0 - c
        else:
            ymin = 0 + c
        if layout.shape[0] + c > layout.shape[1]:
            xmax = layout.shape[1] + 1 - c
        else:
            ymax = layout.shape[0] + 1 + c

        slapped[range(xmin, xmax), range(ymin, ymax)] = 1

        xmin = 0
        xmax = layout.shape[0] + 1
        ymin = 0
        ymax = layout.shape[1] + 1

        if layout.shape[0] + c > layout.shape[1]:


        if c < 0:
            xmin = 0 - c
        else:
            ymin = 0 + c
        if layout.shape[0] + c > layout.shape[1]:
            xmax = layout.shape[1] + 1 - c
        else:
            ymax = layout.shape[0] + 1 + c

        slapped[range(xmin, xmax), range(ymin, ymax)] = 1


        if c >= 0:
            pass
        else:
            pass


        # y = x + c
    
    return slapped




with open("day11input.txt") as file:
    layout = np.array([[char for char in line.strip()] for line in file])
    #layout = [[char for char in line.strip()] for line in file]

    newLayout = layout.copy()
    newLayout = changeSeats(layout)

    loops = 0

    while not np.all(newLayout == layout):
        layout = newLayout
        newLayout = changeSeats(layout)
        loops+=1
    
    print(loops)

    with open("day11results.txt", "w") as results:
        for row in layout:
            for char in row:
                results.write(char)
            results.write("\n")

    print(countFilledSeats(layout))
    