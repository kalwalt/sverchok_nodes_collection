"""
in bounds s d=10 n=2
in iso_val s d=8.0 n=2
in samples s d=100 n=2
out vertices v
out triangles s
"""


import numpy as np
import sys
mcubes_path = r"/usr/local/lib/python3.5/dist-packages" #it depend on your OS but just paste the path where is scipy
if not mcubes_path in sys.path:
    sys.path.append(mcubes_path)    
import mcubes
import math

# Create the volume
def f(x, y, z):
    return math.cos(x) + math.cos(y) + math.cos(z)


# Extract the 16-isosurface
verts, tri = mcubes.marching_cubes_func(
        (-bounds, -bounds, -bounds), (bounds, bounds, bounds),  # Bounds
        samples, samples, samples,              # Number of samples in each dimension
        f,                          # Implicit function
        iso_val)                         # Isosurface value

vertices, triangles = verts.tolist(), tri.tolist()
