import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings

import PolyVoxCore as pv

def sv_main(vol_region=32,sphere_radius=30):
    in_sockets = [
        ['s', 'Volume region', vol_region],
        ['s', 'Sphere radius', sphere_radius]
       ]

    #Create a 64x64x64 volume of integers
    #volume = vol_region - 1
    volume = 32
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(volume,volume,volume))
    vol = pv.SimpleVolumeuint8(r)

    #Now fill the volume with our data (a sphere)
    v3dVolCenter = pv.Vector3Dint32_t(vol.getWidth() // 2, vol.getHeight() // 2, vol.getDepth() // 2)
    sphereRadius = 30
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

             #Write the voxel value into the volume
             vol.setVoxelAt(x, y, z, uVoxelValue);

    #Create a mesh, pass it to the extractor and generate the mesh
    mesh = pv.SurfaceMeshPositionMaterialNormal()
    extractor = pv.CubicSurfaceExtractorWithNormalsSimpleVolumeuint8(vol, r, mesh)
    extractor.execute()

    #That's all of the PolyVox generation done, now to convert the output to something OpenGL can read efficiently

    import numpy as np

    indices = np.array(mesh.getIndices()) #Throw in the vertex indices into an array
    #The vertices and normals are placed in an interpolated array like [vvvnnn,vvvnnn,vvvnnn]
    vertices = np.array([[vertex.getPosition().getX(), vertex.getPosition().getY(), vertex.getPosition().getZ()] for vertex in mesh.getVertices()] )
    #to test the vertices...
    print(vertices)

    Verts = vertices
    Edges = []
    
    out_sockets = [
        ['v', 'Verts', [Verts]],
        ['s', 'Edges', [Edges]],
    ]

    return in_sockets, out_sockets
