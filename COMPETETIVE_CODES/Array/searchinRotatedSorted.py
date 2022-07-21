
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

def searchinSortedArr(arr,sum):

    # find pivot
    n=len(arr)
    l,r=0,0
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            r=i
            l=i+1
    while l!=r:
        if arr[l]+arr[r]==sum:
            return True
        # l+r=37 <req(45) so add little big value than current
        elif arr[l]+arr[r]<sum:
            l=(l+1)%n
        elif arr[l]+arr[r]>sum:
            r=(r-1+n)%n
    return False

arr=[11,15,26,38,9,10]
sum=35
sum2=45
print(searchinSortedArr(arr,sum))
print(searchinSortedArr(arr,sum2))

def searchtarget(arr,target):
    n=len(arr)
    l,r=0,0
    updated=False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            l=i+1
            r=i
            updated=True

    # to handle [1,3] in this l,r not updated arr laredy sorted           
    if not updated:
        l,r=0,n-1
    # to handle 1 ele [1] targte 1        
    if l==r:
        if arr[l]==target:
                return l
    while l!=r:
        if arr[l]==target:
            return l
        elif arr[r]==target:
            return r
        if arr[l]<target:
           l=(l+1)%n
        else:
            r=(n+r-1)%n       
    return -1

arr=[11,15,26,38,9,10]
arr1=[1,3]
target=1
print(searchtarget(arr1,target))