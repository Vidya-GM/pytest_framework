# This file has different classes intended to write class based pytest in tests(dir)
import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other.length 

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)