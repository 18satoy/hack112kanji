import pygame
import colorSheet

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

    def drawText(self, screen):
        