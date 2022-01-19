def apelidofst():
    name = input("Insira nome: ").split()
    print(name[-1], end=", ")
    for i in range(len(name) - 1):
        print(name[i], end=" ")


apelidofst()
