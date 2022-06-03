# ```python
#    ____
#    ____
#    ____
#    ____
# ```


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class Boggle:
#     def __init__(self,char="_"):
#         self.char = char

#     def board_set_up(self):
#         print(f"""Press 'Shake' to Boggle!
# {self.char}{self.char}{self.char}{self.char}
# {self.char}{self.char}{self.char}{self.char}
# {self.char}{self.char}{self.char}{self.char}
# {self.char}{self.char}{self.char}{self.char}
# """)
    


#     def shake(self):
#         import string
#         import random
#         charArr = []
#         alphabet = (string.ascii_uppercase)
#         for char in alphabet:
#             charArr.append(char) 
#         charArr[16] = "Qu"
#         rando = random.randint(0,25)
#         char = charArr[rando]
#         print(f"""Press 'Shake' to Boggle!
# {char}{char}{char}{char}
# {char}{char}{char}{char}
# {char}{char}{char}{char}
# {char}{char}{char}{char}
# """)
    


# boggle = Boggle('_')
# print(boggle.board_set_up())
# # Output:
# Press 'Shake' to Boggle!
# ____
# ____
# ____
# ____
# (4 rows of 4 "_")

# -=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-

# boggle.shake()
# # output: right format, but a full Boggle of only one letter
# print(new_shake)

# Problem lies in how i add letters to my boggle board.
# i need a radminized number for every push, push it into something, then return it in board format
# i can do this with rows (x,y) and possibly while loops


# -=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--
# addtional working code:

# random letter generator

# import string
# import random

# charArr = []
# alphabet = (string.ascii_uppercase)
# for char in alphabet:
#     charArr.append(char)
# charArr[16] = "Qu"
# # print(charArr)
# # prints updated array of letters
# rando = random.randint(0,25)
# print(charArr[rando])
# prints random uppercase charecter

# -=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import string
import random
class Boggle:
    def __init__(self,char='_'):
        print('Welcome to Boggle!')
        self.char = char
        for x in range(4):
            print(f"{char}"*4)

    def shake(self):
        num = 1
        charArr = []
        alphabet = (string.ascii_uppercase)
        for char in alphabet:
                charArr.append(char)
        charArr[16] = "Qu"
        print(f' --Shake {num}--')
        for x in range(4):
            row = ''
            for y in range(4):
                rando = random.randint(0,25)
                row += (f" {charArr[rando]} ")
            print(row + '\r')
        num += 1

new_game = Boggle()
print(new_game) 
# output:
# Welcome to Boggle!
# ____
# ____
# ____
# ____
new_game.shake()
# output: 
# --Shake 1--
#  G  P  L  K 
#  L  C  C  T 
#  T  K  M  Qu 
#  K  V  V  T 

# next steps: work on making randomized dice with randomized letters, 
# track used letters so they dont repeat the charecter next to each other