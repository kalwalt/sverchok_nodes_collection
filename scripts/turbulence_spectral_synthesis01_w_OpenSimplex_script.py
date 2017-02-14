'''
turbulence script from texturing and modeling book ch.2 p.86, spectral syntesys approach.
Used only for testing pourpouse, trying to implement a turbulence function with rseed, because blender turbulence lack in this sense.
See the opensimplex version for the same implementation but with seed.
made by @kalwalt.
'''
import sys
sys.path.append('/home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates')

from opensimplex import OpenSimplex
from mathutils import Vector

def sv_main(vec=[],octaves=1,amplitude=1.0,frequency=0.5,rseed=1):
    
    data = [[]]

    in_sockets = [
        ['v', 'vec', vec],
        ['s', 'octaves', octaves],
        ['s', 'amplitude', amplitude],
        ['s', 'frequency', frequency],
        ['s', 'Random seed', rseed]]

    out_sockets = [
        ['s', 'Float Data', data]
    ]
    
    osx= OpenSimplex(rseed)
    
    def turbulence(vec,oct,freq):
        
        value = 0.0
       
        for o in range(oct):
           
            freq *= 2.0
            vVec = Vector(vec)
            multVec = vVec * freq
            #print(multVec)
            #print(f)
            value += abs(osx.noise3d(multVec.x,multVec.y,multVec.z))/freq 
            #value += (noise.noise(multVec,noise_type))/f
            #value += amplitude*(noise.noise(multVec,noise_type))
            
        return value
        
    out = []
    append = data[0].append

    if vec and vec[0]:
        for v in vec[0]:
            append(turbulence(v,octaves,frequency))
            
    #print('data: {0}'.format(data))
    
    return in_sockets, out_sockets
