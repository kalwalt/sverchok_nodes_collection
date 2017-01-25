import sys
sys.path.append("//home/walter/blender-2.78a-linux-glibc211-x86_64/2.78/scripts/addons/sverchok-master/node_scripts/templates/polyvox/lib") #This is just to point to the generated bindings
#sys.path.append("/templates/polyvox/lib")
import PolyVoxCore as pv
from mathutils import noise, Vector

def createPerlinTerrain(volData, Hfactor, Lacunarity, octaves):


    for x in range(volData.getWidth()):

        for y in range(volData.getHeight()):

            perlinVal = noise.fractal(Vector((x,y,0)),Hfactor,Lacunarity, octaves)
            #for debuugging pourpose comment the line below
            #print("perlin values: " + str(perlinVal))
            perlinVal += 1.0
            perlinVal *= 0.5
            perlinVal *= volData.getWidth()

            for z in range(volData.getDepth()):


                if(z < perlinVal):

                    uVoxelValue = 245

                else:

                    uVoxelValue = 0

                volData.setVoxelAt(x, y, z, uVoxelValue);
                
    return volData

def sv_main(vol_region=64,h_factor=1.0, lacunarity=1.5,octaves=3, ):
    in_sockets = [
        ['s', 'Volume region', vol_region],
        ['s', 'H Factor ', h_factor],
        ['s', 'lacunarity', lacunarity],
        ['s', 'octaves', octaves]
       ]

    #Create a volume of integers
    volume = vol_region - 1
    #volume = 32
    r = pv.Region(pv.Vector3Dint32_t(0,0,0), pv.Vector3Dint32_t(volume,volume,volume))
    vol = pv.SimpleVolumeuint8(r)
   
    #This three-level for loop iterates over every voxel in the volume
    createPerlinTerrain(vol, h_factor, lacunarity, octaves)
    print("terain: Done! > let's go w the extractor...")
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
