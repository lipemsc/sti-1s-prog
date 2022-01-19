def menorAlgarismo(num):
    for i in list(str(num)):
        if 'maior' not in vars() or maior > i:
            maior = i
    return maior


print(menorAlgarismo(int(input("Insira o num: "))))
