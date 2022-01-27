from quatroemlinha import start as startquatroemlinha
from quatroemlinha import clearConsole
from galo import start as startgalo
from gloria import start as startgloria

print("Bundle de jogos\n\n1. Jogo do Galo\n2. Jogo do 4 em linha\n3. Jogo da Glória\n")

option = int(input("Que jogo pretende jogar? "))
if option == 1:
    clearConsole()
    startgalo()
elif option == 2:
    clearConsole()
    startquatroemlinha()
elif option == 3:
    clearConsole
    startgloria()