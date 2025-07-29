import pytest
from src import shapes


@pytest.mark.parametrize("side_length, expected_area", [(2,4),(5,25),(3,9),(10,100),(12, 144)])
def test_multiple_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(2,8),(5,20),(3,12),(10,40),(12,48)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
