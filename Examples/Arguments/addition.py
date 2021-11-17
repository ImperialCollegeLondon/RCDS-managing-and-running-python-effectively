import sys

# Print out the name of the file being run and the command line arguments
print(sys.argv)

# Set sum to zero and accumulate the sum of the command line arguments in it
sum = 0

# Loop over the command line arguments and add them to sum
for value in sys.argv[1:]:
    sum = sum + int(value)

# Print the final value - the sum of all command line arguments
print(sum)