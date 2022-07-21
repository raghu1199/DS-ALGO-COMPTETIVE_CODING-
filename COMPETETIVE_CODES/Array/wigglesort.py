

# def wigglesort(arr):

#     less=False    
#     for i in range(len(arr)-1):
#         if less==False:
#             if arr[i]> arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#                 less=True
#             else:
#                 less=True
#         elif less==True:
#             if arr[i]<arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#                 less=False
#             else:
#                 less=False
#     print(arr)


# def wigglesort(arr):
#     arr.sort()
#     for i in range(1,len(arr)-1,2):
#         arr[i],arr[i+1]=arr[i+1],arr[i]
    
#     return arr


# arr=[3,5,2,1,6,4]
# print(wigglesort(arr))

def wigglesort2(arr):
    for i in range(1,len(arr)-1,2):
        if arr[i-1] > arr[i]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
        if i<len(arr)-1 and arr[i] < arr[i+1]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
    return arr

arr=[3,5,2,1,6,4]
print(wigglesort2(arr))
    






        





        