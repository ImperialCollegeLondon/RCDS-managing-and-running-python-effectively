import sys

# Print out the name of the file being run and the command line arguments
print(sys.argv)

# Set total to zero and accumulate the sum of the command line arguments in it
total = 0

# Loop over the command line arguments and add them to total
for value in sys.argv[1:]:
    total = total + int(value)

# Print the final value - the sum of all command line arguments
print(total)