import pygame

class Player_select:
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(self, screen, width, height):
        white = (255, 255, 255)
        screen.fill(white)
        pygame.display.update()
        return self

#minimaal 3 spelers