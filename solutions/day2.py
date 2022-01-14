with open("day2input.txt") as file:
    passwords = []
    policies = []

    for line in file:
        pwdSplit = line.strip().split(": ")
        passwords.append(pwdSplit[1])

        polSplit = pwdSplit[0].split(' ')
        rangeSplit = polSplit[0].split('-')
        pol = (polSplit[1], int(rangeSplit[0]), int(rangeSplit[1]))
        policies.append(pol)
    

    policyMet = [1 if (pwd.count(pol[0]) >= pol[1] and pwd.count(pol[0]) <= pol[2]) else 0
        for (pwd, pol) in zip(passwords, policies)]

    print(sum(policyMet))

    newPolicyMet = [1 if ((pol[0] == pwd[pol[1]-1]) != (pol[0] == pwd[pol[2]-1])) else 0
        for (pwd, pol) in zip(passwords, policies)]

    print(sum(newPolicyMet))

    #print(passwords)
    #print("\n\n")
    #print(policies)

