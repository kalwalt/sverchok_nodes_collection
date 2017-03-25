import numpy as np
from sverchok.data_structure import fullList
from mathutils import Vector


# function (modified version) to map values, from Sverchok addon
def map_range(x_list, old_min, old_max, new_min, new_max):
    old_d = old_max - old_min
    new_d = new_max - new_min
    scale = new_d / old_d

    def f(x):
        return new_min + (x - old_min) * scale

    return min(new_max, max(new_min, f(x_list)))


def get_max(value):
    a = np.array(value[0])
    return np.amax(a)


def get_min(value):
    a = np.array(value[0])
    return np.amin(a)


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
