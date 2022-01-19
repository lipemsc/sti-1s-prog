def genInitials(string):
    words = string.split()
    initials = ""
    for i in words:
        initials += i[0]
    return str(initials)

notas = {}
for i in range(int(input("Numero de UC's: "))):
    nomeuc = input("Insira o nome da UC: ")
    notas[nomeuc] = int(input("Insira a nota da UC: "))

for i in notas:
    print(genInitials(str(i)), "-", notas[i])