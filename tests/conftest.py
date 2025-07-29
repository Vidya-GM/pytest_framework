# To use the defined rectangles globly

import pytest
from src import shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)

@pytest.fixture
def standard_rectangle():
    return shapes.Rectangle(length=50, width=100)