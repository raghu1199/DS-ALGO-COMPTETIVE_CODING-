from collections import defaultdict
from heapq import heappop,heappush
import sys



def dijkstra(graph,source):
    distance={u:sys.maxsize for u in graph} # all dist infinite
    distance[source]=0
    pred=defaultdict(list)
    Q=[]
    visited=set()
    heappush(Q,(0,source))

    while Q:
        u_dist,u=heappop(Q)
        print(u,end=" ")
        if u in visited:
            continue   # go extract next min vertex, till here to down nothing executed
        visited.add(u)

        for v in graph[u]:
            if v in visited: continue
            if distance[u]+graph[u][v] < distance[v]:
                distance[v]=distance[u]+graph[u][v]
                pred[v].append(u)
                heappush(Q,(distance[v],v))
    print()

    print(distance)
    print(pred)


graph=defaultdict(dict)

nV,nE=map(int,input("enter noof vertex,noof edge").split())
print("enter edge details")
for i in range(nE):
    frm,to,cost=input().split()
    graph[frm][to]=int(cost)


dijkstra(graph,'s')