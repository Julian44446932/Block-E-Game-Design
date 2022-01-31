#Julian Meyer
#Make a menu for the game with instructions 
#We are making a code to play rock paper scissors.
# #Psuedocode: Have computer randomly generate rock paper or scissors
# Computer should transfer the user input into numbers
# Make if statements for each scenario
# Loop yes or no to reset the game
# Failsafe for if the input a letter instead of a number
# Misspelling scenario failsafe
from multiprocessing.sharedctypes import Value
import os, random
from urllib import response
os.system=('cls')
def menu():
    print("<**************************>")
    print("<       WELCOME TO         >")
    print("<          ROCK            >")
    print("<          PAPER           >")
    print("<          SCISORS         >")
    print("<**************************>")
    print("<In this Game, 1 = Rock, 2 = Paper, and 3 = Scisors>")
    print("         Select r, p, or s                ")
    print("                                                    ")

menu()
userGuess= input("What is your choice:")
GameOn=True
ValueError!=int
# check=True
# while check:
#     try:
# choice=int(input("Choice:  "))
#         check=False
#     except ValueError:
#         print("Sorry, wrong choice, please answer r, p, or s only.")

myNumber= random.randint(1,3) 

while GameOn==True:
    if ValueError:
        print("You can't choose that! TRy again.")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 1 and int(myNumber)==2:
        print("You Won! Rock beats paper!!!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 1 and int(myNumber)==3:
        print("You Lost!! Rock beats scissors!!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 1 and int(myNumber)==1:
        print("You tied. We both picked rock!!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 2 and int(myNumber)==2:
        print("You tied. We both picked paper!!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 2 and int(myNumber)==3:
        print("You lost!! Scisors beats paper!!")
        quit()
    elif int(userGuess) == 2 and int(myNumber)==1:
        print("You won!! Paper beats rock!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 3 and int(myNumber)==2:
        print("You won!! Scisors beats paper!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 3 and int(myNumber)==3:
        print("We tied. We both picked paper!")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()
    elif int(userGuess) == 3 and int(userGuess)==1:
        print("You lost!! Rocks beats scissors")
        repeat=input("Do you want to try again (y for yes,n for no):")
        if repeat=="y":
            os.system('cls')
            menu()
            myNumber=random.randint(1,3)
            userGuess=input ("What is your choice:")
        elif repeat=="n":
            GameOn=False
            quit()






    #     print("You Lost!!!")
    # if myNumber == 2:
    #     print("You Tied!!!")
    # if myNumber == 3:
    #     print("You won!!")


# while(GameOn):
#     userGuess=int(choice)
#     if myNumber ==userGuess:
#         print("You won!!")
#         GameOn=False
#     else:
#         print("Good luck next time", myNumber)
# print("You beat the computer.")
# os.system=('cls')











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
