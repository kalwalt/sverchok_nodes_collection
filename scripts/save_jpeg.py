import bpy
image_name = 'image-test.jpeg'
size = 4, 4
img = bpy.data.images.new(name= image_name,width=size[0],height=size[1],alpha=False,float_buffer=True)


pix=[]

pixels = [1.0] * (4 * size[0] * size[1])
pixels = [None] * size[0] * size[1]
for x in range(size[0]):
    for y in range(size[1]):
        # assign RGBA to something useful
        r = x / size[0]
        g = y / size[1]
        b = (1 - r) * g
        a = 1.0

        pixels[(y * size[0]) + x] = [r, g, b, a]

# flatten list
pixels = [chan for px in pixels for chan in px]
#img.file_format = 'JPEG'
img.pixels = pixels
#img.filepath_raw = '/tmp/' + image_name
#img.save()
scene=bpy.context.scene
scene.render.image_settings.file_format='JPEG'

img.save_render('/tmp/img.jpeg',scene)
print('saved!')

