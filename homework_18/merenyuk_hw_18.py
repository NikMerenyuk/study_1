class Figure:

    def __init__(self, formula):
        self.formula = formula

    def get_totally_area(self):
        pass


class Rectangle(Figure):

    def __init__(self, formula):
        super(Rectangle, self).__init__(formula)

    def get_totally_area(self, a=None, b=None):
        return f'Площадь прямоугольника: {a * b}'


class Circle(Figure):

    def __init__(self, formula):
        super(Circle, self).__init__(formula)
        self.__pi = 3.14

    def get_totally_area(self, r=None):
        return f'Площадь круга: {self.__pi * (r ** 2)}'


class RectTriangle(Figure):

    def __init__(self, formula):
        super(RectTriangle, self).__init__(formula)

    def get_totally_area(self, a=None, b=None):
        return f'Площадь прямоугольного треугольника: {a * b // 2}'


class Trapeze(Figure):

    def __init__(self, formula):
        super(Trapeze, self).__init__(formula)

    def get_totally_area(self, a=None, b=None, h=None):
        return f'Площадь трапеции: {(a + b) * h // 2}'


rectangle = Rectangle(Figure)
print(rectangle.get_totally_area(2, 4))

circle = Circle(Figure)
print(circle.get_totally_area(4))

rect_triangle = RectTriangle(Figure)
print(rect_triangle.get_totally_area(2, 4))

trapeze = Trapeze(Figure)
print(trapeze.get_totally_area(2, 4, 5))
