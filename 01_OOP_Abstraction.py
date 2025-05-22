from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, shapetype):
        self.shapetype = shapetype

    def get_shapetype(self):
        return self.shapetype

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__('Rectangle')
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


c1 = Circle(10)
print('Shape: ', c1.get_shapetype())
print('Area: ', c1.area())
print('Perimeter: ', c1.perimeter())


r1 = Rectangle(5, 10)
print('Shape: ', r1.get_shapetype())
print('Area: ', r1.area())
print('Perimeter: ', r1.perimeter())
