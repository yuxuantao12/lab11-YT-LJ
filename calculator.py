# https://github.com/yuxuantao12/lab11-YT-LJ
# Partner 1: Yuxuan Tao
# Partner 2: Liam Jensen

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a == 0).")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a ** b


def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        raise e


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e
