import pygame
import colorSheet

class dialogue(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textImages = ["line1.png", "line2.png", "line3.png", "line4.png", 
        "line5.png", "line6.png", "line7.png", "line8.png", "line9.png", 
        "line10.png", "line11.png", "line12.png", "line13.png", "line14.png", 
        "line15.png", "line16.png", "line17.png", "line18.png", "line19.png", 
        "line20.png"]
        # self.text = getTextList(dialogueText.txt)

    def drawBox(self, screen):
        x, y, width, height = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, colorSheet.darkGray, (x, y, width, height))
        screen.blit(screen, "line1.png", self.x, self.y)
    # def drawText(self, screen):
