def readlist():
    numlist = []
    for i in range(10):
        numlist.append(int(input("Insira o numero {0}: ".format(i+1))))
    return numlist


def getDifference(numlist):
    numlist.sort()
    diff = numlist[9] - numlist[0]
    return diff


def getPairs(numlist):
    pares = 0
    impares = 0
    for i in numlist:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


print(getDifference(readlist()))