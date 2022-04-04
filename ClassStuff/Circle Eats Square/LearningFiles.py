# #JUlian Meyer
# Learning files
# A) open/create a file
#b) write 'w'
#c) append 'a'
#d) read 'r' 
# e) close()

import pygame,os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Jesse'
scoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y')
print(scoreLine)
#open a file and write in it
myFile=open('ClassStuff\sce.txt','r')
# myFile.write(scoreLine)

# myFile.close()
# score=345
# name='Jay'
# print(date.strftime('%m/%d/%Y'))
# scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y')
# myFile=open('ClassStuff\sce.txt','r')

# # myFile.write(scoreLine)
# myFile=open('ClassStuff\sce.txt','r')
lines=myFile.readline()
print(lines)
# lines=myFile.readlines()
# print(lines)
myFile.close()