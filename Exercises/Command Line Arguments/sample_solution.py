import sys
from sin_plotter import sin_plotter

print(sys.argv)
print(len(sys.argv))

if (len(sys.argv) - 1) % 3 != 0:
    raise ValueError("Arguments need to be provided in triplets, but "+ str(len(sys.argv) - 1) + " arguments were provided")

n_sins = (len(sys.argv) - 1) // 3

sin_descriptions = []

for i_sin in range(n_sins):
    amplitude = float(sys.argv[i_sin * 3 + 1])
    wavelength = float(sys.argv[i_sin * 3 + 2])
    phase = float(sys.argv[i_sin * 3 + 3])

    sin_descriptions.append([amplitude, wavelength, phase])

sin_plotter(sin_descriptions)