#MAria I SUarez
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
#K_SPACE FOR JUMP
#initialize pygame

import os, random, time, pygame
from pickle import FALSE, TRUE
os.system('cls')
TITLE_FONT=pygame.font.SysFont('comicsans',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)
#initialize pygame
pygame.init()
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#declare constants, variables, init, dictionaries
#suare size

check = True #for the while loop
move = 5 #5 pixels
#square variables
xs = 20
ys = 20
wbox = 30
hbox = 30
MAIN=TRUE
INST=FALSESETT=
#circle variables
radius = 15
xc = random.randint(15, WIDTH-radius)
yc = random.randint(15, HEIGHT-radius)
#square
square = pygame.Rect(xs, ys, wbox, hbox)
#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('cirlce eats square')
#define colors
colors= {'white':[255,255,255],'red':[255,0,0],'blueish':[102, 153, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}
background = colors.get('pink')
randColor=''
cr_color = colors.get('white')
sq_color = colors.get(randColor)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if randColor==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
    #Get colors
SelectSquare = pygame.Rect(xs,ys,wbox,hbox)
settingsList=['screen size', 'Background color', 'Font Size', 'Circle Color']
menuList=['INSTRUCTIONS',"SETTINGS","LEVEL 1","LEVEL 2", "LEVEL 3",'Scoreboard','Exit']
txty=156.5
for i in range(len(menuList)):
    message=menuList[i]
    ClickText=INSTRUCTION_FONT.render(message,1,(0,169,184))
    screen.blit(ClickText,(90,txty))
    pygame.draw.rect(screen,sq_color,SelectSquare)
    SelectSquare.y+=75
    txty+=75
changeColor()


settingsList=['screen size', 'Background color', 'Font Size', 'Circle Color']
menuList=['INSTRUCTIONS',"SETTINGS","LEVEL 1","LEVEL 2", "LEVEL 3",'Scoreboard','Exit']

MAX=10
jumpCount=MAX
JUMP=False
while check:
    # pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    screen.fill(background)
    MainMenu(menuList)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check = False

    keys = pygame.key.get_pressed()
    if case.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos= pygame.mouse.get_pos
        print(mouse_pos)
    if ((mouse_pos[0]>20 and mouse_pos[0]<60 and mouse_pos[1]>250 and mouse_pos[1]<29:))
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")


    if keys[pygame.K_a] and square.x >= move:
        square.x -= move #subtract 5 from the x value
    if keys[pygame.K_d] and square.x < WIDTH - (wbox+move):
        square.x += move 
    #Jumping part
    if not JUMP:
        if keys[pygame.K_w] and square.y >= move:
            square.y -= move
        if keys[pygame.K_s] and square.y < HEIGHT - hbox:
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP=True
    else:
        if jumpCount>=-MAX:
            square.y -= jumpCount*abs(jumpCount)/2
            jumpCount-=1
        else:
            jumpCount=MAX
            JUMP=False
    #finished circle
    if keys[pygame.K_LEFT] and xc >=(radius+move):
           xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (radius+move):
           xc += move
    if keys[pygame.K_UP] and yc >=radius+move:
           yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (radius+move):
           yc += move
    checkCollide = square.collidepoint((xc,yc))
    if checkCollide:
        square.x = random.randint(wbox, WIDTH-radius)
        square.y = random.randint(hbox, HEIGHT-radius)
        changeColor()
        radius+=move
    if radius > 200:
        quit()

      
    



    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    pygame.display.update()
    pygame.time.delay(10)

    