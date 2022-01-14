with open("day9input.txt") as file:
    nums = [int(line) for line in file]
    numChecks = []

    for i in range(0, len(nums) - 25):
        checkSet = {num for num in nums[:25+i]}
        check = False
        for num in checkSet:
            if (nums[25+i] - num) != num and (nums[25+i] - num) in checkSet:
                check = True

        numChecks.append(check)

    noSumNum = nums[numChecks.index(False)+25]
    print(noSumNum)

    for i in range(0, len(nums)):
        for j in range (i, len(nums)):
            summedNum = sum(nums[i:j])
            if summedNum == noSumNum:
                print("match!")
                print(min(nums[i:j]) + max(nums[i:j]))
            if summedNum > noSumNum:
                break

    print("note, second match is an array of just [noSumNum] lol")

