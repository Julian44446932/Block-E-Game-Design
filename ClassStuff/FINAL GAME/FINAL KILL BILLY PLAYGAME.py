import os, random, time, pygame, math, datetime
from turtle import screensize
os.system('cls')
WIDTH=600
HEIGHT=700
bg1=pygame.transform.scale('ClassStuff\Images\FinalGameimages\Mario Background.png',(700, 600))
bg2=pygame.image.load('ClassStuff\Images\FinalGameimages\Mario Background.png')
win = pygame.display.set_mode((500,480))
def playgame():
    win.blit(bg1, (0,0))
    pygame.display.update()
    pygame.time.delay(10000)
playgame()