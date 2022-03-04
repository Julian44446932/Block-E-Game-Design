import os, time
import pygame as p

#initialize pygame
p.init()
#define colors
white=[255,255,255]
red=[255,0,0]
mag=[255,0,255]
aqua=[51,153,255]
m=[47,192,229]


#create your window/screen
WIDTH=600
HEIGHT=700
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("My window")
screen.fill(white)
p.display.update()
p.time.delay(4000)
screen.fill(red)
p.display.update()
p.time.delay(4000)
screen.fill(mag)
#define a rectangle
#position
x=20
y=30
#w and h of rect
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
p.display.update()
square2=p.Rect(x+200, y+200, wbox, hbox)
run=True
while run:
    screen.fill(mag)
    p.display.update()
    for event in p.event.get():
        if event.type== p.QUIT:
            run =False
    square.x +=5
    square.y +=5
    p.draw.rect(screen,(white),square)
    p.draw.rect(screen,(red),square2)
 
    p.display.update()
