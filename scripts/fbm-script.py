from mathutils import noise, Vector

def sv_main( verts=[], h_factor=1.0, lacunarity=1.0, octaves=3 ):

    data = []

    in_sockets = [
        ['v','Vector', verts],
        ['s', 'H Factor ', h_factor],
        ['s', 'Lacunarity', lacunarity],
        ['s', 'octaves', octaves]
    ]

    out_sockets = [
       ['s', 'Float Data', [data]]
    ]

    if verts and verts[0]:    
        for v in verts[0]:
             out = noise.fractal(v, h_factor, lacunarity, octaves )
             data.append(out)
                     
    return in_sockets, out_sockets
