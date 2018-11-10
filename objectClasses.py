import module_manager
module_manager.review()

from image_util import*

class kanji (object):
    def __init__(self, imagePath):
        self.image = pygame.image.load(imagePath)
        self.image.convert()

    def draw(self, canvas):
    #drawing the box image in the correct position
        upperLeftX = 0
        upperLeftY = 0
        lowerRightX = width         #width of large canvas
        lowerRightY = height - groundHeight     #height of large canvas
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
     
class player(kanji):
    def __init(self, x, y, imagePath):
        super().__init__(x, y, imagePath)
        self.speed = 10
    
    def move(self, x, y):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
             self.x -= self.speed
        elif keys[pygame.K_RIGHT]:
             self.x += self.speed
           
        win.fill((r,g,b)) #insert color of background
        pygame.display.update()
