
# not work for < 3 elements
# def peak(arr):
#     for i in range(1,len(arr)):
#         if arr[i-1]< arr[i] and arr[i] >arr[i+1]:
#             return (arr[i],i)
# #arr=[1,2,3,1]
# arr=[1,2,1,3,5,6,4]

# print(peak(arr))

# O(N)
# def findpeak(arr):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             return (arr[i]," index is:",i)
#     # if not returned yet means last ele is largest and it will be peak       
#     return len(arr)-1

# arr=[1,2,3,4,5]
# print(findpeak(arr))

def bs(arr,start,end,n):
    mid=(start+end)//2
    print("mid is:",mid)
    if (mid==0 or arr[mid-1]<arr[mid]) and (mid==n-1 or arr[mid+1]<arr[mid] ):
        return mid
    elif mid>0  and arr[mid-1]>arr[mid]:
        print("going left..")
        return bs(arr,start,mid-1,n)
    print("going right")
    return bs(arr,mid+1,end,n)

arr=[1,4,3,2,1]
print(bs(arr,0,len(arr)-1,len(arr)))



