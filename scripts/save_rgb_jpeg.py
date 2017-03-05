import bpy
image_name = 'image-test.jpeg'
size = 4, 4
img = bpy.data.images.new(name= image_name,width=size[0],height=size[1],alpha=False,float_buffer=True)
print('blender image rgb pixel length: ',len(img.pixels))

pix=[]

pixels = [1.0] * (3 * size[0] * size[1])
print(pixels)
pixels = [None] * size[0] * size[1]
print(pixels)
for x in range(size[0]):
    for y in range(size[1]):
        # assign RGB to something useful
        r = x / size[0]
        g = y / size[1]
        b = (1 - r) * g

        pixels[(y * size[0]) + x] = [r, g, b]
print(pixels)
print('pixels length in cicle: ',len(pixels))

# flatten list
pixels = [chan for px in pixels for chan in px]
print('pixels (flattened) length : ',len(pixels))
print(pixels)
#img.file_format = 'JPEG'
img.pixels = pixels
data = img.pixels[:]
print('img.pixels: ', data)
print('length data: ', len(data))
#img.filepath_raw = '/tmp/' + image_name
#img.save()
scene=bpy.context.scene
scene.render.image_settings.file_format='JPEG'

img.save_render('/tmp/img_rgb.jpeg',scene)
print('saved!')