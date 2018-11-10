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

# class myProject(PygameGame):
#     def init(self):
#         self.message = "world helo"

#     def mousePressed(self, x, y):
#         print(x)

#     def redrawAll(self, screen):
#         pygame.draw.rect(screen, (0,45, 200), (0, 0, self.width, self.height)) 

game = drawDialogue(1000, 620)
game.run()