#jiayizha
#Tutorial from GitHub: https://github.com/MiniGirlGeek/pygame-paintme

import pygame
from colorSheet import *
from pygame.locals import *
from dialogueBox import *
from sys import exit
from pygamegame import PygameGame
from dialogueBox import dialogue

class writeScreen(object):
    def __init__(self, width=300, height=200):
        self.width = width
        self.height = height

class drawWindow(PygameGame):
    def __init__(self, x=620, y=410, width=300, height=200):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.charaList = [hito, sora, ki, hana, kawa]
        self.mouse_pos = None
        self.isDrawing = False
        self.step = 0
        self.brushColor = darkMagenta

    def drawBox(self,screen):
        chara = self.charaList[self.step]
        chara.image = pygame.image.load(chara.path).convert()
        writing = pygame.Surface((370,200))
        writing.fill(white)
        writing.set_alpha(150) #transparency
        screen.blit(chara.image,(self.x+90,self.y))
        screen.blit(writing,(self.x,self.y))

    def redrawAll(self,screen):
        self.drawWindow.drawBox(screen)

    def mousePressed(self,x,y):
        print(x,y)
        if self.mouse_pos == None:
            self.isDrawing == True
'''
    def mouseMotion(self,x,y):

    def mouseDrag(self,x,y):
        mouse_pos2 = pygame.mouse.get_pos()
        pygame.draw.line(writing,self.brushColor,mouse_pos, mouse_pos2,10)
            mouse_pos = mouse_pos2

    def keyPressed(self,keyCode,modifier):
        print(keyCode)
        if keyCode == 114:
            writing.fill(white)
            chara.strokeDone = 0

    def write(self):
        if self.isDrawing:
            if 
        if chara.isDone():
            writing.fill(white)
            i+=1




#Set-up the writing layer
#writing = pygame.Surface((300,200))
#writing.fill(white)
#writing.set_alpha(150) #transparency

# class Brush(object):
#     def __init__(self,color=darkMagenta):
#         self.color = color

# brush = Brush()

# try:
#     while running:
#         time = clock.tick(500) #similar to timerDelay
if i < len(charaList):
    chara = charaList[i]
    chara.image = pygame.image.load(chara.path).convert()

if chara.isDone():
    writing.fill(white)
    i+=1

    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]<=500:
        isDrawing = True

    # if event.type == pygame.KEYDOWN:
    #     if event.key == 114: #"r"
    #         writing.fill(white)
    #         chara.strokeDone = 0

    if isDrawing:
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos == None:
            mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()==(1,0,0):
            mouse_pos2 = pygame.mouse.get_pos()
            pygame.draw.line(writing,brush.color,mouse_pos, mouse_pos2,10)
            mouse_pos = mouse_pos2

        if pygame.mouse.get_pressed()==(0,0,0):
            chara.strokeDone+=1
            isDrawing = False
            mouse_pos = None

window.blit(chara.image,(50,0))
window.blit(writing,(0,0))

#     pygame.quit()
# except SystemExit:
#     pygame.quit()
'''
