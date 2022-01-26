# question 1
# generate a dictionary of field names to rules, rules are generic lambda functions
def generateRules(file):
    rules = dict()
    for line in file:
        if line.strip() == "":
            return rules
        
        fieldName, rangeStrings = line.split(":")
        ranges = [[int(val) for val in rangeString.split("-")] for rangeString in rangeStrings.strip().split(" or ")]
        rules[fieldName.strip()] = prepRule(ranges)


# python overwrites every lambda function in a dictionary if multiple lambdas are assigned in the same function. Strange awful bug.
# To work around, an extra function is needed to prep the lambda function for inserting into the dictionary
def prepRule(ranges):
    return lambda num : (ranges[0][0] <= num and num <= ranges[0][1]) or (ranges[1][0] <= num and num <= ranges[1][1])
        

# get ticket information for your ticket and the other tickets you have access to
def grabTickets(file):
    file.readline()
    myTicket = [int(num) for num in file.readline().strip().split(",")]

    file.readline()
    file.readline()

    otherTickets = []
    for line in file:
        if line.strip() == "":
            break
        
        otherTickets.append([int(num) for num in line.strip().split(",")])
    
    return myTicket, otherTickets


# figure out which fields are invalid by checking if the number's match any of the rules
def findInvalidFields(rules, tickets):
    invalidFields = []

    for ticket in tickets:
        for field in ticket:
            valid = False
            for rule in rules.values():
                if rule(field):
                    valid = True
                    break
            
            if not valid:
                invalidFields.append(field)
    
    return invalidFields



# run w/ test input
test1Pass = False
with open("day16q1Test.txt") as file:
    print("Running test 1:")
    print("Parsing input")
    rules = generateRules(file)
    myTicket, otherTickets = grabTickets(file)

    print("Finding invalid fields")
    expectedSum = 71
    invalidFields = findInvalidFields(rules, [myTicket] + otherTickets)

    print("Invalid fields: " + str(invalidFields))
    print("Expected sum: " + str(expectedSum))
    print("Actual sum: " + str(sum(invalidFields)))

    if expectedSum == sum(invalidFields):
        print("Test 1 passed!\n\n")
        test1Pass = True
    









# question 2

# question 2 requires filtering out invalid tickets, slightly modify findInvalidFields to return list of valid tickets
def filterValidTickets(rules, tickets):
    validTickets = []

    for ticket in tickets:
        validTicket = True
        for field in ticket:
            validField = False
            for rule in rules.values():
                if rule(field):
                    # if any rule matches, field is valid
                    validField = True
                    break
            
            # if all fields are valid the ticket is valid
            validTicket = validTicket and validField
            
        if validTicket:
            validTickets.append(ticket)
    
    return validTickets

# now we make a lookup for each fieldname to the possible indexes
def generateFieldNameIndexLookup(rules, tickets):
    # start where every field name could point to any index in a ticket
    fieldNameIndexLookup = {ruleName : {i for i in range(len(tickets[0]))} for ruleName in rules}

    # then filter down and remove fields that don't match rules
    for ticket in tickets:
        for i, field in enumerate(ticket):
            for ruleName in rules:
                if not rules[ruleName](field) and i in fieldNameIndexLookup[ruleName]:
                    fieldNameIndexLookup[ruleName].remove(i)

    # now deduce that when a field only has one possible index, the index possibility can be removed from any other field

    for _ in range(len(fieldNameIndexLookup)):
        for fieldName1 in fieldNameIndexLookup:
            if len(fieldNameIndexLookup[fieldName1]) == 1:
                for fieldName2 in fieldNameIndexLookup:
                    if fieldName1 != fieldName2:
                        index = fieldNameIndexLookup[fieldName1].pop()
                        if index in fieldNameIndexLookup[fieldName2]:
                            fieldNameIndexLookup[fieldName2].remove(index)

                        fieldNameIndexLookup[fieldName1].add(index)
    
    # at this stage all sets should be size 1 so pop it all out
    for fieldName in fieldNameIndexLookup:
        fieldNameIndexLookup[fieldName] = fieldNameIndexLookup[fieldName].pop()

    return fieldNameIndexLookup


# run w/ test input
test2Pass = False
with open("day16q2Test.txt") as file:
    print("Running test 2:")
    print("Parsing input")
    rules = generateRules(file)
    myTicket, otherTickets = grabTickets(file)

    print("Removing invalid tickets")
    validTickets = filterValidTickets(rules, [myTicket] + otherTickets)

    fieldNameIndexLookup = generateFieldNameIndexLookup(rules, validTickets)

    expectedValues = {
        "class" : 12,
        "row" : 11,
        "seat" : 13
    }
    localTestPass = True

    print("Expected field values: " + str(expectedValues))
    print("Actual field values:")
    for fieldName in fieldNameIndexLookup:
        print(fieldName + " = " + str(myTicket[fieldNameIndexLookup[fieldName]]))

        localTestPass = localTestPass and myTicket[fieldNameIndexLookup[fieldName]] == expectedValues[fieldName]

    if localTestPass:
        print("Test 2 passed!\n\n")
        test2Pass = True

    #print("Invalid fields: " + str(invalidFields))
    #print("Expected sum: " + str(expectedSum))
    #print("Actual sum: " + str(sum(invalidFields)))

    #if expectedSum == sum(invalidFields):
    #    print("Test 1 passed!")
    #    test2Pass = True







with open("day16input.txt") as file:
    

    if test1Pass:
        print("Test 1 passed! Running question 1")

        print("Question 1:")
        print("Parsing input")
        rules = generateRules(file)
        myTicket, otherTickets = grabTickets(file)

        print("Finding invalid fields")
        invalidFields = findInvalidFields(rules, [myTicket] + otherTickets)

        print("Invalid fields: " + str(invalidFields))
        print("Sum: " + str(sum(invalidFields)))

        if test2Pass:
            print("Test 2 passed! Running question 2")

            print("Question 2:")
            print("Removing invalid tickets")
            validTickets = filterValidTickets(rules, [myTicket] + otherTickets)

            fieldNameIndexLookup = generateFieldNameIndexLookup(rules, validTickets)

            print(fieldNameIndexLookup)

            departureValues = [myTicket[fieldNameIndexLookup[fieldName]] for fieldName in fieldNameIndexLookup if fieldName.startswith("departure")]

            departureProd = 1
            for val in departureValues:
                departureProd *= val

            print("departure values: " + str(departureValues))
            print("Prod: " + str(departureProd))

