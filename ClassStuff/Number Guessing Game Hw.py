#Julian Meyer
#1/26/22
#Program to make a game where you can guess numbers
import os
os.system('cls')
import os, random
os.system('cls')

#Today we are learning to try and except, funtions, elif

# Let's make menu a function keyword def
def menu():
    print('########################################')

    print('#          Guess A Number Menu         #')

    print('#                                      #')

    print('#         1.  Choices 1-10             #')

    print('#         2.  Choices 1-50             #')

    print('#         3.  Choices 1-100            #')

    print('#           Select your choice         #')

    print('######################################')
#Checking for correct user input
menu()  #calling the funciton menu
check=True
while check:
    try:
         choice=int(input("Choice: "))
         check=False
    except ValueError:
        print("Sorry, wrong choice, please answer 1 to 3 only")

if int(choice) > 3:
    print ("that's not a level try again")
    quit()
elif choice == 1:
     myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
     myNumber= random.randint(1,100)

print(choice)

GameOn=True

while(GameOn):

    userGuess=int(input("give me a number "))

    if myNumber ==userGuess:

        print("You guessed it!")

        GameOn=False

    else:

        print("good luck next time", myNumber)

print("The number to guess was " + str(myNumber))
os.system('cls')