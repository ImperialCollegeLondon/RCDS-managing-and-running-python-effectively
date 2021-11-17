import matplotlib.pyplot as plt
import numpy as np

# Plots a figure showing the sum of all described sin functions
def sin_plotter(sin_descriptions):
    # Create the array of x values the sin value will be output at
    x = np.arange(0, 100, 0.01)
    # Create an initially empty array to hold the sum of the sin function at the corresponding values of x
    y = np.zeros(len(x))

    for sin_description in sin_descriptions:
        amplitude = sin_description[0]
        wavelength = sin_description[1]
        phase = sin_description[2]
        # Calculate the values of the current sin function as a function of x and add it to the running total of y
        y += amplitude * np.sin((x * np.pi * 2 + phase) / wavelength)

    # Plot y as a function of x
    plt.plot(x,y)

    # Set the x and y axes
    plt.xlabel("X (radians)")
    plt.ylabel("Y")

    # Show the graph
    plt.show()