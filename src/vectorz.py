class Vec2d:
    # Holds a 2 dimensional vector
    x = 0
    y = 0

    def __init__(self, x, y):
        self.y = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ')'
