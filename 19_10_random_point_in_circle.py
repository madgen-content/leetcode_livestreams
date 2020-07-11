from random import uniform, choice
from math import sqrt
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        

    def randPoint(self) -> List[float]:

        while True:
            x = uniform(-1,1)
            y = uniform(-1,1)
            
            if x * x + y * y <= 1:

                y *= self.radius
                x *= self.radius

                y += self.y_center
                x += self.x_center

                return [x,y]
