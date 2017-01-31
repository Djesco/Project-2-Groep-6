import pygame
import colors
import random
from Board import *
playercolors = [colors.red(), colors.blue(), colors.green(), colors.yellow(), colors.purple(), colors.orange()]
questpng = pygame.image.load('images/tiles/quest.png')
class Player:
    def __init__(self, pos, img, name):
        self.pos = pos
        self.img = img
        self.name = name
        self.quests = self.createquests(landmarks)
        self.playerturns = 0
        self.lastdirection = []

    def createquests(self, list):
        quests = []
        listnum = len(list)
        for i in range(3):
            n = random.randint(0, listnum - 1)
            q = list[n]
            quests.append(q)
            list.remove(q)
            listnum -= 1
        return quests

    def draw(self, screen, cSize, rSize, voffset):
        pygame.draw.circle(screen, self.img, [int(self.pos.x * cSize + cSize * 0.5 ),int((self.pos.y+2) * rSize + rSize * 0.5 ) + voffset], int(0.3 * cSize), 0)

    def drawquests(self, screen, cSize, rSize):
        for i in range(len(self.quests)):
            x, y = self.quests[i]
            screen.blit(pygame.transform.scale(questpng, (cSize, rSize)),(x * cSize, (y + 2) * rSize))
    def removequest(self, quest):
        self.quests.remove(quest)
    def is_in(self, f, list,):
        for i in range(len(list)):
            if f(list[i].pos):
                return True
        return False
