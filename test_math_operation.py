import pytest

def add_numbers(a, b):
    """Simple function to add two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Simple function to subtract two numbers."""
    return a - b

class TestMathOperations:
    def test_addition(self):
        """Test addition of positive numbers."""
        assert add_numbers(3, 5) == 8
        assert add_numbers(-1, 1) == 0
    
    def test_subtraction(self):
        """Test subtraction of numbers."""
        assert subtract_numbers(10, 4) == 6
        assert subtract_numbers(5, 7) == -2
    
    def test_division(self):
        """Test division with different scenarios."""
        assert 10 / 2 == 5
        with pytest.raises(ZeroDivisionError):
            1 / 0

def test_string_operations():
    """Demonstrate string-related test."""
    assert "Hello" + " World" == "Hello World"
    assert len("Python") == 6

# Parametrized test example
@pytest.mark.parametrize("input_a,input_b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_parametrized_addition(input_a, input_b, expected):
    """Parametrized test for addition."""
    assert add_numbers(input_a, input_b) == expected