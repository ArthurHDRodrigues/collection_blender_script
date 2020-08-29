import bpy, math

s = 100 #curve's number of sides
nome = "8figure"

def parametric(t):
    x = (2+math.cos(2*t))*math.cos(3*t)
    y = (2+math.cos(2*t))*math.sin(3*t)
    z = math.sin(4*t)
    
    return(x,y,z)

def main():
    step = 2*math.pi/s

    vertices = []

    for i in range(s):
        vertices.append(parametric(step*i))
    
    edges = []
    for i in range(s-1):
        edges.append([i,i+1])
    edges.append([s-1,0])
    

    me = bpy.data.meshes.new(nome + "Mesh")
    ob = bpy.data.objects.new(nome, me)


    # Make a mesh from a list of vertices/edges/faces
    me.from_pydata(vertices, edges, [])

    # Display name and update the mesh
    ob.show_name = True
    me.update()

    bpy.context.collection.objects.link(ob)
    
main()