alunomaisnovo = 999 # O aluno mais novo da turma
nometurmaalunomaisnovo = "" # O nome da turma com o aluno mais novo
turmaalunomaisnovo = 999 # A idade do aluno mais novo de todas as turmas

alunomaisvelho = -1 # O aluno mais novo da turma
nometurmaalunomaisvelho = "" # O nome da turma com o aluno mais novo
turmaalunomaisvelho = -1 # A idade do aluno mais novo de todas as turmas

alunomaiornota = -1 # O aluno mais novo da turma
nometurmaalunomaiornota = "" # O nome da turma com o aluno mais novo
turmaalunomaiornota = -1 # A idade do aluno mais novo de todas as turmas


raparigas = 0
notamaisalta = -1


for i in range(int(input("Quantas turmas: "))):

    alunomaisnovo = 999
    alunomaisvelho = -1
    alunomaiornota = -1

    print()
    nomecurso = input("Qual é o nome do curso?: ")
    print()
    for j in range(int(input("Quantos alunos tem a tua turma: "))):
        print()
        idade = int(input("Qual é a idade do aluno: "))
        genero = int(input("Insira o genero masculino - 1, feminino - 0: "))
        notadadisciplina = float(input("Insira a nota da disciplina: "))
        print()
        if genero == 0:
            raparigas += 1

        if idade < alunomaisnovo:
            alunomaisnovo = idade

        if idade > alunomaisvelho:
            alunomaisvelho = idade

        if notadadisciplina > alunomaiornota:
            alunomaiornota = notadadisciplina

        if notamaisalta < notadadisciplina:
            notamaisalta = notadadisciplina
            generodanotamaisalta = genero

    if alunomaisnovo < turmaalunomaisnovo:
        turmaalunomaisnovo = alunomaisnovo
        nometurmaalunomaisnovo = nomecurso

    if alunomaisvelho > turmaalunomaisvelho:
        turmaalunomaisvelho = alunomaisvelho
        nometurmaalunomaisvelho = nomecurso

    if alunomaiornota > turmaalunomaiornota:
        turmaalunomaiornota = alunomaiornota
        nometurmaalunomaiornota = nomecurso


print("O nome da turma que tem o(a) aluno(a) mais novo(a) é a turma: ",nometurmaalunomaisnovo)
print("A turma que tem o(a) aluno(a) mais velho(a) é a: ",nometurmaalunomaisvelho)
print("Existem ",raparigas," rapariga(s) no TeSP de ISE-DEE")
print("A turma com o(a) aluno(a) que tem a nota de entrada mais alta é: ",nometurmaalunomaiornota)
print("A nota da entrada mais alta é",notamaisalta,"e o genero dessa nota foi ",genero)
