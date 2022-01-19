def order(numList):  # bubble sort
    for i in numList:
        for j in range(len(numList) - 1):
            if numList[j] > numList[j + 1]:
                tmp = numList[j + 1]
                numList[j + 1] = numList[j]
                numList[j] = tmp
    return numList


nums = list()

for i in range(int(input("Insira o tamanho da lista: "))):
    nums.append(int(input("Insira o {0} valor: ".format(i + 1))))

nums = order(nums)
print(nums)