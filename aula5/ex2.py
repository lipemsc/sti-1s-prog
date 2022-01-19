def maiorAlgarismo(num):
    for i in list(str(num)):
        if 'maior' not in vars() or maior < i:
            maior = i
    return maior


print(maiorAlgarismo(int(input("Insira o num: "))))
