
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Graph:
    def __init__(self,NoOfvertices):
        self.nV=NoOfvertices
        self.graph=[None]*self.nV

    #[2->1->N,2->0->N,0->1-N,N]  add edge (2,3) so add node 3 to linked list of 2
    #node=3 ,3.next=graph[src=2]=0->1->N (maintain prev data)so node 3 looks like 3->0>1->N 
    # update at src so graph[src=2]=node 3 , [2->1>N,2->0->N,3->0>1->N,N]
    # now make edge(3,2) also means add node 2 to linked list of node 3, node=2, 2.next =graph[src=3]=N so 2->N now update at src node 3
    # graph[src=3]=node 2 so it looks like [2->1->N,2->0->N,3->0>1->N,2->N]
    def add_edge(self,src,dest):
        node=Node(dest)
        # copy prev list present at src nd add to dest node's next nd then place this new dest node
        #  to src as newly updated linked list of src
        node.next=self.graph[src]
        self.graph[src]=node
        # undirected graph so after edge (src,dest) make edge (dest,src) also
        node=Node(src)
        node.next=self.graph[dest]
        self.graph[dest]=node

    #[2->1->N, 2->0->N, 3->0>1->N, 2->N]
    def print_graph(self):
        for i in range(self.nV):
            print("Adjacency list of vertex {}:".format(i),end=" ")
            current=self.graph[i]  # 2->1->None for i=0

            while current is not None:
                print("->{}".format(current.data),end=" ")
                current=current.next
            print("\n")
    
g=Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
print()
g.print_graph()




