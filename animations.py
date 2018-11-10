import pygame

from pygamegame import PygameGame
import mouseTracking
import dialogueBox

class drawDialogueBox(PygameGame):
    def init(self):
        self.margin = 10
        self.boxWidth = 600
        self.boxHeight = 200
        self.dialogue = dialogueBox.dialogue(self.margin, self.margin + self.boxHeight * 2,
            self.boxWidth, self.boxHeight)
        self.gamePosition = 0
        # self.mouseWindow = mouseTracking.window

    def keyPressed(self, keyCode, modifier):
        code = pygame.key.name(keyCode)
        if code == "right":
            self.gamePosition += 1

    def redrawAll(self, screen):
        self.dialogue.drawBox(screen, self.dialogue.textImages, self.gamePosition)
        # screen.blit(self.mouseWindow, (0, 0))

# class drawText(PygameGame):
#     def init(self, filePath):
#         self.


game = drawDialogueBox(1000, 620)
game.run()
