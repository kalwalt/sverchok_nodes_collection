"""
in size s d=400 n=2
in center_x s d=100 n=2
in center_y s d=100 n=2
in radius s d=100 n=2
out pixels s
"""

import numpy as np
import sys
scikit_path = r"/usr/local/lib/python3.5/dist-packages"  # it depend on your OS but just paste the path where is scikit
if not scikit_path in sys.path:
    sys.path.append(scikit_path)
from skimage.draw import circle


img = np.zeros((size, size), dtype=np.float32)
# fill circle
rr, cc = circle(center_x, center_y, radius, img.shape)

img[rr, cc] = 1.0

new_shape = size * size
out = np.reshape(img, (new_shape,))

pixels = [out.tolist()]
