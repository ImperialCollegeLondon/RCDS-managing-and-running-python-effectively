import math

# This function calculates and returns the length of the hypotenuse of a right-angled triangle given the length of the other two sides
def hypotenuse(a, b):
    # A check to raise an exception if a or b is less than zero
    # This check currently contains an error
    if a < 0:
        raise ValueError("a and b must both be zero or greater")

    # Calculate and return the length of the hypotenuse
    return math.sqrt(a ** 2 + b ** 2)