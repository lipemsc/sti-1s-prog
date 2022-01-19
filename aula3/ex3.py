notas = {
    "matematica": float(input("Insira a nota de Matemática: ")),
    "portugues": float(input("Insira a nota de Português: ")),
    "ingles": float(input("Insira a nota de Inglês: ")),
    "geografia": float(input("Insira a nota de Geografia: "))
}
sum = 0
for i in notas:
    sum += notas[i]
print("A média é ", sum / len(notas))
