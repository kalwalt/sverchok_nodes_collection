import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings
#sys.path.append("/polyvox/lib")
import PolyVoxCore as pv
from mathutils import noise, Vector
import math

def sv_main(uVoxelValue=[],vol_region=4):
    in_sockets = [
        ['s', 'Voxel value', uVoxelValue],
        ['s', 'Volume region', vol_region]
       ]
    #64 voxels values as volume region of 4x4x4 (for testing pourpose)
    #uVoxelValue=[[0, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 255, 255, 0, 0, 255, 255, 255, 255, 0, 255, 0, 255, 0, 255, 255, 0, 255, 255, 0, 0, 255, 0, 255, 255, 255, 255, 255, 0, 255, 0, 255, 255, 255, 255, 0, 255, 0, 0, 255, 255, 0, 255, 0]]
    
    #print(len(voxel_value[0]))
    print("Voxel_value inside_script: {0}".format(uVoxelValue))
    
    
    #Create a volume of integers
    volume = vol_region - 1
    
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(volume,volume,volume))
    
    vol = pv.SimpleVolumeuint8(r)
    #Now fill the volume with our data 
    #v3dVolCenter = pv.Vector3Dint32_t(vol.getWidth() // 2, vol.getHeight() // 2, vol.getDepth() // 2)
    print(vol.getDepth()*vol.getHeight()*vol.getWidth())
    #This three-level for loop iterates over every voxel in the volume
    for z in range(vol.getDepth()):
       for y in range(vol.getHeight()):
          for x in range(vol.getWidth()):
           
            if uVoxelValue:
                #print("ok")
                vol.setVoxelAt(x, y, z, uVoxelValue[0][0][x*y*z]);
                         
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
