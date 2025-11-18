# https://github.com/yuxuantao12/lab11-YT-LJ
# Partner 1: Yuxuan Tao
# Partner 2: Liam Jensen

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)
    

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 5, 0)

    
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), math.log(100, 10))
        self.assertEqual(logarithm(2, 8), 3)
    

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 999), 0)
    

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-20, 5), -4)


    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, -5)
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
