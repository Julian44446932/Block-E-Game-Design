#first let's import random since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ['♥',"♦", "♣", "♠"]
royals = ["J", "Q", "K", "A"]
tempplayer1 = []
tempplayer2 = [] 
halfDeck=0 

#using loops and append to add our content to numberCards :

def carddecks():
    for i in range(2,11):
        numberCards.append(str(i))

    for i in range(2,11):
        numberCards.append(str(i))
    #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
    #this will add the card faces to the base list
#Create full deck

    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
        #this adds the information to the "full deck" we want to make
#you can print the deck here, if you want to see how it looks


# print(deck)
#now let's see the deck!

def printdeck():
    global row, col
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
#now let's shuffle our deck!
#Shuffle the deck cards
def realShuffle():
    global player1
    global player2

    random.shuffle(deck)
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])

# you could print it again here just to see how it shuffle
#loop to devide the cards to each player
def splitcards():
    global halfDeck
    halfDeck=int(len(deck)/2)



        # if 2==0:
        #     player1.append(deck[1])
        # else:
        #     player2.append(deck[1])


# print("player1 ",player1)
# print()
# print("player2 ",player2)


    #ask user to hit a key to release cards
halfDeck=int(len(deck)/2)  
GameOn=True
while GameOn:
    carddecks()
    splitcards()
    realShuffle()
    numberofcards = 0
    for i in range (0,halfDeck):
        click=input("Press [enter] to get cards")
        print("Player 1     Player 2")
        print("     "+player1[i]+"      "+player2[i])
        if player1[i]>player2[i]:
            tempplayer1.append(player1[i])
            tempplayer1.append(player2[i])
        elif player1[i]<player2[i]:
            tempplayer2.append(player1[i])
            tempplayer2.append(player2[i])
        elif player1[i]==player2[i]:
            tempplayer1.append(player2[i])
            tempplayer2.append(player2[i])
if (len(tempplayer2)) == 0:
        print("player 1 won the game!")
        gameon = False
elif (len(tempplayer1)) == 0:
        print("player 2 won the game!")
        gameon = False
else:
    print("in", halfDeck)
    print("length =", len(player1))
    for j in range (0, int(halfDeck/2)):
        player1.pop(j)
        player2.pop(j)
    player1.extend(tempplayer1)
    player2.extend(tempplayer2)
    if len(player1)<len(player2):
        halfDeck = len(player1)
    else:
        halfDeck = len(player2)


#     if plyr1>plyr2:
#         print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
#     else:
#         print("Player two won the game "+str(plyr2)+" to "+str(plyr1))

# playgame()

#after a single round have the cards won all given to the winner
#