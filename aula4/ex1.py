values = []
pares = 0
impares = 0

for i in range(10):
    values.append(int(input("Insira o {0} valor: ".format(i + 1))))

values.sort()
print("Diferenca:", values[9] - values[0])

for value in values:
    if value % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Impares:", impares)
