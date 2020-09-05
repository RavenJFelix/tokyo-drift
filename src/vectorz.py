class Vec2d:
    # Holds a 2 dimensional vector
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ')'

    def __add__(self, addend):
        x = self.x + addend.x
        y = self.y + addend.y
        return Vec2d(x, y)

    def scale(self, scale_factor):
        scaled_x = self.x * scale_factor
        scaled_y = self.y * scale_factor
        return Vec2d(scaled_x, scaled_y)

