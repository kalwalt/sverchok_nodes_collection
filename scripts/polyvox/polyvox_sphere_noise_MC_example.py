import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings
#sys.path.append("/polyvox/lib")
import PolyVoxCore as pv
from mathutils import noise, Vector
import math

def sv_main(vol_region=32,sphere_radius=14):
    in_sockets = [
        ['s', 'Volume region', vol_region],
        ['s', 'Sphere radius', sphere_radius]
       ]

    #Create a 64x64x64 volume of integers
    volume = vol_region - 1
    
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(volume,volume,volume))
    vol = pv.SimpleVolumeuint8(r)
      
    #Now fill the volume with our data (a sphere)
    v3dVolCenter = pv.Vector3Dint32_t(vol.getWidth() // 2, vol.getHeight() // 2, vol.getDepth() // 2)
    sphereRadius = sphere_radius
    #print(sphere_radius)
    #This three-level for loop iterates over every voxel in the volume
    for z in range(vol.getDepth()):
       for y in range(vol.getHeight()):
          for x in range(vol.getWidth()):
              
            #compute Noise so we add to the distance field
            plusFactor = noise.fractal(Vector((x,y,z)), 0.25, 0.75, 3, 1) * 6.0
            #print(plusFactor)
            
            #Compute how far the current position is from the center of the volume    
            fDistToCenter = (pv.Vector3Dint32_t(x,y,z) - v3dVolCenter).length()
            #print(fDistToCenter)
            
            #If the current voxel is less than 'radius' units from the center then we make it solid.
            
            #if(fDistToCenter + plusFactor <= sphereRadius + (noise.random()*3)):
            if(fDistToCenter + plusFactor <= sphereRadius ):
            #Our new voxel value
                uVoxelValue = 255
            else:
                uVoxelValue = 0
            
            #Write the voxel value into the volume
            #print(uVoxelValue)
            vol.setVoxelAt(x, y, z, uVoxelValue);
             
    #Create a mesh, pass it to the extractor and generate the mesh
    mesh = pv.SurfaceMeshPositionMaterialNormal()
    extractor = pv.MarchingCubesSurfaceExtractorSimpleVolumeuint8(vol, r, mesh)
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
