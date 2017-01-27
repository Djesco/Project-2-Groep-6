import pygame

class Policeline:
    def __init__(self):
        self.x = 0
        self.activated = False
        self.img = pygame.image.load('images/tiles/policecar.png')

    def draw(self, screen, cSize, rSize, columns):
        for x in range(self.x):
            for y in range(columns):
                screen.blit(pygame.transform.scale(self.img, (cSize - 2, rSize - 2)), (x * cSize, (y) * rSize))

    def move(self):
        self.x += 2

