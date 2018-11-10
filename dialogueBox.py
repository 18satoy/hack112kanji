import pygame
import colorSheet

pygame.init()

class dialogue(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        x, y, width, height = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, colorSheet.darkGray, (x, y, width, height))


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

    #def self.checkpoint

hito = kanjiWriting("images/Kanji/charaHito.png", 2)
sora = kanjiWriting("images/Kanji/charaSora.png", 8)
ki = kanjiWriting("images/Kanji/charaKi.png", 4)
hana = kanjiWriting("images/Kanji/charaHana.png", 7)
kawa = kanjiWriting("images/Kanji/charaKawa.png", 3)
