'''
in frame_current s d=0 n=2
in frame_start s d=0 n=2
in frame_end s d=4 n=2
in width s d=64 n=2
in height s d=64 n=2
in data s d=0.0 n=1
out some s
'''

import bpy
import numpy as np


def assign_BW_image(image, buffer):
    # from sverchok redux, modified version
    np_buff = np.empty(len(image.pixels), dtype=np.float32)
    np_buff.shape = (-1, 4)
    np_buff[:, :] = np.array(buffer)[:, np.newaxis]
    np_buff[:, 3] = 1
    np_buff.shape = -1
    image.pixels[:] = np_buff
    return image

image_name = 'circle' + '_'

if data:

    scene = bpy.context.scene
    scene.render.image_settings.file_format = 'PNG'
    path = '/tmp/' + image_name  + str(frame_current) + '.png'
    params = dict(name=image_name, width=width, height=height, alpha=False, float_buffer=True)
    img = bpy.data.images.new(**params)
    assign_BW_image(img, data)
    image = bpy.data.images[image_name]

    if img.has_data:
        #print('img-data : ', image.has_data)
        print('preparing')

        if frame_current <= frame_end: 
            print('frame is: {0}\n'.format(frame_current))
            
            #if img.has_data:
            if img.is_float:
                img.save_render(path, scene)
                if img.has_data:
                   img.save_render(path, scene)
                   print('saved!')
                

        if frame_current == frame_end:
            img.save_render(path, scene)
           
            print('stop')
            bpy.ops.screen.animation_play()
