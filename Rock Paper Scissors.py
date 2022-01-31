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
    print("         Select 1, 2, or 3.                 ")
    print("                                                    ")
menu()
choice=int(input("Choice: "))
check=True
while check:
    try:
        choice=int(input("Choice:  "))
        check=False
    except ValueError:
        print("Sorry, wrong choice, please answer 1, 2, or 3 only.")
    

if int(choice) > 3:
    print("Enter valid level please.")
elif choice == 1:
    myNumber= random.randint(1,3)
elif choice == 2:
    myNumber= random.randint(1,3)
elif choice == 3:
    myNumber= random.randint(1,3) 

print(choice)
GameOn=True

while(GameOn):
    userGuess=int(input("Give me a number "))
    if myNumber ==userGuess:
        print("You won!!")
        GameOn=False
    else:
        print("Good luck next time", myNumber)
print("The number to guess was "+str(myNumber))
os.system=('cls')











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
