from functools import reduce

with open("day06input.txt") as file:
    groupAnswerStrings = file.read().split("\n\n")
    groupAnswers = [{answer for answer in answerString.replace("\n", "")} for answerString in groupAnswerStrings]

    groupAnswerSums = [len(answers) for answers in groupAnswers]
    print(sum(groupAnswerSums))

    ammendedGroupAnswers = [[{answer for answer in singleAnswerString} for singleAnswerString in answerString.split("\n")] for answerString in groupAnswerStrings]
    ammendedGroupAnswersIntersection = [reduce(lambda ansIntersection, singleAnswer : ansIntersection.intersection(singleAnswer), answerlist) for answerlist in ammendedGroupAnswers]

    ammendedGroupAnswerSums = [len(answers) for answers in ammendedGroupAnswersIntersection]
    print(sum(ammendedGroupAnswerSums))