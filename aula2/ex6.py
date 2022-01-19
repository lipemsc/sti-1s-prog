alt = float(input("Insira a altura: "))
comp = float(input("Insira a comprimento: "))
area = alt * comp

if alt == comp:
    print("Quadrado")
else:
    print("Rectangulo")
print("Área: {0}".format(area))