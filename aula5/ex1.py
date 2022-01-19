def potencia(num, expo):
    result = 1
    for i in range(expo):
        result = result * num
    return result


n1 = int(input("Insira o num: "))
n2 = int(input("Insira o expoente: "))
print("O resultado é", potencia(n1, n2))
