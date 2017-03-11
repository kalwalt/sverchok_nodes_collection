import bpy
import sys
import string
import struct
import os  # glob
from os import path, name, sep
from math import *
from mathutils import noise
import bmesh
import time


def map_range(x_list, old_min, old_max, new_min, new_max):
    old_d = old_max - old_min
    new_d = new_max - new_min
    scale = new_d/old_d

    def f(x):
        return new_min + (x-old_min)*scale

        
    return min(new_max, max(new_min, f(x_list)))
        
def export_ter(filepath):
    start_time = time.process_time()
    filename = filepath + '.ter'
    
    '''
    obj = bpy.context.scene.objects.active
    mesh = obj.data
    new = bmesh.new()
    new.from_mesh(mesh)
    verts, edges, faces = pydata_from_bmesh(new)
    print(verts)
    print(len(verts))
    length_v = len(verts)
    size = sqrt(length_v)
    vertices = [int(v) for v in verts[0]]
    print(vertices)
    '''

    ter_header = 'TERRAGENTERRAIN '
    size_tag = 'SIZE'
    size_value = 64
    scal_tag = 'SCAL'
    scalx = 30.0
    scaly = 30.0
    scalz = 30.0
    xpoints_tag = 'XPTS'
    xpoints_value = 65
    xpoints = bytearray(xpoints_value)
    ypoints_tag = 'YPTS'
    ypoints_value = 65
    ypoints = bytearray(ypoints_value)
    altw_tag = 'ALTW'
    HeightScale = 80
    BaseHeight = 0
    totalpoints = xpoints_value * ypoints_value
    noise.seed_set(123)
    values = [int(map_range(noise.random(), 0.0, 1.0, 0.0, 32767.0)) for i in range(totalpoints)]
    #values = vertices
    #h_val = bytearray(values)
    print(values)
    eof_tag = 'EOF'  # end of file tag
    padding = b'\x00\x00'

    with open(filename, "wb") as file:
        file.write(ter_header.encode('ascii'))
        file.write(size_tag.encode('ascii'))
        # file.write(size)
        file.write(struct.pack('h', size_value))
        file.write(padding) # padding
        file.write(scal_tag.encode('ascii'))

        file.write(struct.pack('fff', scalx, scaly, scalz))

        '''
        file.write(xpoints_tag.encode('ascii'))
        # file.write(xpoints)
        file.write(struct.pack('h', xpoints_value))
        file.write(ypoints_tag.encode('ascii'))
        # file.write(ypoints)
        file.write(struct.pack('h', ypoints_value))
        '''
        
        file.write(altw_tag.encode('ascii'))
        file.write(struct.pack('h', HeightScale))
        file.write(struct.pack('h', BaseHeight))
        # file.write(h_val)
        for v in values:
            file.write(struct.pack('h', v))

        file.write(eof_tag.encode('ascii'))

        # newFile.close()
    print('Terrain exported in %.4f sec.' % (time.process_time() - start_time))

export_ter('/tmp/test_terrain')