import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# sample data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# custom colors from low to high values
colors = ["blue", "green", "yellow", "red"]

# make the custom colormap
custom_cmap = LinearSegmentedColormap.from_list("mycmap", colors)

# plot the data with the custom colormap
plt.imshow(Z, cmap=custom_cmap, origin='lower')
plt.colorbar()
plt.title("Plot with Custom Colormap")
plt.show()
