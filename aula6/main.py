import quatroemlinha
import galo

print("Bundle de jogos\n\n1. Jogo do Galo\n2. Jogo do 4 em linha\n")

option = int(input("Que jogo pretende jogar? "))
if option == 1:
    quatroemlinha.clearConsole()
    galo.start()
elif option == 2:
    quatroemlinha.clearConsole()
    quatroemlinha.start()