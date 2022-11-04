

graph=defaultdict(dict)

def dijkstra():
    for item in roads:
        frm,to,cost=item
        graph[frm][to]=cost
        graph[to][frm]=cost

    #print(graph)
    dist={}
    for u in graph:
        dist[u]=sys.maxsize
        pred[u]=[]
    source=0
    dist[source]=0
    visited=set()
    q=[]
    heapq.heappush(q,[0,source])
    res=[]
    cnt=0
    while q:
        udist,u=heapq.heappop(q)
        #print("u:",graph[u])
        if u in visited and u!=n-1:
            continue
        if u!=n-1:
            visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if dist[u]+graph[u][v]<=dist[v]:
                    print(u,v,graph[u][v])
                    dist[v]=dist[u]+graph[u][v]
                    pred[v].append(v)
                heapq.heappush(q,[dist[v],v])
