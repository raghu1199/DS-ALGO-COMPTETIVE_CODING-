from heapq import heappop,heappush
from collections import deque

import sys

class Vertex:
    def __init__(self,name):
        self.name=name
        self.dist=sys.maxsize
        self.pred=None
        self.visited=False
        self.adj=[]

class edge:
    def __init__(self,weight,sourceV,destV):
        if isinstance(sourceV,Vertex) and isinstance(destV,Vertex):
            self.weight=weight
            # self.source=sourceV
            # self.dest=destV
            sourceV.adj.append((weight,destV))

def bfs():
    Q=deque()

def dijkstra(sourceV):
    if isinstance(sourceV,Vertex):
        Q=[]
        sourceV.dist=0
        heappush(Q,(0,sourceV))

        while Q:
            u_dist,u=heappop(Q)  # extract min and mark as visited
            u.visited=True
            print(u.name,end=" ")

            for item in u.adj:
                eweight,v=item
                if not v.visited:
                    if u.dist+eweight < v.dist:
                        v.dist=u.dist+eweight
                        v.pred=u
                        heappush(Q,(v.dist,v))
        print()

def shortestPath(targetV):
    print(f"shortest path from s to {targetV.name}  cost is:",targetV.dist,end=" ")
    vertex=targetV
    path=[]
    print("Shortest route is:",end=" ")
    while vertex is not None:
        path.append(vertex)
        vertex=vertex.pred
    for i in range(len(path)-1,-1,-1):
        v=path[i]
        print(v.name,"-> ",end=" ")
    print()



s=Vertex('s')
t=Vertex('t')
y=Vertex('y')
x=Vertex('x')
z=Vertex('z')

st=edge(10,s,t)
sy=edge(5,s,y)
ty=edge(2,t,y)
yt=edge(3,y,t)
yz=edge(2,y,z)
yx=edge(9,y,x)
tx=edge(1,t,x)
zx=edge(6,z,x)
xz=edge(4,x,z)
zs=edge(9,z,s)
#print(y.adj)
dijkstra(s)
shortestPath(x)
shortestPath(z)
