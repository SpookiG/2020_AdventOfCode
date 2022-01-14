passportFields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid",
}

passportChecks = {
    "byr": lambda v : int(v) >= 1920 and int(v) <= 2002,
    "iyr": lambda v : int(v) >= 2010 and int(v) <= 2020,
    "eyr": lambda v : int(v) >= 2020 and int(v) <= 2030,
    "hgt": lambda v : (v[-2:] == "cm" and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or (v[-2:] == "in" and int(v[:-2]) >= 59 and int(v[:-2]) <= 76),
    "hcl": lambda v : len(v) == 7 and v[0] == "#" and colCheck(v[1:]),
    "ecl": lambda v : v in { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" },
    "pid": lambda v : len(v) == 9 and int(v),
    "cid": lambda v : True,
}

def colCheck(col):
    for c in col:
        if (ord(c) not in range(ord("0"), ord("9") + 1)
            and ord(c) not in range(ord("a"), ord("f") + 1)):
            return False
    
    return True


with open("day4input.txt") as file:
    passports = []
    passportString = ""

    for line in file:
        if line.strip() == "":
            passports.append({entry.split(":")[0].strip(): entry.split(":")[1].strip() for entry in passportString.split()})
            passportString = ""
            continue

        passportString += line
    
    
    validPassports = []
    for p in passports:
        valid = True
        for f in passportFields:
            if f not in p:
                valid = False
        
        validPassports.append(valid)
    
    print(len(validPassports))
    print(validPassports.count(True))


    updatedValidPassports = []
    for p in passports:
        valid = True
        try:
            for k in p:
                if not passportChecks[k](p[k]):
                    valid = False
        except:
            valid = False
        
        updatedValidPassports.append(valid)
            

    print([old and new for old, new in zip(validPassports, updatedValidPassports)].count(True))
