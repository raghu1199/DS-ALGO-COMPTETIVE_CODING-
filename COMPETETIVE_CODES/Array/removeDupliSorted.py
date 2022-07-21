
 #input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def dupli(arr):
    l=0
    arr[l]=arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            l+=1
            arr[l]=arr[i]
    return l+1  # as k

nums = [0,0,1,1,1,2,2,3,3,4]
print(dupli(nums))
print(nums)
