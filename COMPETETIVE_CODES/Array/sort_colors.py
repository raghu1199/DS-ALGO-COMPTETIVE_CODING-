
# o(n^2)
# def sortcolors(arr):
#     n=len(arr)
#     l,r=0,n-1
#     while l<r:
#         for j in range(l+1,r+1):
#             if arr[l]==arr[j]:
#                 arr[l+1],arr[j]=arr[j],arr[l+1]
#                 l=l+1
#         else:
#             l=l+1
#     print(arr)

# arr=[0,1,0,1,2,1,2,1]
# sortcolors(arr)

# bucket sort
def sortcolors2(arr,k):
    bucket=[0]*k
    for j in range(k):
        for i in range(len(arr)):
            if j==arr[i]:
                bucket[j]+=1
    print(bucket)
    arr.clear()
    for j in range(k):
        for i in range(bucket[j]):
            arr.append(j)
            
    print(arr)
            

# arr=[0,1,0,1,2,1,2,1]
# sortcolors2(arr,3)

def sortcolorsBetter(arr):
    n=len(arr)
    c,l,h=0,0,n-1
    while c<=h:
        # if 0 then swap to left
        if arr[c]==0:
            arr[l],arr[c]=arr[c],arr[l]
            c+=1
            l+=1
        elif arr[c]==1:
            c+=1
        elif arr[c]==2:
            arr[h],arr[c]=arr[c],arr[h]
            h-=1
    return arr
        

#arr=[0,1,0,1,2,1,2,1]
arr=[1,0,1,1,2,0,0]

print(sortcolorsBetter(arr))



