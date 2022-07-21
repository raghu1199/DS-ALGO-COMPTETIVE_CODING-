
def maxsumsubarrwithksize(arr,k):
    maxs=0
    for i in range(0,len(arr)-k+1):
        wsum=0
        for j in range(i,i+k):
            wsum+=arr[j]
        maxs=max(maxs,wsum)
    return maxs

arr=[1,9,-1,-2,7,3,-1,2]
print(maxsumsubarrwithksize(arr,4))

def maxsumsubarrwithk(arr,k):
    maxs=0
    
    n=len(arr)
    wsum=0
    for i in range(0,k):
        wsum+=arr[i]
    maxsum=wsum
    l,r=0,k-1
    while r<=n-2:
        wsum-=arr[l]
        l+=1
        r+=1
        wsum+=arr[r]
        maxsum=max(wsum,maxsum)
    return maxsum


arr=[1,9,-1,-2,7,3,-1,2]
print(maxsumsubarrwithk(arr,4))

    
        


