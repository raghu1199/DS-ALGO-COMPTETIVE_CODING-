from collections import defaultdict

class DFS:
    def __init__(self,NoOfvertices):
        self.nV=NoOfvertices
        self.colors=['white']*self.nV
        self.d=[0]*self.nV   # discover time
        self.f=[0]*self.nV    # finish time
        self.graph=defaultdict(list)

    # gra[h {0:[1,2],1:[2],2:[3],3:[1],4:[3,5],5:[5]}
    def add_edge(self,u,v):
        self.graph[u].append(v)   # it is same as 1)graph[u]=[] nd then 2) graph[u].append(v)
    
    def dfs_visit(self,u):
        self.colors[u]='grey'
        self.time+=1
        self.d[u]=self.time
        print(u,end=" ")
        # go to u's adjacency list
        for v in self.graph[u]:
            if self.colors[v]=='white':
                self.dfs_visit(v)
        self.time+=1
        self.colors[u]='black'
        self.f[u]=self.time

    
    def dfs(self):
        self.time=0
        for u in range(self.nV):
            if self.colors[u]=='white':
                self.dfs_visit(u)
        print()
        print("discovery time :",self.d,"end time:",self.f)

d=DFS(6)
d.add_edge(0,1)
d.add_edge(0,2)
d.add_edge(1,2)
d.add_edge(2,3)
d.add_edge(3,1)
d.add_edge(4,3)
d.add_edge(4,5)
d.add_edge(5,5)
d.dfs()
