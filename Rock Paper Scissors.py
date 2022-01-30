#Julian Meyer
#Make a menu for the game with instructions 
#We are making a code to play rock paper scissors.
# #Psuedocode: Have computer randomly generate rock paper or scissors
# Computer should transfer the user input into numbers
# Make if statements for each scenario
# Loop yes or no to reset the game
# Failsafe for if the input a letter instead of a number
# Misspelling scenario failsafe
import os, random
os.system=('cls')
def menu():
    print("<**************************>")
    print("<       WELCOME TO         >")
    print("<          ROCK            >")
    print("<          PAPER           >")
    print("<          SCISORS         >")
    print("<**************************>")
    print("<In this Game, 1 = Rock, 2 = Paper, and 3 = Scisors>")
    print("                                                    ")
rockpaperscissors=random.randint(1,3)




menu()

# user='paper'
# computer = 1
# import os
# os.system('cls')
# if 'pap' in user:
#     user = int(1)
#     print("paper"+str(user))
# elif 'r' in user:
#     user=int(2)
# elif 's' in user:
#     user=int(3)

