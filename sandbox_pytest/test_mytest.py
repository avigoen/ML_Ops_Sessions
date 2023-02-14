from mytest import square
import pytest

@pytest.fixture
def input_values():
    return 2

def test_square_gives_correct_value():
    out = square(2)
    assert out == 4

def test_square_gices_correct_value(input_values):
    out = square(input_values)
    assert out == 4