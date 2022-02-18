# CArd War game
import os, random
os.system('cls')
numberCards=[]
for i in range(2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[i-2])
print(numberCards)
suit=['s', 'c', 'h', 'd']
royals=['J', 'Q', 'K', 'A']
cardTypes=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# make a list like this (2,3,4,5,6,7,8,9,10,J,Q,K)
#make a deck of cards addding each suit