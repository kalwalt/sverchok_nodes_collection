"""
in bounds s d=10 n=2
in iso_val s d=8.0 n=2
in samples s d=100 n=2
in r_i s d=5.0 n=2
in r_o s d=1.0 n=2
out vertices v
out triangles s
"""


import numpy as np
import sys
mcubes_path = r"/usr/local/lib/python3.5/dist-packages"  # it depend on your OS but just paste the path where is mcubes
if not mcubes_path in sys.path:
    sys.path.append(mcubes_path)
import mcubes
import math


# Create the volume
def f(x, y, z):
    # (sqrt(x*x+y*y)-3)^2+z*z-1
    res = (math.sqrt(x*x + y*y)-r_i)**2 + z*z - r_o
    return res


# Extract the 16-isosurface
verts, tri = mcubes.marching_cubes_func(
    (-bounds, -bounds, -bounds), (bounds, bounds, bounds),  # Bounds
    samples, samples, samples,            # Number of samples in each dimension
    f,                                    # Implicit function
    iso_val)                              # Isosurface value

vertices, triangles = [verts.tolist()], [tri.tolist()]
