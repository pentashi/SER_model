import unittest

def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

class TestDivideFunction(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_with_remainder(10, 3), (3, 1))

    def test_divide_negative_numbers(self):
        self.assertEqual(divide_with_remainder(-10, 3), (-4, 2))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_with_remainder(10, 0)

if __name__ == '__main__':
    unittest.main()
