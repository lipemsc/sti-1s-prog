#  se ler o cartao de cidadao, como e que vou determinar o nome???? assumindo que é para ler o nome e nao o CC

minAge = 999
minAgeName = ""

while True:
    age = int(input("Insert age: "))
    if age == 999:
        break
    name = input("Insert name: ")
    if age < minAge:
        minAge = age
        minAgeName = name
print("Youngest person is {0} and they're {1} years old".format(minAgeName, minAge))

