
adj=[[],[2,3],[1,3],[1,2],[5,6],[4,6],[4,5,7],[6]]
V=len(adj)
print(V)
visited=[False]*(V+1)
nodes=[]

def dfs(u):
    visited[u]=True
    nodes.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v)


def NoOfgoodComponents(adj,V):
    cnt=0
    for u in range(1,V):
        if not visited[u]:
            nodes.clear()
            dfs(u)
            isFullyconnected=True
            print("nodes:",nodes)
            size=len(nodes)
            for n in nodes:
                if len(adj[n])!=size-1:
                    isFullyconnected=False
                    break
            if isFullyconnected:
                cnt+=1
    
    return cnt

print(NoOfgoodComponents(adj,V))


