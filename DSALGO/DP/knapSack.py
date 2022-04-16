
def knapsack(wt,val,Capacity,n):
    k=[[0 for w in range(Capacity+1) ] for i in range(n+1) ]

    for i in range(n+1):
        for w in range(Capacity+1):
            if i==0 or w==0:
                k[i][w]=0
            if wt[i-1]<= w:
                k[i][w]=max(k[i-1][w],k[i-1][w-wt[i-1]]+val[i-1])
            else:
                k[i][w]=k[i-1][w]
    
    return k[n][Capacity]

val = [60, 100, 120]
wt = [10, 20, 30]
Capacity = 50
n = len(val)
print(knapsack(wt, val,Capacity,n))

