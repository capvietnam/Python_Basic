from math import sqrt


class Cube:
    list_figures = list()

    def __init__(self, side: int | float) -> None:
        self.side = side
        for _ in range(6):
            self.list_figures.append(Square(side=side))

    def square(self) -> int | float:
        return pow(self.side, 3)

    def surface_area(self) -> int | float:
        return pow(self.side, 2) * 6

    def set_side(self, side: int | float) -> None:
        for number in range(6):
            self.list_figures.insert(number, Square(side=side))

    def get_list_figures(self) -> list:
        return self.list_figures


class Pyramid:
    list_figures = list()

    def __init__(self, footing: int | float, height: int | float) -> None:
        self.footing = footing
        self.height = height
        self.list_figures.append(Square(footing))
        for _ in range(4):
            self.list_figures.append(Triangle(footing=footing, height=height))

    def set_side(self, footing: int | float, height: int | float) -> None:
        self.list_figures.append(Square(footing))
        for number in range(4):
            self.list_figures.insert(number, Triangle(footing=footing, height=height))

    def get_list_figures(self) -> list:
        return self.list_figures

    def square(self) -> int | float:
        return pow(self.footing, 3)

    def surface_area(self) -> int | float:
        return pow(self.footing, 2) + 2 * self.footing * self.height


class Square:
    def __init__(self, side: int | float) -> None:
        self.side = side

    def square(self) -> int | float:
        return pow(self.side, 2)

    def perimeter(self) -> int | float:
        return self.side * 4

    def get_square(self):
        return self.side

    def __str__(self) -> str:
        return f'Квадрат со стороной: {self.side}'


class Triangle:

    def __init__(self, footing: int | float, height: int | float) -> None:
        self.footing = footing
        self.height = height
        self.lateral_face = sqrt(pow(height, 2) - pow(footing / 2, 2))

    def square(self) -> int | float:
        return self.footing * self.height / 2

    def perimeter(self) -> int | float:
        return self.lateral_face * 2 + self.footing

    def __str__(self) -> str:
        return f'Треугольник с высотой: {self.height}, основанием: {self.footing}'


pyramid = Pyramid(4, 4)
cube = Cube(4)

print(cube.surface_area())
print(pyramid.surface_area())
