"""
in sp s d=0.0 n=2
in iso_val s d=0.0 n=2
in step s d=1 n=2
in a s d=6 n=2
in b s d=10 n=2
in c s d=16 n=2
out vertices v
out faces s
"""


import numpy as np
import sys
scikit_path = r"/usr/local/lib/python3.5/dist-packages" # it depend on your OS but just paste the path where is scikit
if not scikit_path in sys.path:
    sys.path.append(scikit_path)
from skimage import measure
from skimage.draw import ellipsoid


# Generate a level set about zero of two identical ellipsoids in 3D
ellip_base = ellipsoid(a, b, c, levelset=True)
ellip_double = np.concatenate((ellip_base[:-1, ...],
                               ellip_base[2:, ...]), axis=0)

# Use marching cubes to obtain the surface mesh of these ellipsoids
verts, faces, normals, values = measure.marching_cubes(
    ellip_double, level=iso_val,spacing=(sp, sp, sp), step_size=step)

vertices, faces = [verts.tolist()], [faces.tolist()]
