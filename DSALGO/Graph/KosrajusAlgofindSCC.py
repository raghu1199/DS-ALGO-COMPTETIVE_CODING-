from collections import defaultdict,deque

class Graph:
    def __init__(self,nV):
        self.nV=nV
        self.adjlist=defaultdict(list)
    
    def add_edge(self,u,v):
        self.adjlist[u].append(v)
    
    def dfstoPush(self,u,visited,stack):
        # mark current node as visited
        visited[u]=True
        # go to all neighbours of this verftex recursively
        for v in self.adjlist[u]:
            if visited[v]==False:
                self.dfstoPush(v,visited,stack)

        # all neighbours visited so finish this vertex u nd push to stack
        stack.append(u)
    
    def dfsforScc(self,u,visited):
        # mark current vertex as visited
        visited[u]=True
        print(u,end=" ")
        # go to neighbours of this vertex recursively
        for v in self.adjlist[u]:
            if visited[v]==False:
                self.dfsforScc(v,visited)

    
    # adjList {0:[1,2],1:[2],2:[3],3:[1],4:[3,5],5:[5]}
    def getTranspose(self):

        graphObject=Graph(self.nV)  # need to add reverse edges in adjacencylist

        for u in self.adjlist:
            for v in self.adjlist[u]:
                graphObject.add_edge(v,u)      # edge (u->v ) reversed as edge (v->u)
        # return reverse graph object
        return graphObject


    
    # main func which finds SCC(strongly connectied components in graph)
    def printSCC(self):

        stack=deque()  # append at last pop from last so use pop()  not popleft()
        # mark all vertex unvisited for first dfs
        visited=[False]*self.nV

        # going for first dfs to fill stack depend on max finish time on top
        # as vertex finish(all its neighbour visited) push to stack
        for u in range(self.nV):
            if visited[u]==False:
                self.dfstoPush(u,visited,stack)
        print()
        print("after first dfs stack is(max finish(at last) time to least):",stack)

        # get transpose graph by reversing all edges if edge (u->v) make it (v->u)
        GT=self.getTranspose()

        # reinitialize all vertex to False as visited to perform 2nd dfs
        visited=[False]*self.nV

        # pop top of vertex of stack each time nd apply dfs on it(print all vertex of its adjcency)
        #  they form scc ,if all its neighbour visited
        #  it will come back here to get next vertex from stack
        while stack:
            u=stack.pop()
            if visited[u]==False:
                GT.dfsforScc(u,visited)
                print()


g=Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.printSCC()



