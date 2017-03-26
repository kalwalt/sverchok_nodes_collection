"""
in int_X s d=2 n=1
in int_Y s d=2 n=1
in StepX s d=1.0 n=1
in StepY s d=1.0 n=1
in freq s d=1.0 n=1
in amp s d=1.0 n=1
in H s d=0.1 n=1
in lacunarity s d=0.4 n=1
in octaves s d=1 n=1
in offset s d=0.5 n=1
in gain s d=0.34 n=1
in noise_type s d=0 n=1
in fractal_type s d=0 n=2
in exp s d=1.0 n=1
out data s
out verts v
out poly s
inject
"""

from mathutils import Vector, noise
from sv_math_utils import make_plane, get_min, get_max, map_range
import numpy as np
import math as mt


def fractal_function(position, freq, amp, H, lacunarity, octaves, offset, gain, noise_basis, fractal_type):
        if fractal_type == 1:
            func = noise.fractal(position, H, lacunarity, octaves, noise_basis)
        elif fractal_type == 2:
            func = noise.multi_fractal(position, H, lacunarity, octaves, noise_basis)
        elif fractal_type == 3:
            func = noise.hetero_terrain(position, H, lacunarity, octaves, offset, noise_basis)
        elif fractal_type == 4:
            func = noise.hybrid_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis)
        elif fractal_type == 5:
            func = noise.ridged_multi_fractal(position, H, lacunarity, octaves, offset, gain, noise_basis)
        return func


data = []
params = vectorize(parameters)

# printings for testing purpose only
# print('params from inject', params)
# print('noise type: ',params[4])

exp = params[13]
print('ractal type: ', params[12])
params_f = params[4:13]
print(params_f)
params = params[0:4]

print('pow exp is: ', exp)

# print('new params: ', params)
plane_list = [make_plane(*param_set) for param_set in zip(*params)]
vertices = [[Vector((freq*vec[0], freq*vec[1], vec[2])) for vec in plane_list[0][0]]]
#print('vertices is: ',vertices[0][0])

data = [[fractal_function(vert, *param_set) for param_set in zip(*params_f)for vert in vertices[0]]]
max = get_max(data)
min = get_min(data)
map_data = [[map_range(d, min, max, 0.0, 1.0) for d in data[0]]]
# print('data max is: ', get_max(data))
# print('data is: ', map_data)
data = [[mt.pow(d, exp[0]) for d in map_data[0]]]
#print('data is: ', data)
#print(plane_list[0])

list = np.array(plane_list[0][0])
print('list shape: {0} \n'.format(list.shape))
print('numpy array list: ', list)

list = list[:, 0:2]
print('\n-------------\n')
print('list : ', list)

f_list = list.tolist()
print('\n-------------\n')
print('f_list is: ', f_list)

if data:
    for i, d in enumerate(data[0]):
        f_list[i].append(d)
print('\n-------------\n')
print('final output is: ', f_list)

verts = [[tuple(f) for f in f_list]]
poly = plane_list[0][1]
