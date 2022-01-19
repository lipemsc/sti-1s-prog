nalunos = int(input("Insira o nº de alunos: "))
somaaltura = 0
somaidade = 0

for i in range(nalunos):
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    somaidade += idade
    somaaltura += altura

    try:
        if maxaltura < altura:
            maxaltura = altura
        if minidade > idade:
            minidade = idade
    except NameError:
        minidade = idade
        maxaltura = altura

print("O aluno mais alto tem ", maxaltura, "cm de altura", sep="")
print("O aluno mais novo tem", minidade, "anos")
print("Media idade: ", somaidade/numalunos)
print("Media alt: ", somaltura/numalunos)