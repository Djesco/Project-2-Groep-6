import pygame
import colors
#colors
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
brown = (110, 60, 15)
yellow = (255, 255, 0)
green = (0, 255, 0)
black = (0,0,0)

kansimg = pygame.image.load('images/kans2.png')
arenaimg = pygame.image.load('images/arena.png')
jailimg = pygame.image.load('images/jail.png')
#lists
starttile = (0,10)
rotterdamc = [(2,8), (2,9), (2,10), (2,11)]
whitetiles = [(2,8), (2,9), (2,10), (2,11),(1, 10),(16,1), (16,2), (16,3), (16, 6), (16,7), (16,9), (16,10), (16,12), (16,13), (16,16), (16,19), (5,19), (6,19), (8,19), (9,19), (7,18), (10,11), (11,11), (12,11), (12,12), (15,13), (16,13), (15,14), (15,15), (16,16), (9,2), (10,3), (10,4), (10,5), (9,6), (14,6), (15,6), (16,6), (17,6), (18,6), (19,6), (19,5), (14,5), (28,6), (29,6), (30,6), (31,6), (31,7), (31,8), (27, 13), (27,14), (27,15), (28,16), (2,0), (2,1), (2,2), (2,3), (2,4), (2,6), (2,7), (2,12), (2,13), (2,14), (2,15), (2,17), (2,18), (2,19), (3,0), (3,10), (3,19), (4,10), (4,19),(5,0), (5,9), (6,0), (6,9), (7,0), (7,8), (7,9), (7,10), (7,11), (7,12), (7,14), (7,15), (8,0), (8, 1), (8,6), (8,11), (8,15), (8,17), (9,0), (9,11), (9,15), (9,16), (10,0), (10,7), (10,8), (10,19), (11,0), (11,15), (11,19), (12, 1), (12,1), (12, 2), (12, 3), (12,5), (12,6), (12,8), (12,15), (12,19), (13,0), (13, 3), (13,6), (13,7), (13,13), (13,19), (14,0), (14,13), (14,4), (15,3), (15,19), (17,0), (17,13), (17,16), (17,17), (17,19), (18,0), (18,3), (18,16), (18,19), (19,0), (19,3), (19,12), (19,13), (19,16), (19,19), (20,0), (20,6), (20,10), (20,13), (20,14), (20,15), (20,16), (21,6), (21,10), (21,17), (21,19), (22,0), (22,6), (22,7), (22,9), (22,17), (22,19), (23,0), (23,14), (23,16), (23,17), (23,19), (24,0), (24,4), (24,5), (24,6), (24,13), (24,19), (25,0), (25,13), (25,19), (26,4), (26,5), (26,7), (26,9), (26,10), (26,12), (26,13), (26,19), (27,0), (27,4), (27,11), (27,17), (27,18), (28,0), (28,5), (28,11), (29,0), (30,0), (30,11), (31,0), (31,2), (31,4), (31,5), (31,10), (31,11), (31,12), (31,13), (31,14), (31,15)]
line = [(16,0), (16,1), (16,2), (16,3), (16, 6), (16,7), (16,8), (16,9), (16,10), (16,11), (16,12), (16,13), (16,16), (16,19)]
landmarks = [(4,0), (8,2), (7,17), (11,8), (12,14), (14,19), (27,19), (29,16), (31,3), (25,4), (26,8), (21,0), (14,3), (23,15), (19,11), (16,11), (19,4), (29,11)]
policesquares = [(7,6), (10,15), (16,0), (20,17), (28,4), (19,10)]
arenas = [(5,19), (6,19), (7,19), (8,19), (9,19), (7,18), (10,11), (11,11), (12,11), (12,12), (15,13), (16,13), (15,14), (15,15), (15,16), (16,16), (9,2), (10,2), (10,3), (10,4), (10,5), (10,6), (9,6), (14,6), (15,6), (16,6), (17,6), (18,6), (19,6), (19,5), (14,5), (28,6), (29,6), (30,6), (31,6), (31,7), (31,8), (27, 13), (27,14), (27,15), (27,16), (28,16)]
kanskaarten = [(2,5), (2,16), (4,9), (7,7), (7,13), (7,19), (9,17), (10,2), (10,6), (12,0), (12,4), (12,13), (13,8), (15,0), (15,16), (16,8), (17,3), (18,13), (19,6), (20,19), (22,8), (23,6), (23,13), (26,0), (26,6), (26,11), (27,16), (31,1), (31,9), (31,16)]
powerups = [(16,2), (10,3), (17,6), (31, 8), (22,10), (10,11), (28,13), (18,17)]

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y

class Tile:
    def __init__(self, pos: Vector2, traversable):
        self.pos = pos
        self.traversable = traversable
        self.arena = False
        self.police = False
        self.kans = False
        self.landmark = False
        self.start = False
    def setArena(self, arena):
        self.arena = arena

    def isTraversable(self):
        return self.traversable

    def drawarenas(self, screen, cSize, rSize):
        if self.arena:
            screen.blit(pygame.transform.scale(arenaimg, (cSize - 2, rSize - 2)),(self.pos.x * cSize, (self.pos.y + 2) * rSize))
    def drawprison(self, screen, cSize, rSize):
        if self.start:
            screen.blit(pygame.transform.scale(jailimg, (cSize - 2, rSize * 6)),(self.pos.x * cSize, (self.pos.y - 1) * rSize))

class Starttile(Tile):
    def __init__(self, pos):
        super().__init__(pos, True)
        self.start = True
    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, colors.dark_grey(), [self.pos.x * cSize, (self.pos.y -1) * rSize, cSize - 2, rSize *6])


class Kans(Tile):
    def __init__(self, pos):
        super().__init__(pos, True)
        self.kans = True
    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, white, [self.pos.x * cSize, (self.pos.y + 2) * rSize, cSize - 2, rSize - 2])
        screen.blit(pygame.transform.scale(kansimg, (cSize - 2, rSize - 2)),(self.pos.x * cSize, (self.pos.y + 2) * rSize))

class Police(Tile):
    def __init__(self, pos):
        super().__init__(pos, True)
        self.police = True
    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, blue, [self.pos.x * cSize, (self.pos.y + 2) * rSize, cSize - 2, rSize - 2])

class Landmark(Tile):
    def __init__(self, pos):
        super().__init__(pos, True)
        self.landmark = True
    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, brown, [self.pos.x * cSize, (self.pos.y + 2) * rSize, cSize - 2, rSize - 2])

class White(Tile):
    def __init__(self, pos):
        super().__init__(pos, True)
    def draw(self, screen, cSize, rSize):
        pygame.draw.rect(screen, white, [self.pos.x * cSize, (self.pos.y + 2) * rSize, cSize - 2, rSize - 2])

class Nothing(Tile):
    def __init__(self, pos):
        super().__init__(pos, False)
    def draw(self, screen, cSize, rSize):
        return