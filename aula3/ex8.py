initNum = int(input("Insira o número: "))
num = initNum

factoracao = list()

while num != 1:  # vai diminuindo a var num até que esta seja 1, será feita uma divisão depois
    for i in range(2, int(num + 1)): # o i percorre desde 2 até valor da var num
        if num % i == 0:  # verifica se o i é divisivel por num
            factoracao.append(i)  # quando verifica qual o menor divisor, adiciona-o para a lista factoracao que foi declarada na linha 4
            num = num / i # divide a var num para que o programa acabe eventualmente
            #  print(i, num)
            break

print(factoracao)
print(initNum, "=", sep="", end="") # print o valor bonito
for x, i in enumerate(factoracao):
    if x == 0:
        print(i, sep="", end="")
    else:
        print("x", i, sep="", end="")
print()
