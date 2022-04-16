from collections import deque ,defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    #initialy{0:[],1:[],..} then after adding edge {0:[1,2],1:[0,2],2:[0,1,3],3:[2]}
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph
    
    def bfs(self,source):
        # crate list of all vertex starting from 0 to max key present in graph
        # by default make all vertex visited false we [False,False,False] means visited[2] is False here
        visited=[False]*(max(self.graph)+1)
        q=deque()
        q.append(source)
        visited[source]=True
        result=[]
        while q:
            u=q.popleft()
            result.append(u)
            print(f"{u} has neigjbours:{self.graph[u]}")
            # visit all neighbours of u and enqueu it in Q, ex here self.graph[0] gives [1,2] as list
            # check in visited list for each vertex  like visted[1]? visited[2]
            for v in self.graph[u]:
                if visited[v]==False:
                    q.append(v)
                    visited[v]=True
        print("BFS traversal:",result[::])


g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,6)
g.add_edge(3,4)
g.add_edge(6,5)
g.bfs(0)

# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
# g.bfs(2)


        


