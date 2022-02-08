##JulianMeyer
#02/08/22
#Word game with 3 levels
#1. Fruits
#2. Animals
#3. COmputer parts
# Choice.
import os, random
os.system('cls')
def menu():
    print("<<<<< Menu >>>>>")
    print("=> 1) Fruits")
    print("=> 2) Animals")
    print("=> 3) Computer Parts")
    print("Select 1, 2, or 3")
    print("                    ")
menu()


fruits=["bananas", "grapes", "watermelon", 'oranges', 'tomatoes', 'mangos', "kiwis", 'strawberry', 'apples', 'blackberries', 'blueberries', 'mangos']
# size= len(fruits)
# randy=random.randint(0,size)
# print(randy)
# word=fruits[randy]
# print(word)
guess=""
word=random.choice(fruits)
def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("enter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
        except ValueError:
            print("only one letter please")
gameOn=True
tries=0
letterGuessed=""

while gameOn:
    guessFunction()
    letterGuessed += guess #letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries) #for testing delete game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end= " ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries > 6:
        print("\n Sorry run out chances ")
        #playgame() ask if they want to play again
    if countLetter == len(word):
        print("you guessed it!")
        #Calculate score do it
        #play game()
    






