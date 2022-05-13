import random, sys, pygame # For generating random numbers # We will use sys.exit to exit the program
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}

# Images and sprites were all changed
PLAYER = 'ClassStuff\Images\FinalGameimages\Mario Sprite (1).png'
BACKGROUND = 'ClassStuff\Images\FinalGameimages\\bluebg.png'
PIPE = 'ClassStuff\Images\FinalGameimages\gallery\sprites\\neon-pink-color-solid-background-1920x1080.png'
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
                score +=20  
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
    offset = SCREENHEIGHT/2.5
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
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\0.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\1.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\2.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\3.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\4.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\5.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\6.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\\7.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\8.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\9.png').convert_alpha(),
        pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\Gucci.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\message3.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('ClassStuff\Images\FinalGameimages\\neon-pink-color-solid-background-1920x1080 (1).png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SPRITES['gamewin'] =pygame.image.load('ClassStuff\Images\FinalGameimages\gallery\sprites\Gucci.png')


    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        mainGame() # This is the main game function 