from mathutils import noise

def sv_main( verts=[], octaves=3, hard=1, noise_basis=1, amp=0.5, freq=2.0 ):

    data = []

    in_sockets = [
        ['v','Vector', verts],
        ['s', 'octaves', octaves],
        ['s', 'Hard ', hard],
        ['s', 'Noise Basis', noise_basis],
        ['s', 'Amplitude', amp],
        ['s', 'Frequency', freq]
        
    ]

    out_sockets = [
       ['s', 'Float Data', [data]]
    ]

    if verts and verts[0]:    
        for v in verts[0]:
             out = noise.turbulence(v, octaves, hard, noise_basis, amp, freq )
             data.append(out)
             print(data)
                     
    return in_sockets, out_sockets
