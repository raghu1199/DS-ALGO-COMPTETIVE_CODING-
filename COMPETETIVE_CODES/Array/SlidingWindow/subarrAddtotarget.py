
def subarrsumtarget(arr,target):
    l,r=0,1
    n=len(arr)
    sum=arr[l]+arr[r]
    while r<=n-2:
        if sum==target:
            return(l,r)
        elif sum < target:
            r+=1
            sum+=arr[r]
        elif sum > target:
            if arr[l]<0:
                sum+=arr[l]
            else:
                sum-=arr[l]
            l+=1
            
    return 0

#arr=[1,2,3,4,5,6,7,8,9]
#arr=[-1,2,3,1,-3,2]
arr=[1,4,20,3,10,5]
print(subarrsumtarget(arr,33))

        
        
