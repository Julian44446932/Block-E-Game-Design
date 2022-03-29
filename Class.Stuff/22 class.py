#JUlian Myer
#01/31/22
#Strings array of characters
#Has many functions

import os, random
os.system('cls')
myName= "Julians Meyer"
myStatement=""" My name is so nice because 
sd
s
d
fd"""
print("My last name begins with " +myName[6])
print(myStatement)
if 'blah' in myStatement:
    print('true')
print('expert' not in myStatement)
INDEX= myName.find("J")
#find() will return the index of the character you are looking for (first instance)
print(INDEX)
#finding the length of your word
wordLen=len(myName)
print(wordLen) #your last index in len-1
#For loop in range 0 to limit
for i in range(wordLen-1):
    if "e" in myName[i]:
        print(i, end=", ")
print("")
print("done")
myStatement=myStatement.upper()
print(myStatement)


for elem in myName:
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words=["Radio", "Clues", "suite", "peter", "robot"]
word=random.choice(words)
print(word)
check=True
while check:
    letter=input("Dear user, please give us a nice letter ")
    if len(letter)>1 or not letter.isalpha():
        print("BaD")
    else:
        check=False
print("ready to play the game")
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end = "")
else:
    print("_", end=" ")


