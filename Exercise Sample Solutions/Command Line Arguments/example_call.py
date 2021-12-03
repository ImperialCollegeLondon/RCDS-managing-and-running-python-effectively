# Import the sin-plotter function and give an example of a call to it
from sin_plotter import sin_plotter
import math

# Create the list of lists which describes the sin functions whose sum is to be plotted
# The first has an amplitude of 1, a wavelength of 5 and a phase of 0
# The second has an amplitude of 1, a wavelength of 5 and a phase of pi/4
# The third has an amplitude of 2, a wavelength of 5 and a phase of pi/2
sin_descriptions_example = [[1, 4, 0], [1, 5, math.pi / 4], [2, 50, math.pi / 2]]

# Call the sin_plotter function and provide the list of lists to describe the sin functions to be plotted
sin_plotter(sin_descriptions_example)