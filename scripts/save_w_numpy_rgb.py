import numpy as np
import bpy

size= 4, 4
length_image = size[0] * size[1] * 3
image_name = 'test_rgba.png'
print('image total pixels: ',length_image)
img = bpy.data.images.new(name= image_name,width=size[0],height=size[1],alpha=False,float_buffer=True)
#pixels = np.empty(length_image, dtype=np.float32)
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
pixels = [chan for px in pixels for chan in px]
print('pixels (flattened) length : ',len(pixels))
rgb =np.array(pixels)
print(rgb)
print(np.shape(rgb))
res=rgb.reshape(size[0]*size[1],3)
print(res)
alpha=np.empty(48)
alpha.fill(1)
A=alpha.reshape(16,3)

print(A)
#rgba=rgba=np.concatenate((res,np.zeros((16,3))),axis=1)
rgba=rgba=np.concatenate((res,A),axis=1)
print(rgba)
final=rgba[:,0:4]
print(final)
img.pixels = final.flatten()
data = img.pixels[:]
print('img.pixels: ', data)
print('length data: ', len(data))
scene=bpy.context.scene
scene.render.image_settings.file_format='JPEG'
img.save_render('/tmp/img_rgb.jpeg',scene)
print('saved!')

#data = [ (r,g,b,) for pix in rgb
#rgba = np.concatenate((rgb, np.zeros((size[0], size[1], 1))), axis=1)
#print('rgba pixels: ', rgba)
'''
np_buff = np.empty(len(img.pixels), dtype=np.float32)
np_buff.shape = (-1, 4)
np_buff[:, :] = np.array(buf)[:, np.newaxis]
np_buff[:, 3] = 1
np_buff.shape = -1
img.pixels[:] = np_buff
'''