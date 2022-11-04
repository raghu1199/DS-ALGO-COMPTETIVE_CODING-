
from bisect import bisect_left,bisect_right,bisect,insort

# arr=[1,1,1,1,1]

# i=bisect_right(arr,1)
# print(i)


# # for desecnd order arr
# def upper(a,start,end,x):
#     if start>end:
#         return start
#     mid=(start+end)//2

#     if x<=a[mid]:
#         return upper(a,mid+1,end,x)
#     return upper(a,start,mid-1,x)

# # for descedn order
# def lower(a,start,end,x):
#     if start>end:
#         return start
#     mid=(start+end)//2
    
#     if x>=a[mid]:
#         return lower(a,start,mid-1,x)
#     return lower(a,mid+1,end,x)

# a=[1,1,1,1,1]
# #a=[0,0,0,1,1]

# print(lower(a,0,4,0))

def upper(arr,start,end,x):
    if start>end:
        return end
    mid=(start+end)//2

    if x>=arr[mid]:
        return upper(arr,mid+1,end,x)
    return upper(arr,start,mid-1,x)

# arr=[0,0,0,1,1,1]
# print(upper(arr,0,5,0))

s="abc"
print(s*2)

