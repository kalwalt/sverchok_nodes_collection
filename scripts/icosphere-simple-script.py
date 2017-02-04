import bpy
import bmesh
from mathutils import Matrix
from sverchok.utils.sv_bmesh_utils import pydata_from_bmesh


def sv_main(subdiv=2,diam=4.0,mat = []):
    
    verts_out = []
    edges_out = []
    faces_out = []
    
    
    in_sockets = [
        ['s', 'subdivisions', subdiv],
        ['s', 'diam', diam],
        ['m','mat',mat]
        ]
       
    # Make a new BMesh
    bm = bmesh.new()
    
    print("matrices in: {0}".format(mat))
    matr = []
    #we want the matrices so we put them in a Blender Matrix()
    print("length of matrix is: {0}".format(len(mat)))
    if mat:
        
        
        for i,m in enumerate(mat):
            if mat[0]:
                matr = Matrix(m)
                print("matrices in for: {0}".format(m))
                print("Blender Matrix is: {0}".format(matr))
    else:
        matr = Matrix.Scale(1.0,1(1.0,1.0,1.0))
        print("Cocooo! we have not a plugged matrix")
                   
    bmesh.ops.create_icosphere(bm, subdivisions=subdiv, diameter=diam, matrix=matr, calc_uvs=False)
                
    #gets verts edges faces with sverchok function pydata_from_bmesh(bmesh)
    verts, edges, faces = pydata_from_bmesh(bm)
    verts_out.append(verts)
    edges_out.append(edges)
    faces_out.append(faces)
    
    #free the bmesh after computation
    #bm.free()
    
    out_sockets = [
        ['v', 'verts', verts_out],
        ['s', 'edges', edges_out],
        ['s', 'faces', faces_out]
    ]
    
    return in_sockets, out_sockets
