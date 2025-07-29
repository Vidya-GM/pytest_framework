import pytest

#from src import shapes


# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(length=10, width=20)

# @pytest.fixture
# def standard_rectangle():
#     return shapes.Rectangle(length=50, width=100)


#  Without fixture define rectangle inside test function for every testcase
# def test_area():
#     rectangle = shapes.Rectangle(length=10, width=20)
#     assert rectangle.area() == rectangle.length*rectangle.width


# with fixture, need to provide my_rectangle as parameter to each test-function/testcase
def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(length=10, width=20)
    assert my_rectangle.perimeter() == (my_rectangle.length+my_rectangle.width)*2


def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(length=10, width=20)
    assert my_rectangle.area() == my_rectangle.length*my_rectangle.width


def test_not_equal(my_rectangle, standard_rectangle):
    assert my_rectangle != standard_rectangle
