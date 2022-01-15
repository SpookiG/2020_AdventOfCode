with open("day01input.txt") as file:
    inputArray = [int(line.strip()) for line in file.read().split('\n') if len(line.strip()) > 0]
    #print (inputArray)

    inputSet = {num for num in inputArray}

    for num in inputSet:
        if (2020 - num) in inputSet:
            print(num)
            print(2020 - num)
            print(num * (2020 - num))
            print()

    print("\n\n")
    
    for num1 in inputSet:
        for num2 in inputSet:
            if num1 == num2:
                break

            if (2020 - num1 - num2) in inputSet:
                print(num1)
                print(num2)
                print(2020 - num1 - num2)
                print(num1 * num2 * (2020 - num1 - num2))
                print()