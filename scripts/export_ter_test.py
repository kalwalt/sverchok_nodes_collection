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
    size = 64
    scal_tag = 'SCAL'
    scalx = 30.0
    scaly = 30.0
    scalz = 30.0
    altw_tag = 'ALTW'
    HeightScale = 80
    BaseHeight = 0
    totalpoints = (size + 1) * (size + 1)
    # set seed for noise.random()
    noise.seed_set(123)
    # values are packed as short (i.e = integers max 32767) so we map them in the right range
    values = [int(map_range(noise.random(), 0.0, 1.0, 0.0, 32767.0)) for i in range(totalpoints)]
    # print(values)
    eof_tag = 'EOF'  # end of file tag

    with open(filename, "wb") as file:
        # write the header
        file.write(ter_header.encode('ascii'))
        # write the size of the terrain
        file.write(size_tag.encode('ascii'))
        file.write(struct.pack('h', size))
        # padding byte needed after SIZE
        file.write(struct.pack('xx'))  # padding -> b'\x00\x00'
        # write the scale tag = SCAL
        file.write(scal_tag.encode('ascii'))
        # pack the scaling values as floats
        file.write(struct.pack('fff', scalx, scaly, scalz))
        # write the altitude ALTW tag
        file.write(altw_tag.encode('ascii'))
        # pack heightScale and baseHeight
        file.write(struct.pack('h', HeightScale))
        file.write(struct.pack('h', BaseHeight))
        # pack as shorts the elvetions values
        for v in values:
            file.write(struct.pack('h', v))
        # EOF = end of file
        file.write(eof_tag.encode('ascii'))
        file.close()

    print('Terrain exported in %.4f sec.' % (time.process_time() - start_time))


export_ter('/tmp/test_terrain')
