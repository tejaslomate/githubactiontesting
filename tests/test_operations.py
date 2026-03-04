from src.math_operations import add, subtract, multiply

def add_test():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0   

def subtract_test():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
    assert subtract(10, 5) == 5

def multiply_test():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0        