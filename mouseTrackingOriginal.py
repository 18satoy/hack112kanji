#jiayizha
#Tutorial from GitHub: https://github.com/MiniGirlGeek/pygame-paintme

import pygame
from colorSheet import *
from pygame.locals import *
from dialogueBox import *
from sys import exit

pygame.init()
pygame.display.set_caption("Write Kanji!")
clock = pygame.time.Clock()
window = pygame.display.set_mode((300,200))
#Set-up the writing layer
writing = pygame.Surface((300,200))
writing.fill(white)
writing.set_alpha(150) #transparency

charaList = [hito, sora, ki, hana, kawa]

i = 0

mouse_pos = None
isDrawing = False
running = True

class Brush(object):
    def __init__(self,color=darkMagenta):
        self.color = color

brush = Brush()

try:
    while running:
        time = clock.tick(500) #similar to timerDelay
        if i < len(charaList):
            chara = charaList[i]
            chara.image = pygame.image.load(chara.path).convert()

        if chara.isDone():
            writing.fill(white)
            i+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]<=500:
                isDrawing = True

            if event.type == pygame.KEYDOWN:
                if event.key == 114: #"r"
                    writing.fill(white)
                    chara.strokeDone = 0

            if isDrawing:
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos == None:
                    mouse_pos = pygame.mouse.get_pos()

                if pygame.mouse.get_pressed()==(1,0,0):
                    mouse_pos2 = pygame.mouse.get_pos()
                    pygame.draw.line(writing,brush.color,mouse_pos, mouse_pos2,10)
                    mouse_pos = mouse_pos2

                if pygame.mousget_pressed()==(0,0,0):
                    chara.strokeDone+=1
                    isDrawing = False
                    mouse_pos = None

        pygame.display.update()
        window.blit(chara.image,(50,0))
        window.blit(writing,(0,0))

    pygame.quit()
except SystemExit:
    pygame.quit()
