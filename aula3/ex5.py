n1 = int(input("Insira o 1º num: "))
n2 = int(input("Insira o 2º num: "))

sum = 0
for i in range(n1, n2 + 1):
    sum += i
print(sum)