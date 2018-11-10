import pygame

from pygamegame import PygameGame
import dialogueBox

class drawDialogue(PygameGame):
    def init(self):
        self.dialogue = dialogueBox.dialogue(100, 100, 20, 20)
        self.message = "hello"

    def redrawAll(self, screen):
        self.dialogue.draw(screen)

# class myProject(PygameGame):
#     def init(self):
#         self.message = "world helo"

#     def mousePressed(self, x, y):
#         print(x)

#     def redrawAll(self, screen):
#         pygame.draw.rect(screen, (0,45, 200), (0, 0, self.width, self.height)) 

game = drawDialogue(800, 500)
game.run()