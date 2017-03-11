import bpy
import sys
import string
import struct
import os  # glob
from os import path, name, sep
from math import *
from mathutils import noise
import time


# function to map values
def map_range(x_list, old_min, old_max, new_min, new_max):
    old_d = old_max - old_min
    new_d = new_max - new_min
    scale = new_d/old_d

    def f(x):
        return new_min + (x-old_min)*scale

        
    return min(new_max, max(new_min, f(x_list)))

# function to export a terrain with random values
# only for testing the correctness of the export process      
def export_ter(filepath):
    start_time = time.process_time()
    filename = filepath + '.ter'
    
    ter_header = 'TERRAGENTERRAIN '
    size_tag = 'SIZE'
    size = 64
    scal_tag = 'SCAL'
    scalx = 30.0
    scaly = 30.0
    scalz = 30.0
    '''
    # we do not add xpoint and ypoints for the moment
    xpoints_tag = 'XPTS'
    xpoints_value = 65
    xpoints = bytearray(xpoints_value)
    ypoints_tag = 'YPTS'
    ypoints_value = 65
    ypoints = bytearray(ypoints_value)
    '''
    altw_tag = 'ALTW'
    HeightScale = 80
    BaseHeight = 0
    totalpoints = (size + 1) * (size + 1)
    noise.seed_set(123)
    # values are packed as short (i.e = integers max 32767) so we map them in the right range
    values = [int(map_range(noise.random(), 0.0, 1.0, 0.0, 32767.0)) for i in range(totalpoints)]
    #values = vertices
    #print(values)
    eof_tag = 'EOF'  # end of file tag
    padding = b'\x00\x00'

    with open(filename, "wb") as file:
        file.write(ter_header.encode('ascii'))
        file.write(size_tag.encode('ascii'))
        file.write(struct.pack('h', size))
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