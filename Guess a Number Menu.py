from multiprocessing.connection import answer_challenge
import os, random
from traceback import print_tb
os.system('cls')
print("**Guess a number menu**")
print("Level 1: 1-10")
print("Level 2: 1-50")
print("Level 3: 1-100")
difficulty=input("Which level do you want:")
guess=int(input("Please give a number:"))
# correctanswer = random.randint(1,10)
# if guess == correctanswer:
#     print("You are correct.")
# if guess > correctanswer:
#     print("Sorry, your answer was too large.")
# if guess < correctanswer:
#     print("Sorry, your answer was too small.")
#     quit()

if int(difficulty)==1:
    correctanswer=random.randint(1,10)
elif guess=="quit":
    print("come back soon!")
    quit()
if int(guess) < correctanswer:
    print("Try higher")
if int(guess) > correctanswer:
    print("try lower")
if int(guess) == correctanswer:
    print("You got it!")
    quit()

