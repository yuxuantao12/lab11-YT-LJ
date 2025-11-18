# https://github.com/yuxuantao12/lab11-YT-LJ
# Partner 1: Yuxuan Tao
# Partner 2: Liam Jensen

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add():
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0


    def test_subtract():
        assert subtract(5, 2) == 3
        assert subtract(2, 5) == -3
        assert subtract(0, 0) == 0
    
    
    def test_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
            divide(0, 5)
    
    
    def test_logarithm():
        assert logarithm(10, 100) == math.log(100, 10)
        assert logarithm(2, 8) == 3
    
    
    def test_log_invalid_base():
        with pytest.raises(ValueError):
            logarithm(-2, 10)
        with pytest.raises(ValueError):
            logarithm(0, 10)
        with pytest.raises(ValueError):
            logarithm(1, 10)
    
    
    def test_multiply():
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 999) == 0
    
    
    def test_divide():
        assert divide(2, 10) == 5
        assert divide(5, -20) == -4
    
    
    def test_log_invalid_argument():
        with pytest.raises(ValueError):
            logarithm(10, -5)
        with pytest.raises(ValueError):
            logarithm(10, 0)
    
    
    def test_hypotenuse():
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(-3, 4) == 5

# Do not touch this
if __name__ == "__main__":
    unittest.main()
