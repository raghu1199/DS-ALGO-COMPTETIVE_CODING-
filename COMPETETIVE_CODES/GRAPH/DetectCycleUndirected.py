

		
		
def dfs(u,src,prev):
    curr=u
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            if v==src:
                flag[0]=True
                return
            if prev!=curr:
                visited[prev]=False
            dfs(v,src,u)
        


def cycle(adj):
    for u in range(0,V):
        dfs(u,u,u)
        if flag[0]==True:
            return 1
    return 0


#adj=[[4],[2,4],[1,3],[2,4],[0,1,3]]
adj=[[],[2],[1,3],[2]]
adj=[[]]
V=len(adj)
visited=[False]*(V+1)
flag=[False]
		
print(cycle(adj))