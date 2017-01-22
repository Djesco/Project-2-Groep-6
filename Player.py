import pygame
class Player:
    def __init__(self, pos, img):
        self.pos = pos
        self.img = img
    def draw(self, screen, cSize, rSize, voffset):
        pygame.draw.circle(screen, self.img, [int(self.pos.x * cSize + cSize * 0.5 ),int((self.pos.y+2) * rSize + rSize * 0.5 ) + voffset], int(0.3 * cSize), 0)

    def is_in(self, f, list,):
        for i in range(len(list)):
            if f(list[i].pos):
                return True
        return False