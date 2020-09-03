import tkinter as tk
import vectorz as vec

class Robot:
    # Robot that can do stuff. Just ask.

    position = vec.Vec2d(100, 100)
    size = vec.Vec2d(100, 100)
    color = 'blue'
    graphics_proxy = None

    def __init__(self, position,
                 graphics_proxy):

        # It's fucking python, just use the kwargs reeee
        self.position = position
        self.graphics_handler = graphics_proxy

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

    def draw(self):

        body_points = self._generate_body_points()
        # Find a way for better documentation?
        self.graphics_proxy.canvas.create_rectangle(10, 10, 10, 10,
                                                    fill='white')
        self.graphics_proxy.canvas.create_rectangle(body_points[0].x,
                                                    body_points[0].y,
                                                    body_points[1].x,
                                                    body_points[1].y,
                                                    fill=self.color)
        self.graphics_proxy.canvas.pack()
        # Probably just delegat from Robot Graphics

