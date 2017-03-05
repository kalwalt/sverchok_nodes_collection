import bpy
image_name = 'image-test.jpeg'
#img = bpy.data.images.new(name= image_name,width=4,height=4,alpha=False,float_buffer=True)
img = bpy.data.image.new(name= image_name,width=4,height=4,alpha=False,float_buffer=True)
pix=[]
for p in range(16):
    pix.append(p)
img.file_format = 'JPEG'
img.pixels = pix
img.filepath_raw = '/tmp/' + image_name

img.save_as({'area': imageEditorArea}, # emulate an imageEditor
    'INVOKE_DEFAULT', # invoke the operator
    copy=True, # make a copy of the image
    filepath=exportDir + image.name) # export it to this location
    
print('Saved!')