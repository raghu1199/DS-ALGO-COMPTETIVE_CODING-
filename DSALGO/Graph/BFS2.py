from collections import deque

from urllib3 import Retry

class Vertex:
    def __init__(self,name):
        self.name=name
        self.neighbours=[]
        self.distance=999999
        self.color='white'
    
    def add_neighbour(self,vertexname):
        if vertexname not in self.neighbours:
            self.neighbours.append(vertexname)


# key as vertex name nd value as vertex object in dict like {'a':Vertex('a'),'1':Vertex('1')}
class Graph:
    vertices=dict()
    
    def add_vertex(self,vertexObject):
        if isinstance(vertexObject,Vertex):
            # check is its name alredy in dict as key or not
            if vertexObject.name not in self.vertices:
                self.vertices[vertexObject.name]=vertexObject
                return True
            else:
                return "vertex name already in dict of vertices"
        else:
            return "please provide valid VertexObject"
    
    # get vertexobject nd add neighbour to it for both vertex  u nd v
    def add_edge(self,Uname,Vname):
        if Uname in self.vertices and Vname in self.vertices:
            for vertexname,vertex in self.vertices.items():
                if vertexname==Uname:
                    vertex.add_neighbour(Vname)
                if vertexname==Vname:
                    vertex.add_neighbour(Uname)
            return True
        else:
            return False
    
    # in queu append vertex name not object
    def bfs(self,vertexObject):
        q=deque()
        Uname=vertexObject.name
        # get object from our graph vertices
        Uobject=self.vertices[Uname]
        Uobject.distance=0
        q.append(Uobject.name)

        while q:
            u=q.popleft()  # now u has vertex name
            print(u,end=" ")
            Uobject=self.vertices[u]   # get object
            for vname in Uobject.neighbours:
                Vobject=self.vertices[vname]
                if Vobject.color=="white":
                    Vobject.color='grey'
                    q.append(Vobject.name)
                    Vobject.distance=Uobject.distance+1

            Uobject.color='Black'  # all neigbours processed so mark as visited


    
    #vertices={'a':Vertex('a'),'1':Vertex('1')}  so vertices[key] gives object of vertex
    def print_graph(self):
        for key in self.vertices.keys():
            print(f"{key}:neighbours:{self.vertices[key].neighbours}, dist is:{self.vertices[key].distance}")



g=Graph()

for i in range(7):
    g.add_vertex(Vertex(f'{i}'))

g.add_edge('0','1')
g.add_edge('0','2')
g.add_edge('1','3')
g.add_edge('1','4')
g.add_edge('2','5')
g.add_edge('2','6')
g.add_edge('3','4')
g.add_edge('6','5')
g.print_graph()
g.bfs(Vertex('0'))
print()
g.print_graph()
