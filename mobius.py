'''
This is a adaptation(to run in Blender 2.80) of Bob's 
script to generate a mobius strip

You may find the original one here:
https://blender.stackexchange.com/questions/82480/how-to-make-a-mobius-strip
'''
import bpy
from math import *
from mathutils import *


def mobius_mesh(resolution, major_radius, minor_radius, thick):

    verts = []
    faces = []

    for i in range(resolution):

        theta = 2*pi * i/resolution
        phi = pi * i/resolution

        rot1 = Matrix.Rotation(phi, 3, [0,1,0])
        rot2 = Matrix.Rotation(theta, 3, [0,0,1])
        c1 = Vector([major_radius, 0, 0])
        
        V_0 = Vector((-thick / 2, 0, minor_radius)) @ rot1[0]
        print(V_0)
        v1 = apply(rot2,c1 +  apply(rot1,Vector((-thick / 2, 0, minor_radius))))
        v2 = apply(rot2,(c1 + apply(rot1,Vector((thick / 2, 0, minor_radius)))))
        v3 = apply(rot2,(c1 + apply(rot1,Vector((thick / 2, 0, -minor_radius)))))
        v4 = apply(rot2,(c1 + apply(rot1,Vector((-thick / 2, 0, -minor_radius)))))
        
        i1 = len(verts)
        verts.extend([v1,v2,v3,v4])

        if i+1<resolution:
            ia = i1+4
            ib = i1+5
            ic = i1+6
            id = i1+7
        else:
            ia = 2
            ib = 3
            ic = 0
            id = 1

        # faces.append( [i1+j for j in range(4) ])
        faces.append( [i1,i1+1,ib,ia])
        faces.append( [i1+1,i1+2,ic,ib])
        faces.append( [i1+2,i1+3,id,ic])
        faces.append( [i1+3,i1,ia,id])
        
    mesh = bpy.data.meshes.new("mobius")
    mesh.from_pydata(verts, [], faces)

    for p in mesh.polygons:
        p.use_smooth=True

    return mesh

def apply(matrix,vector):
    '''
    matrix,vector -> vector
    
    this function receives a matrix and a vector and returns
    the vector obtained by multipling both of them
    '''
    V_0 = vector @ matrix[0]
    V_1 = vector @ matrix[1]
    V_2 = vector @ matrix[2]
            
    return Vector((V_0,V_1,V_2))

def mission1(scn, resolution, major_radius, minor_radius, thick):

    me = mobius_mesh(resolution, major_radius, minor_radius, thick)

    ob = bpy.data.objects.new("Mesh", me)

    #me.from_pydata(vertex_list, edge_list, [])
    #me.update()
    bpy.context.collection.objects.link(ob)
    


mission1(bpy.context.scene, 36, 5, 3, 0.1)