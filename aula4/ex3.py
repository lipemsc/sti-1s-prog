nums = list()

for i in range(int(input("Insira o tamanho da lista: "))):
    nums.append(int(input("Insira o {0} valor: ".format(i + 1))))

try:
    nums.index(int(input("Introduza o valor a procurar: ")))
except ValueError:
    print("Não encontrei")
else:
    print("Encontrei")