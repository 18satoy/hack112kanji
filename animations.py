import pygame

from pygamegame import PygameGame
import dialogueBox

class drawDialogue(PygameGame):
    def init(self):
        self.margin = 10
        self.boxWidth = 600
        self.boxHeight = 200
        self.dialogue = dialogueBox.dialogue(self.margin, self.margin + self.boxHeight * 2,
            self.boxWidth, self.boxHeight)

    def redrawAll(self, screen):
        self.dialogue.draw(screen)

class drawText(PygameGame):
    def init(self, filePath):
        self.


game = drawDialogue(1000, 620)
game.run()