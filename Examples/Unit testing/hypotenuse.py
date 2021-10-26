import math

def hypotenuse(a, b):
    if a < 0 :
        raise ValueError("a and b must both be zero or greater")

    return math.sqrt(a ** 2 + b ** 2)