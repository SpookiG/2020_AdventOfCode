testSequences = [[1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]
testSolutions = [1, 10, 27, 78, 438, 1836]

iterations1 = 2020

def runSequence(sequence, iterations):
    numberTurnLookup = dict()
    lastNum = 0

    for i in range(iterations - 1):
        if sequence:
            numberTurnLookup[sequence[0]] = i
            lastNum = sequence[0]
            sequence = sequence[1:]
            
        
        if lastNum in numberTurnLookup:
            nextNum = i - numberTurnLookup[lastNum]
            numberTurnLookup[lastNum] = i
            lastNum = nextNum

        else:
            numberTurnLookup[lastNum] = i
            lastNum = 0
    
    return lastNum
        

        
# run tests (passed woo!)
print("Running q1 tests:")
for sequence, solution in zip(testSequences, testSolutions):
    calculatedResult = runSequence(sequence, iterations1)
    print("Expected result: " + str(solution) + " | Given result: " + str(calculatedResult) + " | Match? : " + str(solution == calculatedResult))

# run question input
calculatedResult = runSequence([9,3,1,0,8,4], iterations1)
print("\n\nQuestion 1 result: " + str(calculatedResult))


#question 2 has it's own iteration number & tests & solutions
testSequences2 = [[0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]
testSolutions2 = [175594, 2578, 3544142, 261214, 6895259, 18, 362]

iterations2 = 30000000



# run tests (passed woo!)
# commenting out because slow
#print("\n\nRunning q2 tests:")
#for sequence, solution in zip(testSequences2, testSolutions2):
#    calculatedResult = runSequence(sequence, iterations2)
#    print("Expected result: " + str(solution) + " | Given result: " + str(calculatedResult) + " | Match? : " + str(solution == calculatedResult))

# run question2 input (takes about 10-15 seconds)
calculatedResult = runSequence([9,3,1,0,8,4], iterations2)
print("\n\nQuestion 2 result: " + str(calculatedResult))