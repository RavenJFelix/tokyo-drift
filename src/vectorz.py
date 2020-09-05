import math as math


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

    def get_counterclockwise_orthog(self):
        return Vec2d(-self.y, self.x)

    def get_magnitude(self):
        # homebrew probably seek another library or put into a custom
        # math modue
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_unit(self):
        return self.scale(1.0/self.get_magnitude())

    def get_counterclockwise_orthog_unit(self):
        return self.get_counterclockwise_orthog().get_unit()




    def inverse(self):
        return Vec2d(-self.x, -self.y)






