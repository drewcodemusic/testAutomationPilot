import unittest
import sys
import os

# Simple function to test
def add_numbers(a, b):
    """
    Simple function to add two numbers
    
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

# Performance test function (can be expanded)
def performance_test():
    """
    Simulate a performance test
    Checks if adding 1 million numbers takes less than a second
    """
    import time
    
    start_time = time.time()
    total = sum(range(1_000_000))
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Performance Test: Total time to sum 1M numbers: {elapsed_time:.4f} seconds")
    
    # Fail if it takes more than 1 second
    assert elapsed_time < 1.0, f"Performance test failed. Took {elapsed_time} seconds"

# Unit test class
class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        self.assertEqual(add_numbers(3, 5), 8)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        self.assertEqual(add_numbers(-3, -5), -8)
    
    def test_add_mixed_numbers(self):
        """Test adding a positive and negative number"""
        self.assertEqual(add_numbers(3, -5), -2)

# Additional error handling test
def test_error_handling():
    """
    Demonstrate error handling in tests
    """
    try:
        # Intentional type error
        add_numbers("not", "number")
    except TypeError:
        print("Error handling test passed")
    else:
        raise AssertionError("Error handling test failed")

# Main execution
if __name__ == '__main__':
    # Run unit tests
    unittest.main(argv=[''], exit=False)
    
    # Run performance test
    performance_test()
    
    # Run error handling test
    test_error_handling()
    
    print("All tests completed successfully!")