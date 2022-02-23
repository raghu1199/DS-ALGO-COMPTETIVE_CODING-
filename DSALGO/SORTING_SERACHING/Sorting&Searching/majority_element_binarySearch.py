def lower_bound(arr,low,end,x):
    if low>end:
        return low
    
    mid=(low+end)//2
    # first find in left subarray if not then go to find in right
    if x<=arr[mid]:
        return lower_bound(arr,low,mid-1,x)
    
    return lower_bound(arr,mid+1,end,x)

def upper_bound(arr,low,end,x):
    if low>end:
        return low
    
    mid=(low+end)//2
    # first find in right subarr if not then go to left subarr
    if x>=arr[mid]:
        return upper_bound(arr,mid+1,end,x)
    
    return upper_bound(arr,low,mid-1,x)

def check_freq(arr,low,end,x):
    if arr[0]==x:
        lower=0
    else:
        lower=lower_bound(arr,low,end,x)
    if arr[end]==x:
        upper=end
    else:
        upper=upper_bound(arr,low,end,x)
    
    if (upper-lower)>=(len(arr)//2):
        print(f"Given element {x} appears more than or equal to n/2 times here {upper-lower} times.")
    else:
        print(f"given element appears only {upper-lower} times in {len(arr)} size input")



arr=[1,2,3,3,3,4,5,6]
check_freq(arr,0,len(arr)-1,3)