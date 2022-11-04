



N=10
parent=[0]*N
rank=[0]*N

def makeSet():
    for i in range(0,N):
        parent[i]=i
        rank[i]=0

def findParent(ele):
    if ele==parent[ele]:
        return ele
    parent[ele]=findParent(parent[ele])
    return parent[ele]


def union(u,v):
    x=findParent(u)
    y=findParent(v)

    # to avoid cycle if both in same set no need to merge
    if x!=y:
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[x]>rank[y]:
            parent[y]=x
        elif rank[x]==rank[y]:
            parent[y]=x
            rank[x]+=1
        return True
    else:
        return False
    

def main():
    n=int(input("No of operation of union:"))
    makeSet()
    while n:
        u,v=map(int,list(input().split(" ")))
        union(u,v)
        n-=1
    
    x=2
    y=8
    print("parent:",parent)
    if findParent(x)!=findParent(y):
        print("in diff set")
    else:
        print("In same set")


main()

