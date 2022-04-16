import sys
from heapq import heapify,heappush,heappop

graph={
    's':{'t':10,'y':5},
    't':{'y':2,'x':1},
    'y':{'t':3,'x':9,'z':2},
    'z':{'s':7,'x':6},
    'x':{'z':4}
}
# node={
#         'A':{'dist':inf,'pred':[]},
#         'B':{'dist':inf,'pred':[]},
#         'C':{'dist':inf,'pred':[]},
#         'D':{'dist':inf,'pred':[]},
#         'E':{'dist':inf,'pred':[]},
#         'F':{'dist':inf,'pred':[]},
#     }

# graph={
#     'A':{'B':2,'C':4},
#     'B':{'A':2,'C':3,'D':8},
#     'C':{'A':4,'B':3,'E':5,'D':2},
#     'D':{'B':8,'C':2,'E':11,'F':22},
#     'E':{'C':5,'D':11,'F':1},
#     'F':{'D':22,'E':1},
# }
def update(Q,v,newCost):
    lenQ=len(Q)
    i=0
    for item in Q:
        if item[1]==v:
            l=list(item)
            
            Q[0],Q[i]=Q[i],Q[0]
            heappop(Q)
            l[0]=newCost
            Nitem=tuple(l)
            heappush(Q,Nitem)
            return
        i+=1
    # if not already in heap then simply push
    else:
        heappush(Q,(newCost,v))

        

def dijkstra(graph,src,dest):
    visited=[]
    inf=sys.maxsize
    node={
        's':{'dist':inf,'pred':[]},
        't':{'dist':inf,'pred':[]},
        'y':{'dist':inf,'pred':[]},
        'x':{'dist':inf,'pred':[]},
        'z':{'dist':inf,'pred':[]},
    }
    # initialize source dist 0
    node[src]['dist']=0
    Q=[]
    heappush(Q,(node[src]['dist'],src))
    print(Q)
    # Q [(0,'s'),(5,'y'),(10,'t')]
    while Q:
        print("visited:",visited," Q is:",Q)
        u_dist,u = heappop(Q)
        visited.append(u)
        print(u)   # print shortest path
        #print("visited:",visited," Q is:",Q)
        
        for v in graph[u]:
            if v not in visited:
                cost=u_dist + graph[u][v]
                if cost < node[v]['dist']:
                    node[v]['dist']=cost
                    node[v]['pred']=node[v]['pred']+list(u)
                    heappush(Q,(node[v]['dist'],v))    # heap can contains duplicate vertices multiple times
                    #update(Q,v,cost)
                
    
    print(f"SHotest dist from {src} to {dest} is:{node[dest]['dist']}")
    print(f"shortest path is :{node[dest]['pred']}")


dijkstra(graph,'s','x')


