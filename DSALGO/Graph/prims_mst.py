import sys

class primsMst:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for col in range(vertices)] for row in range(vertices)]
    
    def minKey(self,keyarr,visited):
        min=sys.maxsize
        min_index=0
        for v in range(self.V):
            if keyarr[v]<min and visited[v]==False:
                min=keyarr[v]
                min_index=v
        return min_index
    
    def primAlgo(self):
        key=[sys.maxsize]*self.V
        parent=[None]*self.V
        visited=[False]*self.V
        for _ in range(self.V):
            u=self.minKey(key,visited)  # O(V)
            visited[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and visited[v]!=True:
                    if self.graph[u][v]<key[v]:
                        key[v]=self.graph[u][v]
                        parent[v]=u
        self.printmst(parent)
        print("parent arrr:",parent)
        print("key arr:",key)

    def printmst(self,parent):
        print("edge\t weight")
        for v in range(1,self.V):
            print(parent[v],"-",v,"\t",self.graph[v][parent[v]])



g = primsMst(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
 
g.primAlgo()