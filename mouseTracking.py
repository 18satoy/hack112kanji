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
        self.charaList = [hito, ki, hana, sora, kawa]
        self.mouse_pos = None
        self.isDrawing = False
        self.step = 0
        self.brushColor = darkMagenta
        self.writing = pygame.Surface((370,200))
        self.writing.fill(white)

    def drawBox(self,screen):
        chara = self.charaList[self.step]
        chara.image = pygame.image.load(chara.path).convert()
        screen.blit(chara.image,(self.x+90,self.y))
        screen.blit(self.writing,(self.x,self.y))

    def fillColor(self):
        self.writing.fill(white)

    def transparent(self):
        self.writing.set_alpha(150) #transparency

    def redrawAll(self,screen):
        self.drawWindow.drawBox(screen)


