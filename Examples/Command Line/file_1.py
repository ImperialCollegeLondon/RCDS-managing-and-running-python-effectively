# Print the name associated with this file
print("Name of file_1: " + __name__)

if __name__ == "__main__":
    # This section will only be reached if this file was run from the command line directly
    print("File 1 inside if")

# This code will always be run - either if this file is run directly, or if it's imported from a different file
a = 1

# Try inserting some breakpoints in this loop and then step through the loop see how the values of variables changes
for i in range(3):
    b = 1 + a

    a = b + 2

print(a)

# Whether this file is run directly or imported from another file, code in functions will only be run if the function is called
# The code below only defines the function
def sample_print():
    print("Hello")