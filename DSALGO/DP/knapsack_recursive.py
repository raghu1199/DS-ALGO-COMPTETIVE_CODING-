
def knap(W,wt,val,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knap(W,wt,val,n-1)
    
    include=val[n-1]+knap(W-wt[n-1],wt,val,n-1)
    exclude=knap(W,wt,val,n-1)
    return max(include,exclude)