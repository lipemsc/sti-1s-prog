import os
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def debug(positions):
    for i in positions:
        print(i)


def draw_logo():
    print("""BEM VINDO AO
    mm                              \"\"#      "           #            
   m"#          mmm   mmmmm           #    mmm    m mm   # mm    mmm  
  #" #         #"  #  # # #           #      #    #"  #  #"  #  "   # 
 #mmm#m        #\"\"\"\"  # # #           #      #    #   #  #   #  m\"\"\"# 
     #         \"#mm\"  # # #           "mm  mm#mm  #   #  #   #  \"mm\"# 
""")


def draw_positions(positions):
    for i in positions:
        print("|", sep="", end="")
        for j in i:
            if j == 1:
                print(" \u25CB |", end="")
            elif j == 2:
                print(" \u25CF |", end="")
            else:
                print("   |", end="")
        print("")


def check_win(positions):
    #debug(positions)
    count = [0, 0]

    # horizontal verification
    for line in positions:
        for cell in line:
            if cell == 0:
                count = [0, 0]
            elif cell == 1:
                count[0] += 1
                count[1] = 0
            elif cell == 2:
                count[1] += 1
                count[0] = 0
            if count[0] >= 4:
                return 1
            if count[1] >= 4:
                return 2
        #print(count)
    
    count = [0, 0]

    for x in range(len(positions[0])):
        for y in range(len(positions)):
            if positions[y][x] == 0:
                count = [0, 0]
            elif positions[y][x] == 1:
                count[0] += 1
                count[1] = 0
            elif positions[y][x] == 2:
                count[1] += 1
                count[0] = 0
            if count[0] >= 4:
                return 1
            if count[1] >= 4:
                return 2
        #print(count)


    for y in range(len(positions)):
        for x in range(len(positions[y])):
            count = [0, 0]
            for i in range(4):
                try:
                    if positions[y+i][x+i] == 1:
                        count[0] += 1
                    if positions[y+i][x+i] == 2:
                        count[1] += 1
                except IndexError:
                    continue
                if count[0] >= 4:
                    return 1
                if count[1] >= 4:
                    return 2
            
            count = [0, 0]
            for i in range(4):
                try:
                    if x-i < 0:
                        continue
                    if positions[y+i][x-i] == 1:
                        count[0] += 1
                    if positions[y+i][x-i] == 2:
                        count[1] += 1
                except IndexError:
                    continue
                if count[0] >= 4:
                    return 1
                if count[1] >= 4:
                    return 2

    return 0

def player_prompt(positions, player):
    play = int(input("Insira a linha para jogar: "))
    for i in range(7, -1, -1):
        if positions[i][play - 1] == 0:
            positions[i][play - 1] = player + 1
            break
    return positions


    #while True:
    #    pos = int(input("Jogador {0}: ".format(player + 1))) - 1
    #    if positions[pos] == 0:
    #        positions[pos] = player + 1
    #        break
    #return positions


draw_logo()
sleep(2)
positions = [[0, 0, 0, 0, 0, 0, 0, 0],  # [y][x]
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]


#positions[0][5] = 1

i = 1

while check_win(positions) == 0:
    i += 1
    clearConsole()
    print(f"Jogador {(i % 2) + 1}")
    draw_positions(positions)
    positions = player_prompt(positions, (i % 2))
clearConsole()
draw_positions(positions)
winner = check_win(positions)

print("** PARABENS **\nO jogador {0} ganhou".format(winner))
