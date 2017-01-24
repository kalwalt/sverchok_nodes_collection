import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings
#sys.path.append("/polyvox/lib")
import PolyVoxCore as pv

def sv_main(vol_region=32,sphere_radius=30):
    in_sockets = [
        ['s', 'Volume region', vol_region],
        ['s', 'Sphere radius', sphere_radius]
       ]

    #Create a 64x64x64 volume of integers
    #volume = vol_region - 1
    volume = 32
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(63,63,63))
    vol = pv.SimpleVolumeuint8(r)

    #Now fill the volume with our data (a sphere)
    v3dVolCenter = pv.Vector3Dint32_t(vol.getWidth() // 2, vol.getHeight() // 2, vol.getDepth() // 2)
    sphereRadius = 20
    #print(sphere_radius)
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
             #print(uVoxelValue)
             vol.setVoxelAt(x, y, z, uVoxelValue);

    #Create a mesh, pass it to the extractor and generate the mesh
    mesh = pv.SurfaceMeshPositionMaterialNormal()
    extractor = pv.CubicSurfaceExtractorWithNormalsSimpleVolumeuint8(vol, r, mesh)
    extractor.execute()

    #That's all of the PolyVox generation done, now to convert the output to something OpenGL can read efficiently

    vertices = []
    verts_out = []
   
        
    #Throw in the vertex indices into an array
    indices = mesh.getIndices()
    Nindx = mesh.getNoOfIndices()
    
    #uncomment the line above for testing pourpose only
    #print("Indices: " + str(indices))
    #print("N. of Indices: " + str(Nindx))
    
    for vertex in mesh.getVertices():
       
       p = vertex.getPosition()
       
       vertices.append(tuple([p.getX(), p.getY(), p.getZ()]))
    
    verts_out.append(vertices)
    
    #uncomment the line above for testing pourpose only  
    #print("Vertices: " + str(vertices))
    #print("N. vert: " + str(mesh.getNoOfVertices()))
   
    Tris = [(indices[i:i+3]) for i in range(0, len(indices)-1, 3)]
  
    out_sockets = [
        ['v', 'Verts', [verts_out]],
        ['s', 'Tris', [Tris]],
    ]
    
    #verts_out.append(vertices)

    return in_sockets, out_sockets
