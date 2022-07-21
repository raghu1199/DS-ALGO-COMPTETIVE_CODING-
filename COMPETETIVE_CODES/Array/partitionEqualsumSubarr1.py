
# works only if continuos subarr need

# def splitarryEqualsum(arr):
#     l=0
#     r=len(arr)-1
#     left,right=0,0
#     if arr[l]<arr[r]:
#         left+=arr[l]
#         l=l+1
#     else:
#         right+=arr[r]
#         r=r-1
#     while l-1!=r+1:
#         if left<right:
#             left+=arr[l]
#             l=l+1
#         elif right<left:
#             right+=arr[r]
#             r=r-1
#         elif left==right:
#             return (l-1,r+1)
    
#     return False

#O(N)
def splitarr(arr):
    left,right=0,0
    for i in range(len(arr)):
        left+=arr[i]
    for i in range(len(arr)-1,-1,-1):
        right=right+arr[i]
        left=left-arr[i]
        if left==right:
            return (i-1,i)
    return False



#arr=[4,1,2,3]
#arr=[1,2,3,4,5,5]
arr=[3,2,1,4]
arr=[1,5,11,5]
print(splitarr(arr))


