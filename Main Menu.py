#Julian Meyer
#3/23/2022

#Main Menu for the game creating functions for menu


import pygame, time
pygame.init()
#Variables
WIDTH=700
HEIGHT=700
xs=50
ys=320
wb=30
hb=30

#list for messages
MenuList=['Instructions', 'Settings', 'sfsmksdk', 'sdlkldslks', 'jsdfkdskf;', 'dsflksdlkk']

#Get Colors
colors= {'white':[255,255,255],'red':[255,0,0],'blueish':[102, 153, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}
background = colors.get('white')
randColor=''
sq_color = colors.get('pink')

wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Eats Square")
#creat different type
# MENU2_FNT=pygame.font.SysFont('comicsans', 70)
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
# MENU_FNT=pygame.font.SysFont('comicsans', 80)
INST_FNT=pygame.font.SysFont('comicsans', 80)
# RETURN_FNT=pygame.font.SysFont('comicsans', 80)
# SETTINGS_FNT=pygame.font.SysFont('comicsans', 80)
wind.fill((255,255,255))

text=TITLE_FNT.render("MENU", 1, (0,255,0))
wind.fill((255,255,255))
#get the width of the text 
#x value = WIDTH/2 - wText/2
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(xt,50))

#Creat First button


#Create Square for menu

square=pygame.Rect(xs,ys,wb,hb)
txty=243
for i in range(7):
    message=MenuList[i]
    text=INST_FNT.render(message,1,(255,0,0))
    wind.blit(text,(90,txty))
    pygame.draw.rect(wind,sq_color, square )
    square.y += 50
    txty+=50

pygame.display.update()
pygame.time.delay(10000)

# text=INST_FNT.render("Level Selection", 1, (255,0,0))
# wind.blit(text,(50,300))
# text=TITLE_FNT.render('Instructions', 1, (102,153,255))
# wind.blit(text,(90, 243))
# text=MENU_FNT.render('Game Credits', 1, (255,85,0))
# wind.blit(text,(50,100))
# text=SETTINGS_FNT.render('Settings', 1, (48,25,52))
# wind.blit(text,(50,400))
# text=RETURN_FNT.render('Click for Return', 1, (0,255,0))
# wind.blit(text,(50,500))


