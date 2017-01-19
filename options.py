import pygame

class Options:
    def __init__(self):
        pass
    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(self, screen, width, height):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        screen.fill(white)
        TitleText, TitleRect = self.text_objects("Opties", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        screen.blit(TitleText, TitleRect)
        pygame.display.update()
        return self

