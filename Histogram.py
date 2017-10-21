# Evan Douglass
# Histogram

# This program plots a basic frequency histogram for a given set of data

import math
import numpy as np
import matplotlib.pyplot as plt

# data for the histogram
DATA = [12, 4, 7, 2, 4, 2, 4]

# the number of classes
NUM_BINS = 12

# the class width
class_width = math.ceil(round(max(DATA) - min(DATA)) / NUM_BINS)

# create a list with the bin boundaries
lower_bound = min(DATA) - 0.5
bin_bounds = [lower_bound]
for bounds in range(NUM_BINS):
    bound = bin_bounds[-1]
    bound += (class_width)
    bin_bounds.append(bound)

# find midpoint of each class for x-axis ticks
first_midpoint = np.mean(bin_bounds[0:2])
x_mid = [first_midpoint]
for mid in range(NUM_BINS - 1):
    tick = x_mid[-1]
    tick += class_width
    x_mid.append(tick)

# set up the histogram
plt.hist(DATA, bins=bin_bounds, facecolor='blue', alpha=.5,
        edgecolor='black', align='mid')
plt.xlabel("Value")
plt.ylabel("Frequency")

# label x ticks as midpoints or as class boundaries
if True:
    plt.xticks(x_mid)       # midpoints
else:
    plt.xticks(bin_bounds)  # class boundaries

# display the histogram
plt.show()
