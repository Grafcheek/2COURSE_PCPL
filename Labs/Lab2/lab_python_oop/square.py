from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "Квадрат {} цвета со стороной {} имеет площадь: {}".format(
            self.color.color, self.width, self.area())
