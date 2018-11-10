import module_manager
module_manager.review()

from image_util import*
import pygame

class kanji (object):
    def __init__(self, width, height, imagePath):
        self.image = pygame.image.load(imagePath)
        self.image.convert()
        self.width = width
        self.height = height

    def draw(self, canvas):
    #drawing the box image in the correct position
        upperLeftX = 0
        upperLeftY = 0
        lowerRightX = self.width #width of large canvas
        lowerRightY = self.height #height of large canvas
        screen.blit(self.image, upperLeftX, upperLeftY, lowerRightX, lowerRightY)

class tree (kanji):
    def __init__(self, imagePath):
        super().__init__(image)

class flower (kanji):
    def __init__(self, imagePath):
        super().__init__(image)

class river (kanji):
    def __init__(self, imagePath):
        super().__init__(image)
