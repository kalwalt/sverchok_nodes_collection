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


print('frame is: {0}\n'.format(frame_current))

image_name = 'circle' + str(frame_current)
if data:
    img = bpy.data.images.new(name=image_name, width=width, height=height,
                              alpha=False, float_buffer=True)

    assign_BW_image(img, data)

    # path = '/tmp/' + image_name

    scene = bpy.context.scene
    scene.render.image_settings.file_format = 'PNG'
    image = bpy.data.images[image_name]
    if image.has_data:
        print('preparing')
        path = '/tmp/' + image_name + '_' + '.png'
        img.save_render(path, scene)
        if bpy.data.images[image_name].is_dirty:
            print('saved!')
        elif frame_current == 8:
            bpy.ops.screen.animation_play()

    elif frame_current == 8:
        bpy.ops.screen.animation_play()
