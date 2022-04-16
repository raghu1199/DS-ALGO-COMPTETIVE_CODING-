import sys
class Graph:
    def __init__(self,nV):
        self.nV=nV
        self.graph=[]
    
    # graph=[[0,1,10],[0,2,5],[1,3,7]]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def BellmanFord(self,source):
        print("Graph is:",self.graph)
        dist=[sys.maxsize]*self.nV
        dist[source]=0
        print("dist arr:",dist)

        for i in range(self.nV-1):
            print("relaxing {}th time".format(i))
            for u,v,w in self.graph:
                if dist[u]+w < dist[v]:
                    dist[v]=dist[u]+w
        
        # to detect negative cycle
        for u,v,w in self.graph:
            if dist[u]+ w < dist[v]:
                print("Contains negative edge cycle")
                break
        
        # print dist of all vertex from source
        for v in range(self.nV):
            print("{}\t{}".format(v,dist[v]))



g=Graph(3)    
# g.addEdge(0, 1, -1)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 2, 3)
# g.addEdge(1, 3, 2)
# g.addEdge(1, 4, 2)
# g.addEdge(3, 2, 5)
# g.addEdge(3, 1, 1)
# g.addEdge(4, 3, -3)
g.addEdge(0,1,-2)
g.addEdge(1,2,2)
g.addEdge(2,0,-2)
g.BellmanFord(0)
    



