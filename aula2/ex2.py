from random import uniform


a = uniform(1, 10)
b = uniform(1, 10)
c = uniform(1, 10)

print(a, b, c)

preSqrt = b * b - 4.0 * a * c
sqrt = preSqrt ** 0.5
if sqrt < 0:
    print("Não existem raízes reais")
else:
    if a == 0:
        print("Erro divisão por zero")
    else:
        x1 = (-b + sqrt) / (2.0 * a)
        x2 = (-b - sqrt) / (2.0 * a)

        print(x1)
        print(x2)
