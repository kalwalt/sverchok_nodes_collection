"""
in verts v d=[[]] n=0
in edges s d=[[]] n=0
in faces s  d=[[]] n=0
in amount s d=[[]] n=0
out final_verts v
"""

import math
import numpy as np
from sverchok.data_structure import match_long_repeat
from sverchok.utils.sv_bmesh_utils import bmesh_from_pydata


def calc_mesh_normals(vertices, edges, faces):
    bm = bmesh_from_pydata(vertices, edges, faces, normal_update=True)
    vertex_normals = [v.normal[:] for v in bm.verts]
    bm.free()
    return vertex_normals


result_vertex_normals = []

meshes = match_long_repeat([verts, edges, faces])
for vertices, edges, f in zip(*meshes):
    vertex_normals = calc_mesh_normals(vertices, edges, f)
    result_vertex_normals.append(vertex_normals)

vertices = np.array(verts)
r_v_n = np.array(result_vertex_normals)
a = np.array(amount)

a.shape = int((r_v_n.size) / 3), 1
mul = r_v_n * a
add = vertices + mul
final_verts = add.tolist()
