
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
import os, random, time, pygame, math, datetime
os.system('cls')
name=input("What is yo name?")
#initialize pygame
pygame.init()


WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ('LEVEL II')
bg=pygame.image.load('C:\Users\meyerj24\OneDrive - Greenhill School\Desktop\Game Design\Block-E-Game-Design\ClassStuff\Images\download.jpg')
chart=pygame.image.load('C:\Users\meyerj24\OneDrive - Greenhill School\Desktop\Game Design\Block-E-Game-Design\ClassStuff\Images\Pygame-Tutorials-master\Game\standing.png')
screen.blit(bg,(0,0))
screen.blit(chart,(200,200))
pygame.display.update()
pygame.time.delay(3000)
