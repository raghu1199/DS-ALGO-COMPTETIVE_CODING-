def maxsumsubarr(arr):
    maxsum=arr[0]
    csum=0
    for i in range(len(arr)):
        if csum<0:
            csum=0
        csum+=arr[i]
        maxsum=max(maxsum,csum)
    return maxsum

        
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxsumsubarr(arr))