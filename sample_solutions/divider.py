# Import the sys module
import sys

# Check there were exactly two arguments provided on the command line
if len(sys.argv) != 3:
    raise ValueError(str(len(sys.argv) - 1) + " arguments were provided, but there should have been precisely 2 provided." )

# Try to convert the first argument to a float and give a custom error if it can't be
try:
    numerator = float(sys.argv[1])
except ValueError:
    raise ValueError("The first argument '" + sys.argv[1] + "' could not be converted to a float to be used as the numerator")

# Try to convert the second argument to a float and give a custom error if it can't be
try:
    denominator = float(sys.argv[2])
except ValueError:
    raise ValueError("The second argument '" + sys.argv[2] + "' could not be converted to a float to be used as the denominator")

# Print the final answer
print(numerator / denominator)