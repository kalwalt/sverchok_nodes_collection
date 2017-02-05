import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings
#sys.path.append("/polyvox/lib")
import PolyVoxCore as pv

def sv_main(vol_region=32,sphere_radius=30):
    in_sockets = [
        ['s', 'Volume region', vol_region],
        ['s', 'Sphere radius', sphere_radius]
       ]

    #Create a volume of integers
    volume = vol_region - 1
    
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(volume,volume,volume))
    vol = pv.SimpleVolumeuint8(r)

    #Now fill the volume with our data (a sphere)
    v3dVolCenter = pv.Vector3Dint32_t(vol.getWidth() // 2, vol.getHeight() // 2, vol.getDepth() // 2)
    sphereRadius = sphere_radius
    #print(sphere_radius)
    voxels=[]
    #This three-level for loop iterates over every voxel in the volume
    for z in range(vol.getDepth()):
       for y in range(vol.getHeight()):
          for x in range(vol.getWidth()):
             #Compute how far the current position is from the center of the volume
             fDistToCenter = (pv.Vector3Dint32_t(x,y,z) - v3dVolCenter).length()

             #If the current voxel is less than 'radius' units from the center then we make it solid.
             if(fDistToCenter <= sphereRadius):
                #Our new voxel value
                uVoxelValue = 255
             else:
                uVoxelValue = 0

             #Append the voxel value into the voxels list
             #print(uVoxelValue)
             voxels.append(uVoxelValue)
             
    #print("voxels: {0}".format(voxels))         
    
    out_sockets = [
        ['s', 'Voxel_value', [voxels]]
    ]

    return in_sockets, out_sockets
