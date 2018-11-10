import pygame

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

    def keyPressed(self, keyCode, modifier):
        code = pygame.key.name(keyCode)
        if code == "space":
            self.gamePosition += 1
            print(self.gamePosition)
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
        print(self.drawWindow.isDrawing)
        if 620<=x<=1000 and 410<=y<=620:
            print(x,y)
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
            print(self.strokeDone)
            self.drawWindow.isDrawing = False
            self.drawWindow.mouse_pos = None
            if self.strokeDone == self.drawWindow.charaList[self.drawWindow.step].stroke:
                self.charaDone = True

                
    def redrawAll(self, screen):
        self.dialogue.drawBox(screen, self.dialogue.textImages, self.gamePosition)
        self.drawWindow.drawBox(screen)


game = drawDialogueBox(1000, 620)
game.run()
