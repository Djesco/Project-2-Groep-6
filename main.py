import pygame
import time
import random
 
pygame.init()
 
width = 1280
height = 720
 
black = (0,0,0)
white = (255,255,255)
red = (175, 0 ,0)
brigth_red = (255,0,0)
green = (0, 175, 0)
brigth_green = (0, 255, 0)
blue = (0, 0, 175)
brigth_blue = (0, 0, 255)
 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ontsnapperdam")
clock = pygame.time.Clock()
 
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def game_menu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() == (1, 0, 0)
        screen.fill(white)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        TitleText, TitleRect = text_objects("Ontsnapperdam", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        StartText, StartRect = text_objects("Start", midText, black)
        StartRect.center = ((width/2),(height/3))
        ExitText, ExitRect = text_objects("Afsluiten", midText, black)
        ExitRect.center = ((width/2),((height/3)*2))
        OptionsText, OptionsRect = text_objects("Opties", midText, black)
        OptionsRect.center= ((width/2),(height/2))
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
                print("meh")
        else:
            pygame.draw.rect(screen, blue, (((width/2) - 100), ((height/2) -25), 200, 50))        
        screen.blit(TitleText, TitleRect)
        screen.blit(StartText, StartRect)
        screen.blit(ExitText, ExitRect)
        screen.blit(OptionsText, OptionsRect)
        pygame.display.update()
        clock.tick(15)

def game_loop():
    while True:
        for event in events:
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                screen.fill(red)
                endText = basicfont.render('Game over!', True, white)
                endRect = endText.get_rect()
                endRect.topleft = (10, 10)
                displaysurf.blit(endText, endRect)
                pygame.display.flip()
                sleep(1)
                exit()

        screen.fill(black)

        game.draw(screen)

        pygame.display.flip()
game_menu()