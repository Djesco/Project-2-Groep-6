class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_same(self, v2):
        return self.x == v2.x and self.y == v2.y