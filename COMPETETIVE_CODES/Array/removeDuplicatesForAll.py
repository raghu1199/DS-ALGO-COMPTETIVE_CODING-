
from os import remove


def finddupli(arr):
    out=[]
    for num in arr:
        idx=abs(num)-1
        if arr[idx]>0:
            arr[idx]*=-1
        else:
            out.append(abs(num))
    return out

# arr=[2,3,4,5,3,7,2,3,4]
# print(finddupli(arr))

# def removedupli(arr):
#     freq={}
#     for ele in arr:
#         if ele in freq:
#             freq[ele]+=1
#         else:
#             freq[ele]=1
#     k=len(arr)
#     i=0
#     while i<len(arr):
#         occ=freq[arr[i]]
#         print("before remove:",occ)
#         if occ>=2:
#             arr.remove(arr[i])
#             freq[l[i]]-=1
#             print(freq,arr)
#             i=i
#         else:
#             i+=1
#     return k

# # arr2=[2,3,4,5,3,7,2,3,4]
# # newarr=list(set(arr2))
# # print(newarr)
# arr2=[2,3,1,1,1,1]
# print(removedupli(arr2))
# print(arr2)

# effiecient
def rd(arr):
    freq={}
    for ele in arr:
        freq[ele]=False
    l=0
    for i in range(len(arr)):
        ele=arr[i]
        if freq[ele]==False:
            arr[l]=ele
            l+=1
            freq[ele]=True
    for i in range(l):
        print(arr[i])

arr=[2,2,3,4,5,3,7,2,3,4]
rd(arr)


