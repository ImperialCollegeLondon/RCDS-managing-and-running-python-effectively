# A function which returns the result of a quadratic expression
def quadratic(a, b, c, x):
    # Raise an AssertionError if x is negative. Allows us to check x is zero or greater. Disabled if the -O flag is used
    assert(x >= 0)

    # Calculate the expression and return it
    return a * x ** 2 + b * x + c