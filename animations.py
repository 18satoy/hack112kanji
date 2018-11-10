import pygame
import sys

from pygamegame import PygameGame
import mouseTracking
from mouseTracking import *
import dialogueBox

class drawDialogueBox(PygameGame):
    def init(self):
        self.margin = 10
        self.boxWidth = 600
        self.boxHeight = 200
        self.dialogue = dialogueBox.dialogue(self.margin, self.margin + self.boxHeight * 2,
            self.boxWidth, self.boxHeight)
        self.drawWindow = mouseTracking.drawWindow()
        self.gamePosition = 0
        self.strokeDone = 0
        self.charaDone = False
        self.bg = pygame.image.load('imageFinal.png')
        self.bgWidth, self.bgHeight = self.bg.get_rect().size
        self.viewWidth = self.bgWidth * 2
        self.stagePosX = 0
        self.startScrollX = 500
        self.walk = []
        for sprite in ['tile001.png', 'tile002.png', 'tile003.png', 'tile004.png', \
                        'tile005.png', 'tile006.png', 'tile007.png', 'tile008.png']:
            self.walk.append(pygame.image.load(sprite))
        self.playerWidth, self.playerHeight = self.walk[0].get_rect().size
        
        self.playerR = self.playerWidth // 2
        self.rPosX = self.playerR
        self.playerPosX = self.playerR
        self.playerPosY = 220 + (self.playerHeight // 2)
        self.speed = 0
        
        self.count = 0
        self.player = self.walk[self.count]
        

    def keyPressed(self, keyCode, modifier):
        code = pygame.key.name(keyCode)
        if code == "space":
            self.gamePosition += 1
            if self.gamePosition == 1:
                self.drawWindow.transparent()
            if self.gamePosition in [4,8,12,16] and self.charaDone==True:
                self.drawWindow.fillColor()
                self.strokeDone = 0
                self.drawWindow.step += 1
        if code == "r":
            self.drawWindow.fillColor()
            self.strokeDone = 0

            
    def mousePressed(self,x,y):
        if 620<=x<=1000 and 410<=y<=620:
            self.drawWindow.isDrawing = True
        if self.drawWindow.isDrawing == True and self.drawWindow.mouse_pos == None:
            self.drawWindow.mouse_pos = (x,y)

    def mouseDrag(self,x,y):
        if self.drawWindow.isDrawing == True:
            mouse_pos2 = (x,y)
            posX=self.drawWindow.mouse_pos[0]-620
            posY=self.drawWindow.mouse_pos[1]-410
            start=(posX,posY)
            posX2=mouse_pos2[0]-620
            posY2=mouse_pos2[1]-410
            end=(posX2,posY2)
            pygame.draw.line(self.drawWindow.writing, self.drawWindow.brushColor,
                start,end,10)
            self.drawWindow.mouse_pos = mouse_pos2

    def mouseReleased(self,x,y):
        if self.drawWindow.isDrawing == True:
            self.strokeDone+=1
            self.drawWindow.isDrawing = False
            self.drawWindow.mouse_pos = None
            if self.strokeDone == self.drawWindow.charaList[self.drawWindow.step].stroke:
                self.charaDone = True

                
    def redrawAll(self, screen):
        
        k = pygame.key.get_pressed()
        
        if k[K_RIGHT]:
            self.speed = 1
            self.player = self.walk[self.count]
            self.count += 1
            
            if self.count >= len(self.walk):
                self.count = 0
        
        else:
            self.speed = 0
        
        self.playerPosX += self.speed
        if self.playerPosX > self.viewWidth - self.playerR: 
            self.playerPosX = self.viewWidth - self.playerR
        if self.playerPosX < self.playerR: self.playerPosX = self.playerR
        if self.playerPosX < self.startScrollX: self.rPosX = self.playerPosX
        elif self.playerPosX > self.viewWidth - self.startScrollX: 
            self.rPosX = self.playerPosX - self.viewWidth + 1000
        else:
            self.rPosX = self.startScrollX
            self.stagePosX += -self.speed
            
        rel_x = self.stagePosX % self.bgWidth
        screen.blit(self.bg, (rel_x - self.bgWidth, 0))
        if rel_x < 1000:
            screen.blit(self.bg, (rel_x, 0))
        
        screen.blit(self.player, (self.playerPosX, self.playerPosY))
        
        self.dialogue.drawBox(screen, self.dialogue.textImages, self.gamePosition)
        self.drawWindow.drawBox(screen)
        


game = drawDialogueBox(1000, 620)
game.run()
