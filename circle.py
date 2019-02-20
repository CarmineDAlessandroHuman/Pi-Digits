from point import Point
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def is_in_the_circle(self, point:Point):
        distance = math.sqrt((point.x - self.radius)**2 + (point.y - self.radius)**2)

        if distance > self.radius:
            return False
        return True
