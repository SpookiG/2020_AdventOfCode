NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# question 1 actions
def MoveAction(ship, direction, amount):
    if direction == NORTH:
        ship["pos"] = (ship["pos"][0], ship["pos"][1] + amount)
    
    if direction == EAST:
        ship["pos"] = (ship["pos"][0] + amount, ship["pos"][1])

    if direction == SOUTH:
        ship["pos"] = (ship["pos"][0], ship["pos"][1] - amount)
    
    if direction == WEST:
        ship["pos"] = (ship["pos"][0] - amount, ship["pos"][1])


def RotateAction(ship, direction, amount):
    if direction == "R":
        ship["dir"] += int(amount / 90)
    
    else:
        ship["dir"] -= int(amount / 90)

    ship["dir"] %= 4


actions = {
    "N" : lambda ship, value : MoveAction(ship, NORTH, value),
    "E" : lambda ship, value : MoveAction(ship, EAST, value),
    "S" : lambda ship, value : MoveAction(ship, SOUTH, value),
    "W" : lambda ship, value : MoveAction(ship, WEST, value),
    "R" : lambda ship, value : RotateAction(ship, "R", value),
    "L" : lambda ship, value : RotateAction(ship, "L", value),
    "F" : lambda ship, value : MoveAction(ship, ship["dir"], value)
}




#question 2 actions
def waypointMove(ship, waypoint, amount):
    ship["pos"] = (ship["pos"][0] + (waypoint["pos"][0] * amount), ship["pos"][1] + (waypoint["pos"][1] * amount))


def waypointRotate(ship, waypoint, direction, amount):
    # rotate 180 degrees by negating x and y
    if amount == 180:
        waypoint["pos"] = (-waypoint["pos"][0], -waypoint["pos"][1])
    
    else:
        # rotate 90 degrees right and then another 180 degrees if the rotation was left
        waypoint["pos"] = (waypoint["pos"][1], -waypoint["pos"][0])

        if (direction == "R" and amount == 270) or (direction == "L" and amount == 90):
            waypoint["pos"] = (-waypoint["pos"][0], -waypoint["pos"][1])

waypointActions = {
    "N" : lambda ship, waypoint, value : MoveAction(waypoint, NORTH, value),
    "E" : lambda ship, waypoint, value : MoveAction(waypoint, EAST, value),
    "S" : lambda ship, waypoint, value : MoveAction(waypoint, SOUTH, value),
    "W" : lambda ship, waypoint, value : MoveAction(waypoint, WEST, value),
    "R" : lambda ship, waypoint, value : waypointRotate(ship, waypoint, "R", value),
    "L" : lambda ship, waypoint, value : waypointRotate(ship, waypoint, "L", value),
    "F" : lambda ship, waypoint, value : waypointMove(ship, waypoint, value)
}




with open("day12input.txt") as file:
    directions = [ (line[0], int(line[1:])) for line in file]

    # check the range of turning angles, should be multiples of 90
    turiningAngles = {direction[1] for direction in directions if direction[0] == "L" or direction[0] == "R"}
    print ("Range of turning angles, should be multiples of 90: " + str(turiningAngles))

    ship = {
        "pos" : (0, 0),
        "dir" : EAST
    }

    loops = 0

    print("Starting ship movements")
    for direction in directions:
        actions[direction[0]](ship, direction[1])
        print("Step: " + str(loops) + "\r", end="")
        loops +=1
    
    print("\nMovements finished")
    print("Finished ship state: " + str(ship))
    print("Manhattan distance: " + str(abs(ship["pos"][0]) + abs(ship["pos"][1])))

    ship = {
        "pos" : (0, 0)
    }

    waypoint = {
        "pos" : (10, 1)
    }

    loops = 0

    print("\nStarting ship and waypoint movements")
    for direction in directions:
        waypointActions[direction[0]](ship, waypoint, direction[1])
        print("Step: " + str(loops) + "\r", end="")
        loops +=1
    
    print("\nMovements finished")
    print("Finished ship state: " + str(ship))
    print("Manhattan distance: " + str(abs(ship["pos"][0]) + abs(ship["pos"][1])))

