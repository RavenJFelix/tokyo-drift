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
    last_graphical_body_coords = vec.Vec2d(0, 0)

    def __init__(self, position, size, canvas):
        # It's fucking python, just use the kwargs reeee
        print(self.position)
        self.position = position
        self.size = size
        self.canvas = canvas
        self.body_canvas_id = self.canvas.create_rectangle(0, 0, self.size.x,
                                                      self.size.y,
                                                      fill=self.color)
        print(str(self.position) + "Hello")
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
    def calc_canvas_body_coords(center):
        return vec.Vec2d(center.x - center.x / 2.0,
                         center.y - center.y / 2.0)

    def draw(self):
        delta_motion = self.position + self.last_graphical_body_coords.inverse()
        # canvas_body_coords = self.get_canvas_body_coords()
        self.canvas.move(self.body_canvas_id,
                         delta_motion.x,
                         delta_motion.y)

        self.last_graphical_body_coords += delta_motion
        # Find a way for better documentation?
        # Probably just delegat from Robot Graphics

    def step(self):
        # What the robot performs each simulation step
        self.position += self.velocity

    def physics_step(self, delta):
        # Physics based actions requiring a delta. Delta will be in seconds.
        # print(self.position)
        self.position += self.velocity.scale(delta)
        return None


class TwoOmniwheelBot:
    velocity = vec.Vec2d(0, 0)
    tangential_velocity = 0
    wheel_size = vec.Vec2d(10, 10)

    def __init__(self, canvas, position=vec.Vec2d(0, 0), radius=10):
        self.canvas = canvas
        self.position = position
        self.radius = radius

        wheel1_position = self.position + vec.Vec2d(-radius, 0)
        wheel2_position = self.position + vec.Vec2d(radius, 0)

        wheel1 = Omniwheel(wheel1_position, self.wheel_size, self.canvas)
        wheel2 = Omniwheel(wheel2_position, self.wheel_size, self.canvas)

        self.omniwheels = []
        self.omniwheels.append(wheel1)
        self.omniwheels.append(wheel2)

    def draw(self):
        print("Wheelbot draw")
        for wheel in self.omniwheels:
            wheel.draw()

    def physics_step(self, delta):
        # Replace with for 
        wheel1 = self.omniwheels[0]
        wheel2 = self.omniwheels[1]

        wheel1_radius_vector = wheel1.position + self.position.inverse()
        wheel2_radius_vector = wheel2.position + self.position.inverse()
        # print(wheel2_radius_vector)

        wheel1_rot_vec = wheel1_radius_vector.get_counterclockwise_orthog_unit()
        wheel2_rot_vec = wheel2_radius_vector.get_counterclockwise_orthog_unit()

        # print(wheel1_rot_vec)
        wheel1_tang_vel = wheel1_rot_vec.scale(self.tangential_velocity)
        wheel2_tang_vel = wheel2_rot_vec.scale(self.tangential_velocity)
        # print(self.tangential_velocity)
        # print(wheel1_tang_vel)
        print(self.velocity)
        wheel1.velocity = wheel1_tang_vel + self.velocity
        wheel2.velocity = wheel2_tang_vel + self.velocity
        print(wheel1.position)

        self.position += self.velocity.scale(delta)

        for wheel in self.omniwheels:
            # print(wheel)
            wheel.physics_step(delta)






