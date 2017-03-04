"""
in int_X s d=2 n=1
in int_Y s d=2 n=1
in StepX s d=1.0 n=1
in StepY s d=1.0 n=1
in H s d=0.1 n=1
in lacunarity s d=0.4 n=1
in octaves s d=1 n=1
in offset s d=0.5 n=1
in gain s d=0.34 n=1
in noise_type s d=0 n=1
in exp s d=1.0 n=1
out data s
out verts v
out poly s
inject
"""

from mathutils import Vector, noise
from sverchok.data_structure import fullList
import numpy as np
import math as mt


def make_plane(int_x, int_y, step_x, step_y, center=False):
    vertices = [(0.0, 0.0, 0.0)]
    vertices_S = []
    int_x = [int(int_x) if type(int_x) is not list else int(int_x[0])]
    int_y = [int(int_y) if type(int_y) is not list else int(int_y[0])]

    # center the grid: offset the starting point of the grid by half its size
    if center:
        Nnx = int_x[0] - 1  # number of steps based on the number of X vertices
        Nsx = len(step_x)  # number of steps given by the X step list

        Nny = int_y[0] - 1  # number of steps based on the number of Y vertices
        Nsy = len(step_y)  # number of steps given by the Y step list

        # grid size along X (step list & repeated last step if any)
        sizeX1 = sum(step_x[:min(Nnx, Nsx)])          # step list size
        sizeX2 = max(0, (Nnx - Nsx)) * step_x[Nsx - 1]  # repeated last step size
        sizeX = sizeX1 + sizeX2                       # total size

        # grid size along Y (step list & repeated last step if any)
        sizeY1 = sum(step_y[:min(Nny, Nsy)])          # step list size
        sizeY2 = max(0, (Nny - Nsy)) * step_y[Nsy - 1]  # repeated last step size
        sizeY = sizeY1 + sizeY2                       # total size

        # starting point of the grid offset by half its size in both directions
        vertices = [(-0.5 * sizeX, -0.5 * sizeY, 0.0)]

    if type(step_x) is not list:
        step_x = [step_x]
    if type(step_y) is not list:
        step_y = [step_y]
    fullList(step_x, int_x[0])
    fullList(step_y, int_y[0])

    for i in range(int_x[0] - 1):
        v = Vector(vertices[i]) + Vector((step_x[i], 0.0, 0.0))
        vertices.append(v[:])

    a = [int_y[0] - 1]
    for i in range(a[0]):
        out = []
        for j in range(int_x[0]):
            out.append(vertices[j + int_x[0] * i])
        for j in out:
            v = Vector(j) + Vector((0.0, step_y[i], 0.0))
            vertices.append(v[:])

    polygons = []
    for i in range(int_x[0] - 1):
        for j in range(int_y[0] - 1):
            polygons.append((int_x[0] * j + i, int_x[0]*j+i+1, int_x[0]*j+i+int_x[0]+1, int_x[0]*j+i+int_x[0]))

    return vertices, polygons


def fractal_function(position, H, lacunarity, octaves, offset, gain, noise_basis):
    return noise.ridged_multi_fractal(Vector(position), H, lacunarity, octaves, offset, gain, noise_basis)


data = []
params = vectorize(parameters)

# printings for testing purpose only
# print('params from inject', params)
# print('noise type: ',params[4])

exp = params[10]
params_f = params[4:10]
print(params_f)
params = params[0:4]

print('pow exp is: ', exp)

# print('new params: ', params)
plane_list = [make_plane(*param_set) for param_set in zip(*params)]
print(plane_list)
# vert=[]
data = [[fractal_function(vert, *param_set) for param_set in zip(*params_f)for vert in plane_list[0][0]]]
data = [[mt.pow(exp[0], d) for d in data[0]]]
print('data is: ', data)

# data = [[noise.ridged_multi_fractal(Vector(vert), H, lacunaarity, octaves, offset, gain, noise_type[0]) for vert in v_list[0]]]
print(plane_list[0])

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

verts = f_list
poly = plane_list[0][1]
