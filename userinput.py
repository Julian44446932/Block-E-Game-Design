import os, random
os.system('cls')

#Julian Meyer
#1/21/2022

#We are going to learn the input() function, random numbers
# #type casting, branching. looping
#declare variable for user input
#input returns a string we must type cast if we need a number
# print("enter a number from 1-10: ",end="^")
# userInfo=int(input())
# print("The number is %.2f" %(userInfo/3))
guess=int(input("Please give a number"))
correct_number = random.ranintt(1,10)
GameOn=True
while(GameOn):



    if guess> correct_number:
        print("Sorry, the number is too big, guess again")
    if guess < correct_number:
        print("Sorry, that number was too small, guess again")
    if guess == correct_number:
        print("You are correct!!") 
