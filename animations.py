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
<<<<<<< HEAD
        self.drawWindow = mouseTracking.drawWindow()
        self.step = 0
        #self.

    def redrawAll(self, screen):
        self.dialogue.drawBox(screen)
        #screen.blit(self.mouseWindow, (0, 0))


=======
        self.gamePosition = 0
        # self.mouseWindow = mouseTracking.window

    def keyPressed(self, keyCode, modifier):
        code = pygame.key.name(keyCode)
        if code == "right":
            self.gamePosition += 1

    def redrawAll(self, screen):
        self.dialogue.drawBox(screen, self.dialogue.textImages, self.gamePosition)
        # screen.blit(self.mouseWindow, (0, 0))
>>>>>>> 7df3e67f8366f9854e0e736600b4a15ff326dbb6

# class drawText(PygameGame):
#     def init(self, filePath):
#         self.


game = drawDialogueBox(1000, 620)
game.run()
mouse.run()
