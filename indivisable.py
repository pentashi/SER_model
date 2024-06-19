import unittest

def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor

class TestDivideByZero(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
