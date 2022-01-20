# functions to convert int to and from binary string
def intToString(i):
    s = ""
    for exponent in range(35, -1, -1):
        if i >= pow(2, exponent):
            s += "1"
            i -= pow(2, exponent)
        else:
            s += "0"
    
    return s

def stringToInt(s):
    i = 0
    for exponent, digit in enumerate(s[::-1]):
        if digit == "1":
            i += pow(2, exponent)
    
    return i

# apply bitmask to bit string based on mask rules given in the question
def applyMask(mask, value):
    maskedValue = ""

    for mbit, vbit in zip(mask, value):
        if mbit == "X":
            maskedValue += vbit
        else:
            maskedValue += mbit
    
    return maskedValue



# define instructions
def setMask(newMask, data):
    data["mask"] = newMask

def setMem(address, value, data):
    maskedValue = stringToInt(applyMask(data["mask"], intToString(value)))      # mask is applied to value being assigned
    data["mem"][address] = maskedValue

# parse function
def parse(line):
    if line.startswith("mask"):
        return lambda data : setMask(line.split("=")[1].strip(), data)
    
    else:
        return lambda data : setMem(int(line.split("=")[0].strip()[4:-1]), int(line.split("=")[1].strip()), data)


# need a simple parser to interpret instructions
with open("day14input.txt") as file:
    # some simple tests to make sure the int to string and string to int functions run as expected before use in the program
    print("Tests for the int to string and int from string conversion functions")
    print("Testing int to string length, should match mask:")
    print("Mask: 0111X10100100X1111X10010X000X1000001")
    print("Mask length: " + str(len("0111X10100100X1111X10010X000X1000001")))
    print("\nint: 468673978")
    print("int to string: " + intToString(468673978))
    print("int to string length: " + str(len(intToString(468673978))))

    print("\nlenght match: " + str(len(intToString(468673978)) == len("0111X10100100X1111X10010X000X1000001")))

    print("\n\nTesting that string to int converts back to the same int generated from int to string:")
    print("int: 468673978")
    print("int to string: " + intToString(468673978))
    print("string to int: " + str(stringToInt(intToString(468673978))))
    print("value match: " + str(468673978 == stringToInt(intToString(468673978))))

    print("\nint: 243184")
    print("int to string: " + intToString(243184))
    print("string to int: " + str(stringToInt(intToString(243184))))
    print("value match: " + str(243184 == stringToInt(intToString(243184))))

    print("\n\nTests complete, parsing instructions")
    data = {
        "mask": "",
        "mem" : dict()
    }

    instructions = [parse(line) for line in file]

    print("Parsing complete, running instructions")
    for instruction in instructions:
        instruction(data)
    
    

    print(sum(data["mem"].values()))


    


# q2 requires some differences
# apply mask is now applied to the memory address with different rules
def applyMask2(mask, address):
    maskedAddresses = [""]

    for mbit, abit in zip(mask, address):
        if mbit == "0":
            for i in range(len(maskedAddresses)):
                maskedAddresses[i] += abit
        
        if mbit == "1":
            for i in range(len(maskedAddresses)):
                maskedAddresses[i] += mbit
        
        # importantly an X means this both the address where the bit == 1 and where the bit == 0 should be accessed in setMem2(), this doubles the number of addresses to be accessed
        if mbit == "X":
            maskedAddresses = [maskedAddress + "1" for maskedAddress in maskedAddresses] + [maskedAddress + "0" for maskedAddress in maskedAddresses]


    return maskedAddresses


# setMem2 now gets a list of memory addresses from the mask and sets the values for all of these addresses
def setMem2(address, value, data):
    maskedAddresses = [stringToInt(maskedAddress) for maskedAddress in applyMask2(data["mask"], intToString(address))]

    for maskedAddress in maskedAddresses:
        data["mem"][maskedAddress] = value


# only difference is using making sure to use setMem2() instead of setMem() 
def parse2(line):
    if line.startswith("mask"):
        return lambda data : setMask(line.split("=")[1].strip(), data)
    
    else:
        return lambda data : setMem2(int(line.split("=")[0].strip()[4:-1]), int(line.split("=")[1].strip()), data)




with open("day14input.txt") as file:
    print("\n\nParsing instructions for question 2")
    data = {
        "mask": "",
        "mem" : dict()
    }

    instructions = [parse2(line) for line in file]

    print("Parsing complete, running instructions")
    for instruction in instructions:
        instruction(data)
    
    
    print(sum(data["mem"].values()))