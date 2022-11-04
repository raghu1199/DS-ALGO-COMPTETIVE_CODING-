def stock(arr):
    n=len(arr)
    profit=0
    maxprofit=0
    l,r=0,1
    while r<=n-1:
        profit=arr[r]-arr[l]
        maxprofit=max(profit,maxprofit)
        if profit<=0:
            l=r
        r+=1
    return maxprofit
