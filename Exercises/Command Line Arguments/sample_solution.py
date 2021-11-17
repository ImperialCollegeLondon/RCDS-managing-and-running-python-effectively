import sys
from sin_plotter import sin_plotter

# Each sin function requires 3 arguments to describe it
# Check that there are a multiple of 3 command line arguments and raise a ValueError if not
if (len(sys.argv) - 1) % 3 != 0:
    raise ValueError("Arguments need to be provided in triplets, but "+ str(len(sys.argv) - 1) + " arguments were provided")

# Calculate the number of sin functions
n_sins = (len(sys.argv) - 1) // 3

# Create the outer list to hold the descriptions of the sin functions
sin_descriptions = []

# Create the descriptions of the sin functions one by one
for i_sin in range(n_sins):
    # Find the amplitude, wavelength and phase of the sin function being constructed
    # The type conversion to float will produce an error if the command line argument cannot be converted to a float
    amplitude = float(sys.argv[i_sin * 3 + 1])
    wavelength = float(sys.argv[i_sin * 3 + 2])
    phase = float(sys.argv[i_sin * 3 + 3])

    # Create the list describing the current sin function and add it to the outer list
    sin_descriptions.append([amplitude, wavelength, phase])

# Call the function with the list containing the descriptions of all the sin functions
sin_plotter(sin_descriptions)