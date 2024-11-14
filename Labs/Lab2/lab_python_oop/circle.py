import math
from .figure import Figure
from .color import Color

class Circle(Figure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Круг {} цвета с радиусом {} имеет площадь: {}".format(
            self.color.color, self.radius, self.area())
