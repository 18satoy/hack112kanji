from colorSheet import *

class dialogue(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        x, y, width, height = self.x, self.y, self.width, self.height
        pygame.draw.rect(screen, (0, 0, 0), (x - width / 2, y - height / 2, 
            x + width / 2, y + height / 2))