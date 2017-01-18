import pygame

#colors
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
brown = (110, 60, 19)
yellow = (255, 255, 0)
green = (0, 255, 0)


#lists
traversablelist = [(2, 0)]
line = [(16,0), (16,1), (16,2), (16,3), (16, 6), (16,7), (16,8), (16,9), (16,10), (16,11), (16,12), (16,13), (16,16), (16,19)]
landmarks = [(4,0), (8,2), (7,17), (11,8), (12,14), (14,19), (27,19), (29,16), (31,3), (25,4), (26,8), (21,0), (14,3), (23,15), (19,11), (16,11), (19,4), (29,11)]
policesquares = [(7,6), (10,15), (16,0), (20,17), (28,4), (19,10)]
arenas = [(5,19), (6,19), (7,19), (8,19), (9,19), (7,18), (10,11), (11,11), (12,11), (12,12), (15,13), (16,13), (15,14), (15,15), (15,16), (16,16), (10,2), (11,2), (11,3), (11,4), (11,5), (11,6), (10,6), (15,6), (16,6), (17,6), (18,6), (19,6), (20,6), (20,5), (15,5)]
kanskaarten = [(2,5), (2,16), (4,9), (7,7), (7,13), (7,19), (9,17), (10,2), (10,6), (12,0), (12,4), (12,13), (13,8), (15,0), (15,16), (16,8), (17,3), (18,13), (19,6), (20,19), (22,8), (23,6), (23,13), (26,0), (26,6), (26,11), (27,16), (31,1), (31,9), (31,16)]

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y

class Tile:
    def __init__(self, pos: Vector2, tail, traversable, type):
        self.pos = pos
        self.tail = tail
        self.type = type
        self.traversable = traversable
    def draw(self, screen, cSize, rSize):
        if self.traversable:
            pygame.draw.rect(screen, white, [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.type == "Line":
            pygame.draw.rect(screen, yellow, [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.type == "Kans":
            pygame.draw.rect(screen, green, [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.type == "Police":
            pygame.draw.rect(screen, blue, [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.type == "Arena":
            pygame.draw.rect(screen, red, [self.pos.x * cSize, self.pos.y * rSize, cSize -2, rSize - 2])
        if self.type == "Landmark":
            pygame.draw.rect(screen, brown, [self.pos.x * cSize, self.pos.y * rSize, cSize -2, rSize - 2])
        if self.tail is not None:
            self.tail.draw(screen, cSize, rSize)

class Game:

    def __init__(self, colloms, rows, width, height):
        self.colloms = colloms
        self.rows = rows
        self.width = width
        self.height = height
        self.board = self.board()

    def board(self):
        board = None
        for y in range(0,self.rows):
            for x in range(0, self.colloms):
                if (x, y) in policesquares:
                    board = Tile(Vector2(x, y), board, True, "Police")
                if (x, y) in arenas:
                    board = Tile(Vector2(x, y), board, True, "Arena")
                if (x, y) in line:
                    board = Tile(Vector2(x, y), board, True, "Line")
                if (x, y) in traversablelist:
                    board = Tile(Vector2(x, y), board, True, "Tile")
                if (x, y) in landmarks:
                    board = Tile(Vector2(x, y), board, True, "Landmark")
                if (x, y) in kanskaarten:
                    board = Tile(Vector2(x, y), board, True, "Kans")
                else:
                    board = Tile(Vector2(x, y), board, False, "Empty")
        return board

    def draw(self, screen):
        cSize = self.width // self.colloms
        rSize = self.height // self.rows

        self.board.draw(screen, cSize, rSize)
