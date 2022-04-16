
import sys

class Vertex:
    def __init__(self,name):
        self.name=name
        self.dist=sys.maxsize
        self.pred=None

class edge:
    def __init__(self,frm,to,weight):
        self.u=frm
        self.v=to
        self.weight=weight

def BellmanFord(nV,EdgeList,source):
    source.dist=0

    for i in range(nV-1):
        for edge in EdgeList:
            u,v,w=edge.u,edge.v,edge.weight
            if u.dist+ w < v.dist:
                v.dist=u.dist+w
                v.pred=u
    # to detect negative edge cycle
    for edge in EdgeList:
        u,v,w=edge.u,edge.v,edge.weight
        if u.dist + w < v.dist:
            print("Negative edge cycle detected")
            return True

def getshortestpath(vertexList,EdgeList,startV,targetV):
    BellmanFord(len(vertexList),EdgeList,startV)
    node=targetV
    path=[]
    while node is not None:
        path.append(node.name)
        node=node.pred
    for v in path[::-1]:
        print(v,end=" ->")
    print("All vertex dist from source")
    for v in vertexList:
        print(v.name,v.dist)

a=Vertex('a')
b=Vertex('b')
c=Vertex('c')
d=Vertex('d')
e=Vertex('e')

ab=edge(a,b,-1)
ac=edge(a,c,4)
bc=edge(b,c,3)
bd=edge(b,d,2)
db=edge(d,b,1)
be=edge(b,e,2)
ed=edge(e,d,-3)
dc=edge(d,c,5)
edgeList=[ab,ac,bc,bd,db,be,ed,dc]
vertexList=[a,b,c,d,e]
getshortestpath(vertexList,edgeList,a,e)



    

