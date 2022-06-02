# ```python
#    ____
#    ____
#    ____
#    ____
# ```


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Boggle:
    def __init__(self,char="_"):
        self.char = char

    def board_set_up(self):
        print(f"""Press 'Shake' to Boggle!
{self.char}{self.char}{self.char}{self.char}
{self.char}{self.char}{self.char}{self.char}
{self.char}{self.char}{self.char}{self.char}
{self.char}{self.char}{self.char}{self.char}
""")
    


    def shake(self):
        import string
        import random
        charArr = []
        alphabet = (string.ascii_uppercase)
        for char in alphabet:
            charArr.append(char) 
        charArr[16] = "Qu"
        rando = random.randint(0,25)
        char = charArr[rando]
        print(f"""Press 'Shake' to Boggle!
{char}{char}{char}{char}
{char}{char}{char}{char}
{char}{char}{char}{char}
{char}{char}{char}{char}
""")
    


boggle = Boggle()
# print(boggle.board_set_up())
# Output:
# Press 'Shake' to Boggle!
# ____
# ____
# ____
# ____
# (4 rows of 4 "_")

# -=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-

new_game = boggle.board_set_up()
# new_game.shake()
new_shake = boggle.shake()
# output: right format, but a full Boggle of only one letter




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
# # prints random uppercase charecter

