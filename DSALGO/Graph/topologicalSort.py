from collections import defaultdict,deque


class Graph:
    def __init__(self,nV):
        self.V=nV
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs_visit(self,u,visited,order):
        visited[u]=True
        for v in self.graph[u]:
            if visited[v]==False:
                self.dfs_visit(v,visited,order)
        # all neighbours done so it will now do backtrack to prev node
        # so add current node to in stack 
        order.appendleft(u)
    
    def topologicalSort(self):
        visited=[False]*self.V
        order=deque()
        for u in range(self.V):
            if visited[u]==False:
                self.dfs_visit(u,visited,order)
        
        print(order)


g= Graph(6)
g.addEdge(3, 1)
g.addEdge(5, 0)
g.addEdge(5, 2)

g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)

g.topologicalSort()

        

