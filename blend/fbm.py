from mathutils import noise, Vector

def sv_main( verts=[], h_factor=1.0, lacunarity=1.0, octaves=3 ):

    data = []

    in_sockets = [
        ['v','Vector', [verts]],
        ['s', 'H Factor ', h_factor],
        ['s', 'Lacunarity', lacunarity],
        ['s', 'octaves', octaves],
       ]

    out_sockets = [
    ['s', 'Float Data', data],
    ]
    print(range(len(verts)))
    
    for x in range(len(verts)):
        for y in range(len(verts)):
            for z in range(len(verts)):
                 
                 out = noise.fractal( Vector((verts[x][0][0],verts[0][y][0],verts[0][0][z])), h_factor, lacunarity, octaves )
                 data.append(out)
                 print("Float data: " + str(data))
                 
    return in_sockets, out_sockets
