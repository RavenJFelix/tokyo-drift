import tkinter as tk
import vectorz as vec


class Robot:
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

    def draw(self):
        self.canvas.move(self.body_canvas_id, self.position.x, self.position.y)
        # Find a way for better documentation?
        # Probably just delegat from Robot Graphics

    def step(self):
        # What the robot performs each simulation step

    def physics_step(self, delta):
        # Physics based actions requiring a delta. Delta will be in seconds.
        
