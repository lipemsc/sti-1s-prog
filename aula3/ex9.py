turmas = int(input("Nº turmas: "))

mnovo = 999
mvelho = -1
raparigas = 0
notamalta = -1

for i in range(turmas):
    nalunos = int(input("Nº alunos: "))
    for j in range(nalunos):
        idade = int(input("Idade: "))
        genero = int(input("Genero: "))
        nota = int(input("Nota de entrada: "))

        if idade < mnovo:
            mnovo = idade
            tmaisnovo = i+1

        if idade > mvelho:
            mvelho = idade
            tmaisvelho = i+1

        if genero == 0:
            raparigas += 1

        if notamalta < nota:
            notamalta = nota
            gennotamalta = genero
            tnotamalta = i+1

print("Turma aluno mais novo:", tmaisnovo)
print("Turma aluno mais velho:", tmaisvelho)
print("Raparigas:", raparigas)
print("Turma maior nota:", tnotamalta)
print("Nota mais alta:", notamalta, "Genero:", gennotamalta)
