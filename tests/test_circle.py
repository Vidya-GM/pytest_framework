import pytest
from src import shapes
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        # self.radius = shapes.Circle.radius = 10
        # self.circle = shapes.Circle(self.radius)
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_circle_area(self):
        assert self.circle.area() == math.pi*self.circle.radius**2

    def test_circle_perimeter(self):
        result = self.circle.perimeter()
        expected = self.circle.radius*2*math.pi
        assert result == expected

    def test_circle_rectangle_areanotequal(self, my_rectangle):
        # my_rectangle is difined globly, so available for all tests
        assert self.circle.area() != my_rectangle.area()

    def test_stdcircle_rectangle_areanotequal(self, standard_rectangle):
        assert self.circle.area() != standard_rectangle
