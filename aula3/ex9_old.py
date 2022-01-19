talunomaisnovo = 999
talunomaisvelho = -1
raparigas = 0
cursonotamaisalta = 0
notamaisalta = 0


for i in range(int(input("Insira o nº de turmas:")) - 1):
    alunomaisnovo = 999
    alunomaisvelho = -1
    for j in range(int(input("Insira o nº de alunos:")) - 1):
        currentidade = int(input("Insira a idade do aluno: "))
        currentgenero = int(input("Insira o genero do aluno (1- Masculino; 0- Feminino): "))
        if currentgenero == 0:
            raparigas += 1


        currentnota = int(input("Insira a nota do aluno: "))
        if currentidade > alunomaisvelho:
            alunomaisvelho = currentidade
        if currentidade < alunomaisnovo:
            alunomaisnovo = currentidade
    if talunomaisvelho < alunomaisvelho:
        talunomaisvelho = alunomaisvelho
    if talunomaisnovo > alunomaisnovo:
        talunomaisnovo = alunomaisnovo