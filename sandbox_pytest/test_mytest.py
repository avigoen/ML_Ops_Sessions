from mytest import square
import pytest

@pytest.fixture
def square_input():
    return 2

@pytest.fixture
def square_output():
    return 4

def test_square_gives_correct_value():
    out = square(2)
    assert out == 4

def test_square_gices_correct_value(square_input, square_output):
    out = square(square_input)
    assert out == square_output