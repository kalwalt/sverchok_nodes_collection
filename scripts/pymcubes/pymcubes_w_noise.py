"""
in bounds s d=10 n=2
in size s d=1.0 n=2
in iso_val s d=8.0 n=2
in noise s d=[] n=0
out vertices v
out triangles s
"""


import numpy as np
import random
import sys
mcubes_path = r"/usr/local/lib/python3.5/dist-packages" #it depend on your OS but just paste the path where is scipy
if not mcubes_path in sys.path:
    sys.path.append(mcubes_path)    
import mcubes



# Create a data volume
b = complex(bounds)
X, Y, Z = np.mgrid[:size:b, :size:b, :size:b]
n = np.array(noise)
u = np.reshape(n, (bounds,bounds,bounds))
v = Z * u
# Extract the 0-isosurface
verts, tri = mcubes.marching_cubes(v, iso_val)

vertices, triangles = [verts.tolist()], [tri.tolist()]