'''
Copyright (C) 2017 Walter Perdan
info@kalwaltart.it

Created by WALTER PERDAN
with modified map_range function from Sverchok addon:
    https://github.com/nortikin/sverchok/nodes/number/map_range.py

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
"""
in data s d=0.0 n=1
in size s d=32 n=2
in BaseHeight s d=0 n=2
in HeightScale s d=20 n=2
out output s
"""

import bpy
import sys
import string
import struct
import os  # glob
from os import path, name, sep
from math import *
from mathutils import noise, Vector
import time


# function (modified version) to map values from Sverchok addon
def map_range(x_list, old_min, old_max, new_min, new_max):
    old_d = old_max - old_min
    new_d = new_max - new_min
    scale = new_d / old_d

    def f(x):
        return new_min + (x - old_min) * scale

    return min(new_max, max(new_min, f(x_list)))


# function to export a terrain with random values
# only for testing the correctness of the export process
def export_ter(filepath):
    start_time = time.process_time()
    filename = filepath + '.ter'
    # start to set all the tags and values needed for the .ter file
    ter_header = 'TERRAGENTERRAIN '
    size_tag = 'SIZE'
    scal_tag = 'SCAL'
    scalx = 30.0
    scaly = 30.0
    scalz = 30.0
    altw_tag = 'ALTW'
    # values are packed as short (i.e = integers max 32767) float data
    # should be in the range -1.0, 1.0 so we map them from 0.0 to 32767.0
    # and we convert them to int values
    # print('data is: ',data)
    values = [int(map_range(d, -1.0, 1.0, 0.0, 32767.0)) for d in data]
    # print(values)
    eof_tag = 'EOF'  # end of file tag

    with open(filename, "wb") as file:
        # write the header
        file.write(ter_header.encode('ascii'))
        # write the size of the terrain
        file.write(size_tag.encode('ascii'))
        file.write(struct.pack('h', int(size)))
        # padding byte needed after SIZE
        file.write(struct.pack('xx'))  # padding -> b'\x00\x00'
        # write the scale tag = SCAL
        file.write(scal_tag.encode('ascii'))
        # pack the scaling values as floats
        file.write(struct.pack('fff', scalx, scaly, scalz))
        # write the altitude ALTW tag
        file.write(altw_tag.encode('ascii'))
        # pack heightScale and baseHeight
        file.write(struct.pack('h', int(HeightScale)))
        file.write(struct.pack('h', int(BaseHeight)))
        # pack as shorts the elvetions values
        for v in values:
            file.write(struct.pack('h', v))
        # EOF = end of file
        file.write(eof_tag.encode('ascii'))
        file.close()

    print('Terrain exported in %.4f sec.' % (time.process_time() - start_time))


export_ter('/tmp/sv_test_terrain')
