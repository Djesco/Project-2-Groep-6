import pygame
from options import Options

class Main_menu:

    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(width, height, screen):
        black = (0,0,0)
        white = (255,255,255)
        red = (175, 0 ,0)
        brigth_red = (255,0,0)
        green = (0, 175, 0)
        brigth_green = (0, 255, 0)
        blue = (0, 0, 175)
        brigth_blue = (0, 0, 255)
        screen.fill(white)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        TitleText, TitleRect = Main_menu.text_objects("Ontsnapperdam", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        StartText, StartRect = Main_menu.text_objects("Start", midText, black)
        StartRect.center = ((width/2),(height/3))
        ExitText, ExitRect = Main_menu.text_objects("Afsluiten", midText, black)
        ExitRect.center = ((width/2),((height/3)*2))
        OptionsText, OptionsRect = Main_menu.text_objects("Opties", midText, black)
        OptionsRect.center= ((width/2),(height/2))   
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() == (1, 0, 0)
        clock = pygame.time.Clock()
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and ((height/3) + 25) > mouse[1] > ((height/3) - 25):
            pygame.draw.rect(screen, brigth_green, (((width/2) - 100), ((height/3) - 25), 200, 50))
            if click:
                print("yeay")
        else:
            pygame.draw.rect(screen, green, (((width/2) - 100), ((height/3) - 25), 200, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) -100) and (((height/3) * 2) + 25) > mouse[1] > (((height/3) * 2) - 25):
            pygame.draw.rect(screen, brigth_red, (((width/2) - 100), (((height/3) * 2) - 25), 200, 50))
            if click:
                exit()
        else:
            pygame.draw.rect(screen, red, (((width/2) - 100), (((height/3) * 2) - 25), 200, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) -100) and ((height/2) + 25) > mouse[1] > ((height/2) -25):
            pygame.draw.rect(screen, brigth_blue, (((width/2) - 100), ((height/2) -25), 200, 50))
            if click:
                return Options.update(screen, width, height)
        else:
            pygame.draw.rect(screen, blue, (((width/2) - 100), ((height/2) -25), 200, 50)) 
        screen.blit(TitleText, TitleRect)
        screen.blit(StartText, StartRect)
        screen.blit(ExitText, ExitRect)
        screen.blit(OptionsText, OptionsRect)        
        pygame.display.update()
        clock.tick(15)