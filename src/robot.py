import tkinter as tk
import vectorz as vec
import time as time


class Omniwheel:
    # Robot that can do stuff. Just ask.
    # Velocity is in pixels per second

    position = vec.Vec2d(100, 100)
    size = vec.Vec2d(100, 100)
    color = 'blue'
    velocity = vec.Vec2d(0, 0)

    def __init__(self, position, size, canvas):
        # It's fucking python, just use the kwargs reeee
        print(self.position)
        self.position = position
        self.size = size
        self.canvas = canvas
        self.body_canvas_id = self.canvas.create_rectangle(0, 0, self.size.x,
                                                      self.size.y,
                                                      fill=self.color)
        self.draw()
    '''
    def _generate_body_points(self):
        # Returns a list of points. Currently assuming a rectangle. Upper lefft
        # and lower right corners.
        x_offset = round(self.size.x / 2)
        y_offset = round(self.size.y / 2)
        # A bit more inefficient but more documentation. Consider comments
        # python is generally an interpreted language
        upper_left = vec.Vec2d(self.position.x - x_offset,
                               self.position.y + y_offset)

        lower_right = vec.Vec2d(self.position.x + x_offset,
                                self.position.y - y_offset)

        points = [upper_left, lower_right]

        return points
    '''
    def get_canvas_body_coords(self):
        return vec.Vec2d(self.position.x - self.size.x / 2.0,
                         self.position.y - self.size.y / 2.0)

    def draw(self):
        canvas_body_coords = self.get_canvas_body_coords()
        self.canvas.move(self.body_canvas_id,
                         canvas_body_coords.x,
                         canvas_body_coords.y)
        # Find a way for better documentation?
        # Probably just delegat from Robot Graphics

    def step(self):
        # What the robot performs each simulation step
        self.position += self.velocity

    def physics_step(self, delta):
        # Physics based actions requiring a delta. Delta will be in seconds.
        self.position += self.velocity.scale(delta)
        return None


class TwoOmniwheelBot:
    velocity = vec.Vec2d(0, 0)
    angular_velocity = 0
    wheel_size = vec.Vec2d(10, 10)

    def __init__(self, canvas, position=vec.Vec2d(0, 0), radius=10):
        self.canvas = canvas
        self.position = position
        self.radius = radius

        wheel1_position = self.position + vec.Vec2d(-radius, 0)
        wheel2_position = self.position + vec.Vec2d(radius, 0)
        print(wheel1_position)
        print(wheel2_position)

        wheel1 = Omniwheel(wheel1_position, self.wheel_size, canvas)
        wheel2 = Omniwheel(wheel2_position, self.wheel_size, canvas)

        self.omniwheels = [wheel1, wheel2]

    def draw(self):
        for wheel in self.omniwheels:
            wheel.draw()
