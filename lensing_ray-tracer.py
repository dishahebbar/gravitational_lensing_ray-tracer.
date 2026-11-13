import numpy as np
import matplotlib.pyplot as plt

# input values
src_x = float(input("Source x position (in Einstein radii): "))
src_y = float(input("Source y position: "))
sigma = float(input("Source size: "))

# camera
axis = np.linspace(-2.5, 2.5, 600)
x, y = np.meshgrid(axis, axis)         # creating the grid

# Lens equation
r2 = x**2 + y**2 + 1e-12          # (avoids dividing by zero)
bx = x - x / r2
by = y - y / r2

# Source and image
brightness = np.exp(-((bx - src_x)**2 + (by - src_y)**2) / (2 * sigma**2))

plt.imshow(brightness, extent=[-2.5, 2.5, -2.5, 2.5], origin="lower", cmap="magma")
plt.plot(0, 0, "w+")              # lens position
plt.title(f"source at ({src_x}, {src_y}), size {sigma}")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("einstein_ring.png", dpi=150)
plt.show()
