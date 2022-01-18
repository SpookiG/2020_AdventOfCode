import ast
from asyncio.windows_events import NULL
from itertools import accumulate

with open("day13input.txt") as file:
    earliestDeparture = int(file.readline())
    busses = [bus.strip() for bus in file.readline().split(",")]

    activeBusses = [int(bus) for bus in busses if bus.isnumeric()]
    waitTimes = [bus - (earliestDeparture % bus) for bus in activeBusses]

    shortestWaitTime = min(waitTimes)
    shortestWaitIndex = waitTimes.index(shortestWaitTime)

    print("earliest bus: " + str(activeBusses[shortestWaitIndex]))
    print("minutes to wait for bus: " +str(shortestWaitTime))
    print("multiplied: " + str(activeBusses[shortestWaitIndex] * shortestWaitTime))


    # list of the size of steps between busses
    accumulatedStepSizes = [step for step, bus in enumerate(busses) if bus.isnumeric()]

    print(accumulatedStepSizes)
    
    # get a max modulo step from the active busses list and use as a basis for the question 2 check
    #maxMod = max(activeBusses)
    #maxModIndex = activeBusses.index(maxMod)
    #accumulatedStepSizes = [step - accumulatedStepSizes[maxModIndex] for step in accumulatedStepSizes]

    print(accumulatedStepSizes)

    print(len(accumulatedStepSizes))
    print(len(activeBusses))

    maxMod = activeBusses[0]
    mod = 0

    checkIndex = 0
    match = False
    matchStep = 0

    # quickly find a value that matches the order
    while checkIndex < len(activeBusses):
        mod += maxMod
        matchStep += maxMod

        print("Step: " + str(mod) + "     " + str(maxMod) + "     " + str(checkIndex) + "\r", end="")

        if (mod + accumulatedStepSizes[checkIndex]) % activeBusses[checkIndex] == 0:
            if match:
                maxMod = matchStep
                mod %= maxMod
                match = False
                checkIndex += 1
            else:
                matchStep = 0
                match = True
        

    
    divisionOccured = True

    print("\n" + str(mod) + "     " + str([(mod + accumulatedStepSize) % bus for accumulatedStepSize, bus in zip(accumulatedStepSizes, activeBusses)]))

    
