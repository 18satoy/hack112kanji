import pygame
import colorSheet

<<<<<<< HEAD
pygame.init()
=======
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def getTextList(path):
    result = []
    resultNum = 0
    fullText = readFile(path)
    for line in fullText.splitlines():
        if line[0] == "#":
            continue
        else:
            start = line.find(")")
            if start != -1:
                resultNum += 1
                result.append([">>>" + line[start + 1:]])
            else:
                result[resultNum - 1].append(line)
    return result
>>>>>>> 858e10a3063326d84b418cbbc9f310c76fee4095

class dialogue(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = getTextList(dialogueText.txt)

    def drawBox(self, screen):
        x, y, width, height = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, colorSheet.darkGray, (x, y, width, height))

<<<<<<< HEAD

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
=======
    def drawText(self, screen):
        
>>>>>>> 858e10a3063326d84b418cbbc9f310c76fee4095
