import pygame
traversablelist = [(9, 9), (4, 3), (2, 5), (6,5), (3,5), (29, 19), (15,10)]
policesquares = [(7,8), (3, 6)]
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
            pygame.draw.rect(screen, (255, 255, 255), [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
        if self.type == "Police":
            pygame.draw.rect(screen, (0, 0, 255), [self.pos.x * cSize, self.pos.y * rSize, cSize - 2, rSize - 2])
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
                if (x, y) in traversablelist:
                    board = Tile(Vector2(x, y), board, True, "Tile")
                else:
                    board = Tile(Vector2(x, y), board, False, "Empty")
        return board

    def draw(self, screen):
        cSize = self.width // self.colloms
        rSize = self.height // self.rows

        self.board.draw(screen, cSize, rSize)

