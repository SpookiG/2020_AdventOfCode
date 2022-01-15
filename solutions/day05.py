with open("day05input.txt") as file:
    binPositions = [(line[:7].replace("F", "0").replace("B", "1"), line[7:].replace("L", "0").replace("R", "1")) for line in file]
    intPositions = [(int(rBin, 2), int(cBin, 2)) for rBin, cBin in binPositions]
    seatIds = {(rInt * 8) + cInt for rInt, cInt in intPositions}

    print(max(seatIds))

    for id in range(min(seatIds) + 1, max(seatIds) - 1):
        if id not in seatIds:
            print(id)