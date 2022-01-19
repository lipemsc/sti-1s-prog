# JOGO DO GALO
#
#  1 | 2 | 3
#  4 | 5 | 6
#  7 | 8 | 9
#
# Layout ^
#        |
#


def draw_logo():
    print("""BEM VINDO AO
   _                         _                     _       
  (_) ___   __ _  ___     __| | ___     __ _  __ _| | ___  
  | |/ _ \\ / _` |/ _ \\   / _` |/ _ \\   / _` |/ _` | |/ _ \\ 
  | | (_) | (_| | (_) | | (_| | (_) | | (_| | (_| | | (_) |
 _/ |\\___/ \\__, |\\___/   \\__,_|\\___/   \\__, |\\__,_|_|\\___/ 
|__/       |___/                       |___/      
""")


def draw_positions(positions):
    print("| ", sep="", end="")
    for i, j in enumerate(positions):
        if i == 3 or i == 6:
            print("\n| ", sep="", end="")
        if j == 1:
            print("X", sep="", end="")
        elif j == 2:
            print("O", sep="", end="")
        else:
            print(" ", sep="", end="")
        print(" | ", sep="", end="")
    print("")


def check_win(positions):
    if positions[0] == positions[1] == positions[2] != 0:
        return positions[0]
    elif positions[3] == positions[4] == positions[5] != 0:
        return positions[3]
    elif positions[6] == positions[7] == positions[8] != 0:
        return positions[6]
    elif positions[0] == positions[3] == positions[6] != 0:
        return positions[0]
    elif positions[1] == positions[4] == positions[7] != 0:
        return positions[1]
    elif positions[2] == positions[5] == positions[8] != 0:
        return positions[2]
    elif positions[0] == positions[4] == positions[8] != 0:
        return positions[0]
    elif positions[2] == positions[4] == positions[6] != 0:
        return positions[2]
    else:
        return 0


def player_prompt(positions, player):
    while True:
        pos = int(input("Jogador {0}: ".format(player + 1))) - 1
        if positions[pos] == 0:
            positions[pos] = player + 1
            break
    return positions


draw_logo()
positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 1
while check_win(positions) == 0:
    i += 1
    positions = player_prompt(positions, i % 2)
    draw_positions(positions)
winner = check_win(positions)

print("** PARABENS **\nO jogador {0} ganhou".format(winner))
