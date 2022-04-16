import heapq
from collections import defaultdict



def dijsktra(adj,src,dest):
    q=[]
    heapq.heappush(q,(0,src))   # push as (cost,vertex)
    while q:
        currCost,currVertex=heapq.heappop(q)  # extractmin from heap
        if currVertex==dest:
            print("shortest pasth from {} to {} is exit nd cost is:{}".format(src,dest,currCost))
            return True

        for v,neighCost in adj[currVertex]:
            updatedCost=currCost+neighCost
            heapq.heappush(q,(updatedCost,v))

adj=defaultdict(list)
nV,nE=map(int,input("ENter NoOFVertex,NoOFEdges:").split()) # take input convert input str to int using

# graph {A:[(B,4),(C,5)], B:[(D:10),(C,6)],....]}
for i in range(nE):
    u,v,w=input().split()
    adj[u].append((v,int(w)))

src,dest=map(str,input().split())
dijsktra(adj,src,dest)
