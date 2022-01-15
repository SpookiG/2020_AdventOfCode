def getPath(treeGrid, xstep, ystep=1):
    return [treeGrid[y][x % len(treeGrid[y])] for x, y in zip(range(0, 10000, xstep), range(0, len(treeGrid), ystep))]

with open("day03input.txt") as file:
    treeGrid = [line.strip() for line in file]

    path = [line[sideStep % len(line)] for line, sideStep in zip(treeGrid, range(0, 10000, 3))]
    print(path.count("#"))
    #print(getPath(treeGrid, 3).count("#"))

    print(getPath(treeGrid, 1).count("#")
        * getPath(treeGrid, 3).count("#")
        * getPath(treeGrid, 5).count("#")
        * getPath(treeGrid, 7).count("#")
        * getPath(treeGrid, 1, 2).count("#"))




