

def trapWater(arr):
    n=len(arr)
    left=[0]*n
    right=[0]*n
    leftmax=arr[0]
    for i in range(1,n):
        left[i]=leftmax
        leftmax=max(leftmax,arr[i])
    rightmax=arr[n-1]
    for i in range(n-1,-1,-1):
        right[i]=rightmax
        rightmax=max(rightmax,arr[i])
    
    trappedwater=0
    for i in range(1,n):
        if arr[i]<left[i] and arr[i]<right[i]:
            trappedwater+=min(left[i],right[i])-arr[i]
    return trappedwater

arr=[4,2,0,3,2,5]
print(trapWater(arr))
    
