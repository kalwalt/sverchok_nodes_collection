"""
in xdim s d=3 n=2
in ydim s d=3 n=2
in zdim s d=3 n=2
in size s d=1.0 n=2
out verts v
"""

import numpy as np

verts = []
hs = size/2
x_ = np.linspace(-hs, hs, xdim)
y_ = np.linspace(-hs, hs, ydim)
z_ = np.linspace(-hs, hs, zdim)
f = np.vstack(np.meshgrid(x_,y_,z_)).reshape(3,-1).T
f = f.tolist()
verts.append(f)