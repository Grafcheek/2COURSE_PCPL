from .figure import Figure
from .color import Color

class Rectangle(Figure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Прямоугольник {} цвета с шириной {} и высотой {} имеет площадь: {}".format(
            self.color.color, self.width, self.height, self.area())
