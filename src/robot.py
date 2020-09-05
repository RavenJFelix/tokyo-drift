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
        print(size)
        self.position = position
        self.size = size
        self.canvas = canvas
        self.body_canvas_id = self.canvas.create_rectangle(0, 0, self.size.x,
                                                      self.size.y,
                                                      fill=self.color)
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
