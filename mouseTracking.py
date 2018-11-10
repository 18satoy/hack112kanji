#jiayizha
#Tutorial from GitHub: https://github.com/MiniGirlGeek/pygame-paintme

import pygame
from colorSheet import *
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption("Write Kanji!")
clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
window.fill(white)
mouse_pos = None
isDrawing = False
canvasSize = (500,500)

running = True
try:
    while running:
        time = clock.tick(500) #similar to timerDelay

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]<=500:
                isDrawing = True

            if event.type == pygame.KEYDOWN:
                if event.key == 114: #"r"
                    window.fill(white)

            if isDrawing:
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos == None:
                    mouse_pos = pygame.mouse.get_pos()

                if pygame.mouse.get_pressed()==(1,0,0):
                    mouse_pos2 = pygame.mouse.get_pos()
                    pygame.draw.line(window,darkMagenta,mouse_pos, mouse_pos2,10)
                    mouse_pos = mouse_pos2

                if pygame.mouse.get_pressed()==(0,0,0):
                    isDrawing = False
                    mouse_pos = None


        pygame.display.update()

    pygame.quit()
except SystemExit:
    pygame.quit()
