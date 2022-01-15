accumulate = 0

def acc(data, inp):
    data["accumulate"] += inp
    data["index"] += 1
    return data

def nop(data, inp):
    data["index"] += 1
    return data

def jmp(data, inp):
    data["index"] += inp
    return data

instructions = {
    "acc": acc,
    "nop": nop,
    "jmp": jmp 
}



with open("day08input.txt") as file:
    program = [(line.split(" ")[0], int(line.strip().split(" ")[1])) for line in file]
    runLines = set()
    currentStatus = {"index": 0, "accumulate": 0}

    while currentStatus["index"] not in runLines:
        runLines.add(currentStatus["index"])
        op, inp = program[currentStatus["index"]]

        currentStatus = instructions[op](currentStatus, inp)
    
    print(currentStatus)

    for i in range(0, len(program)):
        newProgram = [line for line in program]
        if newProgram[i][0] == "jmp":
            newProgram[i] = ("nop", newProgram[i][1])
        elif newProgram[i][0] == "nop":
            newProgram[i] = ("jmp", newProgram[i][1])
        
        runLines = set()
        currentStatus = {"index": 0, "accumulate": 0}

        try:
            while currentStatus["index"] not in runLines:
                runLines.add(currentStatus["index"])
                op, inp = newProgram[currentStatus["index"]]

                currentStatus = instructions[op](currentStatus, inp)
        except IndexError:
            print("Oopsies an index error")
            print(currentStatus)
            break