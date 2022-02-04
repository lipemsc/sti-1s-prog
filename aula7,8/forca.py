import os

class Game:
    def __init__(self, word):
        self.misses = []
        self.word = list(word)
        self.guessed = []
        for i in range(len(word)):
            if self.word[i] == " ":
                self.guessed.append(" ")
            else:
                self.guessed.append(None)

    def clear(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def make_play(self,character):
        try:
            character = list(character)[0]
        except IndexError:
            return -1
       
        if (character.lower() in self.word or character.upper() in self.word) and not character in self.guessed:
            for i in range(len(self.word)):
                if self.word[i] == character.lower() or self.word[i] == character.upper():
                    self.guessed[i] = self.word[i]
        else:
            self.misses.append(character)
    
    def debug(self):
        print(self.word)
        print(self.guessed)
    
    def print_humanoid(self):
        mcount = len(self.misses)
        print(" _________")
        for i in range(12):
            print("|", end="")
            if i == 1 or i == 0:
                print("         |", end="")
            if i == 2 and mcount >= 1:
                print("        / \\", end="")
            if i == 3 and mcount >= 1:
                print("        \ /", end="")
            if i == 4 and mcount >= 2:
                print("         |", end="")
            if i == 5:
                if mcount >= 3:
                    print("    -----", end="")
                else:
                    print("         ", end="")
            if i == 5 and mcount >= 2:
                print("|", end="")
            if i == 5 and mcount >= 4:
                print("-----", end="")
            if i == 6 and mcount >= 2:
                print("         |", end="")
            if i == 7:
                if mcount >= 5:
                    print("        /", end="")
                else:
                    print("         ", end="")
            if i == 7:
                if mcount >= 6:
                    print(" \\", end="")
            if i == 8:
                if mcount >= 5:
                    print("       /", end="")
                else:
                    print("        ", end="")
            if i == 8:
                if mcount >= 6:
                    print("   \\", end="")
            print()

    
    def print_guess(self):
        for character in self.guessed:
            if character == None:
                print("_", end="")
            else:
                print(character, end="")
        print()
    
    def print_misses(self):
        for miss in self.misses:
            print(f"{miss}," ,end="")
        print("\b ")

    def verify_win(self):
        if not None in self.guessed:
            return True
        else:
            return False
    
    def verify_loss(self):
        if len(self.misses) >= 6:
            return True
        else:
            return False
        


game = Game(input("Insira a palavra:").strip())

while True:
    game.clear()
    game.print_humanoid()
    game.print_guess()
    game.print_misses()
    if game.verify_win() == True:
        print("Ganhaste!")
        break
    if game.verify_loss() == True:
        print("Perdeste!")
        break
    game.make_play(input("Insira uma letra: "))
    
