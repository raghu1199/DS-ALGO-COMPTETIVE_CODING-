
from collections import deque,defaultdict
class Graph:
    def __init__(self,nV):
        self.nV=nV
        self.adj=defaultdict(list)
        self.visited=[False]*nV
    
    def add_edge(self,u,v):
        self.adj[u].append(v)
        #self.adj[v].append(u)   #  if undirected graph then uncomment it
    
    def bfs(self,src):
        print("****BFS TRAVERSAL****")
        q=deque()
        q.append(src)
        while q:
            u=q.popleft()   # add at end remove from start (first in First out)
            print(u,end=" ")
            self.visited[u]=True
            for v in self.adj[u]:
                if self.visited[v]==False:
                    q.append(v)
                    self.visited[v]=True
        
        print()
        # at end of bfs reinitailize visited list with all false
        self.visited=[False]*self.nV

    
    def dfs(self,src):
        print("****DFS TRAVERSAL****")
        stack=deque()   # append at last(right) , pop fom last(right)
        stack.append(src)
        self.visited[src]=True

        while stack:
            u=stack.pop() # pop last item first
            print(u,end=" ")
            for v in self.adj[u]:
                if self.visited[v]==False:
                    stack.append(v)
                    self.visited[v]=True
        
        print()
        # end of dfs so reinitailize visited list with all false value so that bfs can be done
        self.visited=[False]*self.nV  



g=Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,6)
g.add_edge(3,4)
g.add_edge(5,6)
g.dfs(0)
g.bfs(0)