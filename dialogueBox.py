import pygame
import colorSheet

class dialogue(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textImages = ["line1", "line2", "line3", "line4", "line5", "line6", "line7", "line8",
        "line9", "line10", "line11", "line12", "line13", "line14", "line15", 
        "line16", "line17", "line18", "line19", "line20"]
        # self.text = getTextList(dialogueText.txt)

    def loadImages(self):
        for textImage in self.textImages:
            textImage = pygame.image.load("textsFiles'\'" + str(image) + ".png")

    def drawBox(self, screen, textImages, num):
        x, y, width, height = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, colorSheet.darkGray, (x, y, width, height))
        image = pygame.image.load("textsFiles\\" + str(textImages[num])\
            + ".png")
        screen.blit(image, (x, y))

class kanjiWriting(object):
    def __init__(self, path, stroke):
        self.path = path
        self.image = None
        self.stroke = stroke
        self.strokeDone = 0

    def isDone(self):
        if self.strokeDone == self.stroke:
            return True

    def writing(self):
        self.strokeDone+=1


hito = kanjiWriting("images/Kanji/charaHito.png", 2)
sora = kanjiWriting("images/Kanji/charaSora.png", 8)
ki = kanjiWriting("images/Kanji/charaKi.png", 4)
hana = kanjiWriting("images/Kanji/charaHana.png", 7)
kawa = kanjiWriting("images/Kanji/charaKawa.png", 3)

