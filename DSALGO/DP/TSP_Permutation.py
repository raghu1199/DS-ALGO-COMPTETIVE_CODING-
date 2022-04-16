
import sys
from itertools import permutations

def tsp(graph,s,nV):
    vertex=[]
    # store all vertex except source vertex to create permutations
    for i in range(nV):
        if i!=s:
            vertex.append(i)
    min_path=sys.maxsize
    next=permutations(vertex)

    for i in next:
        current=0
        k=s
        for j in i:              # if permutation[1,2,3]
            current+=graph[k][j]  # g[0][1]+g[0][2]+g[0][3]
            k=j
        # to create cycle add edge cost from last vertex to source
        current+=graph[k][s]  # k=3 so graph[3][0]
        min_path=min(min_path,current)

    return min_path

graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
s=0
V=4
print(tsp(graph,s,V))