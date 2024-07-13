import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def __str__(self):
        return super().__str__() + f", {self.r}"


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


#s = Shape(10,20)

c = Circle(10, 20, 15)
print(c)
print(c.area())

s = Square(10, 20, 30)
print(s.area())
