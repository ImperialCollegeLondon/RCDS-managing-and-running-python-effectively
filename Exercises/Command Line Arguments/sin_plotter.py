import matplotlib.pyplot as plt
import numpy as np

def sin_plotter(sin_descriptions):
    x = np.arange(0, 100, 0.01)
    y = np.zeros(len(x))

    for sin_description in sin_descriptions:
        amplitude = sin_description[0]
        wavelength = sin_description[1]
        phase = sin_description[2]
        y += amplitude * np.sin((x * np.pi * 2 + phase) / wavelength)

    plt.plot(x,y)

    plt.xlabel("X (radians)")
    plt.ylabel("Y")

    plt.show()