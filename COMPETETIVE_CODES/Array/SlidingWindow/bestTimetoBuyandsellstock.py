

def besttimetobuyandsell(arr):
    n=len(arr)
    l,r=0,1
    res=0
    profit=0
    while r<=n-1:
        profit=arr[r]-arr[l]
        if profit < 0:
            l+=1
        else:
            r+=1
        res=max(res,profit)
    return res

arr=[7,1,5,3,6,4]
print(besttimetobuyandsell(arr))


