# Julian Meyer
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame

import os, sys, random, time, pygame, math, datetime
from turtle import screensize
from pygame.locals import *
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
QUIT=False
#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
InstructionsList=['You can use the up arrow or space bar','Dont let mario hit the blocks to get points','Your score will be shown on the screen','Click escape to exit the window in the game','Click the back arrow to go to the menu','Have fun!']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print("in instr")
    myFile=open('ClassStuff\CircleEatsSquare\instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()



    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        # temp[j]=stuff[i]
        #     j +=1
        # print(temp)
        # for i in range(N):
        #     text=INST_FNT.render(temp[i], 1, BLACK)
        #     screen.blit(text, (40,yi))
        #     pygame.display.update()
        #     pygame.time.delay(50)
        #     yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
def lev1():

    # Global Variables for the game
    FPS = 32
    SCREENWIDTH = 600
    SCREENHEIGHT = 700
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}

    # Images and sprites were all changed
    PLAYER = 'ClassStuff\Images\FinalGameimages\Mario Sprite (1).png'
    BACKGROUND = 'ClassStuff\Images\FinalGameimages\\bluebg.png'
    PIPE = 'ClassStuff\Images\FinalGameimages\gallery\sprites\pink pipe.png'
    # GAMEWIN=pygame.image.load("ClassStuff\Images\FinalGameimages\gallery\sprites\Gucci.png")
    def welcomeScreen():
        """
        Shows welcome images on the s
        creen
        """

        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2  )
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                    return  
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))      
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0#sw/5 playerx
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping

    # All sound has been removed from the game
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP or K_w):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True


            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes, ) # This function will return true if the player is crashed
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1  
                    print(f"Your score is {score}") 
            # if score == 300:
            #     SCREEN.blit (GAME_SPRITES['gamewin'] (0,0))
            #     pygame.display.update()



            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe






    if __name__ == "__main__":
        # This will be the main point from where our game will start
        pygame.init() # Initialize all pygame's modules
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird by JULIAN')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (10).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (1).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (2).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (3).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (4).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (5).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (6).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (7).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\Gucci.png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\message3.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\pink-block-1.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )
        GAME_SPRITES['gamewin'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\Gucci.png')


        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        mainGame() # This is the main game function 
def lev2():
    # Global Variables for the game
    FPS = 32
    #sw-289 sh-511
    SCREENWIDTH = 600
    SCREENHEIGHT = 700
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}

    # Images and sprites were all changed
    PLAYER = 'ClassStuff\Images\FinalGameimages\Mario Sprite (1).png'
    BACKGROUND = 'ClassStuff\Images\FinalGameimages\\bluebg.png'
    PIPE = 'ClassStuff\Images\FinalGameimages\gallery\sprites\pink pipe.png'
    def welcomeScreen():
        """
        Shows welcome images on the s
        creen
        """
        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2  )
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                    return  
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))      
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0#sw/5 playerx
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping

    # All sound has been removed from the game
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP or K_w):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True


            crashTest = isCollide(playerx-10, playery+5, upperPipes, lowerPipes, ) # This function will return true if the player is crashed
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    print(f"Your score is {score}") 


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])
    #Upper0 lower1
            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """#SH/3
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/4
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe






    if __name__ == "__main__":
        # This will be the main point from where our game will start
        pygame.init() # Initialize all pygame's modules
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird by JULIAN')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (10).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (1).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (2).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (3).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (4).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (5).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (6).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (7).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\message3.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\pink-block-1.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )


        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

        while True:
            welcomeScreen() # Shows welcome screen to the user until he presses a button
            mainGame() # This is the main game function 

    #sq_color=colors.get('navy')
    #Making a rand c f the square
    changeColor()
def lev3():
    # Global Variables for the game
    FPS = 32
    #sw-289 sh-511
    SCREENWIDTH = 600
    SCREENHEIGHT = 700
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}

    # Images and sprites were all changed
    PLAYER = 'ClassStuff\Images\FinalGameimages\Mario Sprite (1).png'
    BACKGROUND = 'ClassStuff\Images\FinalGameimages\\bluebg.png'
    PIPE = 'ClassStuff\Images\FinalGameimages\gallery\sprites\pink pipe.png'
    def welcomeScreen():
        """
        Shows welcome images on the s
        creen
        """
        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2  )
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                    return  
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))      
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0#sw/5 playerx
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping

    # All sound has been removed from the game
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP or K_w):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True


            crashTest = isCollide(playerx-10, playery+5, upperPipes, lowerPipes, ) # This function will return true if the player is crashed
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    print(f"Your score is {score}") 


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])
    #Upper0 lower1
            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """#SH/3
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/5
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe






    if __name__ == "__main__":
        # This will be the main point from where our game will start
        pygame.init() # Initialize all pygame's modules
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird by JULIAN')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (10).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (1).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (2).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (3).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (4).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (5).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (6).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (7).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
            pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1 (8).png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\message3.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\pink-block-1.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )

        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

        while True:
            welcomeScreen() # Shows welcome screen to the user until he presses a button
            mainGame() # This is the main game function 


#==============================================
#
#Beginning  main prram
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
xm=0 
ym=0
f_SEET=True
sc_size=False
set_first=True
c_first=True
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
# if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP or K_w):
#                     if playery > 0:
#                         playerVelY = playerFlapAccv
#                         playerFlapped = True
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        MainMenu(InstructionsList)
    if INST:
        if keys[pygame.K_LEFT]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        if keys[pygame.K_LEFT]:
            INST=False
            MAIN=True
            first=True
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[pygame.K_LEFT]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        lev1()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        lev2()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_III:
        screen.fill(background)
        lev3()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if QUIT:
        quit()
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[pygame.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)




os.system('cls')
pygame.quit()