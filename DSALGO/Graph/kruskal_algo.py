
class Kruskal:
    def __init__(self,nV):
        self.nV=nV
        self.graph=[]
    
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    
    def kruskal_algo(self):
        mst=[]
        self.graph=sorted(self.graph,key=lambda item:item[2])
        # initalize parent arr all item iself as parent
        parent=[i for i in range(self.nV)]
        i,e=0,0
        while e< self.nV-1:
            u,v,w=self.graph[i]
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                mst.append([u,v,w])
                parent[y]=x
                e+=1  # mst must contain edges =v-1 so if edge successulfy addedt to mst then only incre edge cpunt
            i+=1
        
        print(mst)


g = Kruskal(6)
g.add_edge(0, 1, 4)
g.add_edge(1, 0, 4)
g.add_edge(0, 2, 4)
g.add_edge(2, 0, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(3, 2, 3)
g.add_edge(2, 5, 2)
g.add_edge(5, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(4, 2, 4)
g.add_edge(3, 4, 3)
g.add_edge(4, 3, 3)
g.add_edge(4, 5, 3)
g.add_edge(5, 4, 3)
g.kruskal_algo()
