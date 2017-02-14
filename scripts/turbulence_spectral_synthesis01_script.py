'''
turbulence script from texturing and modeling book ch.2 p.86, spectral syntesys approach.
Used only for testing pourpouse, trying to implement a turbulence function with rseed, because blender turbulence lack in this sense.
See the opensimplex version for the same implementation but with seed.
made by @kalwalt.
'''

from mathutils import Vector, noise

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
    
    
    def turbulence(vec,oct,freq,rseed):
        #we choose a noise type
        noise_type = noise.types.STDPERLIN
        #set the seed but won't work with blender noise
        noise.seed_set(rseed)
        sndata = []
        value = 0.0

        for o in range(oct):
           
            freq *= 2.0
            vVec = Vector(vec)
            multVec = vVec * freq
            #print(multVec)
            #print(f)
            value += abs(noise.noise(multVec,noise_type))/freq 
            #value += (noise.noise(multVec,noise_type))/f
            #value += amplitude*(noise.noise(multVec,noise_type))
            
        return value
        
    
    out = []
    
    
    if vec and vec[0]:
        for v in vec[0]:
            out = turbulence(v,octaves,frequency,rseed)
            data[0].append(out)
            #print(out)
            #print(len(data[0]))
            
    #print('data: {0}'.format(data))
    
    return in_sockets, out_sockets
