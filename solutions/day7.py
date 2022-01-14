from collections import defaultdict

def countBags(bagBagLookup, topBag, multiplier=1):
    count = 0
    for canHold, valueBag in bagBagLookup[topBag]:
        count += canHold * multiplier
        count += countBags(bagBagLookup, valueBag, multiplier * canHold)
    
    return count

with open("day7input.txt") as file:
    bagBagStringLookup = {line.split(" bags contain ")[0]: line.split(" bags contain ")[1] for line in file}
    bagBagStringLookup = {keyBag: [valueBag.strip() for valueBag in bagBagStringLookup[keyBag].split(",")] for keyBag in bagBagStringLookup}

    bagBagLookup = defaultdict(list)
    for keyBag in bagBagStringLookup:
        for bagString in bagBagStringLookup[keyBag]:
            if bagBagStringLookup[keyBag][0] != "no other bags.":
                firstSpace = bagString.find(" ")
                lastSpace = bagString.rfind(" ")
                bagBagLookup[keyBag].append((int(bagString[:firstSpace]), bagString[firstSpace + 1:lastSpace]))

    reverseBagBagLookup = defaultdict(list)
    for keyBag in bagBagLookup:
        for canHold, valueBag in bagBagLookup[keyBag]:
            reverseBagBagLookup[valueBag].append(keyBag)

    checkFor = {"shiny gold"}
    matches = {"shiny gold"}

    while checkFor:
        newCheckFor = set()
        for check in checkFor:
            for match in reverseBagBagLookup[check]:
                if match not in matches:
                    newCheckFor.add(match)

                matches.add(match)
            
        checkFor = newCheckFor
    
    matches.remove("shiny gold")

    #reverseBagBagLookup = {valueBag if else valueBag: [] for keyBag in bagBagLookup for canHold, valueBag in bagBagLookup[keyBag]}

    #print(reverseBagBagLookup)
    #print(reverseBagBagLookup["shiny gold"])
    print(len(matches))

    print(countBags(bagBagLookup, "shiny gold"))



