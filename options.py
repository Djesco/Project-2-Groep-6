import pygame

class Options:
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(screen, width, height):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        screen.fill(white)
        TitleText, TitleRect = Options.text_objects("Opties", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        screen.blit(TitleText, TitleRect)
        pygame.display.update()

