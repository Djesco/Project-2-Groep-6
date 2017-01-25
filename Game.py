import pygame
import random
from pause_menu import Pause_menu #ook nieuw
from Board import *
from Player import *

class Game:
    def __init__(self, cols, rows, width, height, playeramount):
        self.columns = cols
        self.rows = rows
        self.width = width
        self.height = height
        self.playeramount = playeramount
        self.players = self.Createplayers(playeramount)
        self.board = self.Createboard()
        self.turn = 0
        self.cooldown = 0.5
        self.turnstart = True
        self.walk = 5000000

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def Createplayers(self, playeramount):
        playerlist = []
        for i in range(playeramount):
            x, y = starttile
            playerlist.append(Player(Vector2(x, y), colors.randomcolor()))
        return playerlist

    def Createboard(self):
        board = {}
        for y in range(self.rows):
            for x in range(self.columns):
                if x == 0:
                    board[x-1,y] = Nothing(Vector2(x,y))
                if y == 0:
                    board[x, y-1] = Nothing(Vector2(x, y))
                if x == self.columns -1:
                    board[self.columns, y] = Nothing(Vector2(x, y))
                if y == self.rows -1:
                    board[x, self.rows] = Nothing(Vector2(x, y))
                if (x, y) == (0,10):
                    board[x, y] = Starttile(Vector2(x, y))

                elif (x, y) in landmarks:
                    board[x,y] = Landmark(Vector2(x,y))
                elif (x, y) in kanskaarten:
                    board[x,y] = Kans(Vector2(x,y))
                elif (x, y) in policesquares:
                    board[x,y] = Police(Vector2(x,y))
                elif (x, y) in whitetiles:
                    board[x,y] = White(Vector2(x,y))
                else:
                    board[x,y] = Nothing(Vector2(x,y))
                if (x, y) in arenas:
                    board[x,y].setArena(True)
        return board

    def MoveDirection(self, key, player):
        if key[pygame.K_UP]:
            if self.gettile(player.pos.x, player.pos.y-1).isTraversable():
                self.players[self.turn].pos.y -= 1
                self.cooldown = 0.5
                self.walk -= 1
        elif key[pygame.K_DOWN]:
            if self.gettile(player.pos.x, player.pos.y + 1).isTraversable():
                self.players[self.turn].pos.y += 1
                self.cooldown = 0.5
                self.walk -= 1
        elif key[pygame.K_RIGHT]:
            if self.gettile(player.pos.x + 1 , player.pos.y).isTraversable():
                self.players[self.turn].pos.x += 1
                self.cooldown = 0.5
                self.walk -= 1
        elif key[pygame.K_LEFT]:
            if self.gettile(player.pos.x-1, player.pos.y).isTraversable():
                self.players[self.turn].pos.x -= 1
                self.cooldown = 0.5
                self.walk -= 1

    def changeturn(self):
        self.turn = (self.turn + 1) % self.playeramount


    def gettile(self, x, y):
        return self.board[x, y]

    def dice(self):
        print("Player {} turn".format(self.turn + 1))
        throw = random.randint(1, 6)
        self.walk = throw
        print("You threw " + str(throw))
        self.turnstart = False

    def update(self, screen, width, height, events, dt):
        self.player = self.players[self.turn]
        if self.turnstart:
            self.dice()

        if self.walk == 0:
            tile = self.gettile(self.player.pos.x, self.player.pos.y)
            if tile.kans:
                print("Kanskaart San")


            self.turnstart = True
            self.changeturn()

        keys = pygame.key.get_pressed()
        self.cooldown = self.cooldown - dt
        if self.cooldown < 0.0:
            self.MoveDirection(keys, self.player)

        self.draw(screen)
        # menu balk in game start
        red = (175, 0, 0)
        bright_red = (255, 0, 0)
        blue = (0, 0, 175)
        bright_blue = (0, 0, 255)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        mouse = pygame.mouse.get_pos()
        SkipText, SkipRect = self.text_objects("Menu", midText, white)
        SkipRect.center = ((width - 100), 25)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p = Pause_menu(self)
                    return p
        if width > mouse[0] > (width - 200) and 50 > mouse[1] > 0:
            pygame.draw.rect(screen, bright_red, ((width - 200), 0, 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    p = Pause_menu(self)
                    return p
        else:
            pygame.draw.rect(screen, red, ((width - 200), 0, 200, 50))
        screen.blit(SkipText, SkipRect)
        # menu balk in game eind
        pygame.display.update()
        return self

    def drawplayers(self, screen, cSize, rSize):
        for i in range(self.playeramount):
            if self.board[self.players[i].pos.x, self.players[i].pos.y].start:
                self.players[i].draw(screen, cSize, rSize, ((i -3) * rSize))
            elif self.players[i].is_in(lambda x: x.is_same(self.players[i].pos), self.players[i+1:]):
                self.players[i].draw(screen, cSize, rSize, ((self.playeramount - i) * (cSize//18)))
            else:
                self.players[i].draw(screen, cSize, rSize, 0)

    def drawboard(self, screen, cSize, rSize):
        for x in range(self.columns):
            for y in range(self.rows):
                self.board[x,y].draw(screen, cSize, rSize)
                self.board[x,y].drawarenas(screen, cSize, rSize)

        self.drawplayers(screen, cSize, rSize)
        self.board[starttile].drawprison(screen, cSize, rSize)

    def draw(self, screen):
        screen.fill(black)
        cSize = self.width // self.columns
        rSize = self.height // (self.rows + 2)
        self.drawboard(screen, cSize, rSize)