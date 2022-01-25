from multiprocessing.connection import answer_challenge
import os, random
os.system('cls')
print("**Guess a number menu**")
guess=int(input("Please give a number"))
correctanswer = random.randint(1,10)
if guess == correctanswer:
    print("You are correct.")
if guess > correctanswer:
    print("Sorry, your answer was too large.")
if guess < correctanswer:
    print("Sorry, your answer was too small.")
    quit()



