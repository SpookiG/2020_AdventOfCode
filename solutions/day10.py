with open("day10input.txt") as file:
    jolts = sorted([int(line.strip()) for line in file])
    jolts = [0] + jolts + [jolts[-1] + 3]

    joltCounts = {1:0, 2:0, 3:0}

    for j, jnext in zip(jolts, jolts[1:]):
        joltCounts[jnext - j] += 1

    print(joltCounts[1] * joltCounts[3])

    
    pathCount = [0] * len(jolts)
    pathCount[0] = 1

    for j in range(len(jolts)):
        for i in range(j + 1, len(jolts)):
            if jolts[i] - jolts[j] <= 3:
                pathCount[i] += pathCount[j]

    print(pathCount[-1])