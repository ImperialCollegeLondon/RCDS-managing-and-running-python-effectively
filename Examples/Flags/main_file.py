from quadratic import quadratic

# Call the quadratic function with a positive value of x which will be allowed by the assert statement
print(quadratic(1,2,3,4))

# Call the quadratic function with a negative value of x which will not be allowed by the assert statement, unless the -O flag is used
print(quadratic(1,2,3,-4))