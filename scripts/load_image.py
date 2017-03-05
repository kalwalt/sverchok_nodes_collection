import bpy


def sv_main(i=0):
    
    in_sockets = [
        ['s', 'i', i]
    ]

    data = []
    float = []
    path = '/home/walter/Immagini/color_test.png'
    img = bpy.data.images.load(path, check_existing=False)

    data = img.pixels[:]
    if data and data[0]:
        for d in data:
            float.append(d)

    out_sockets = [
        ['s', 'float', [float]],
    ]

    return in_sockets, out_sockets
