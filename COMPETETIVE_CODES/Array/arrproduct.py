
# from collections import deque
# def productinotj2(arr):
#     output=deque()
#     for i in range(0,len(arr)):
#         product=1
#         for j in range(0,len(arr)):
#             if j!=i:
#                 product*=arr[j]
#         output.append(product)
#     for i in range(0,len(output)):
#         print(output[i],end=" ")
    

# arr=[1,2,3,4]
# productinotj2(arr)

# def productinotj(arr):
#     output=[]
#     for i in range(0,len(arr)):
#         product=1
#         for j in range(0,len(arr)):
#             if j!=i:
#                 product*=arr[j]
#         output.append(product)
#     return output

# arr=[1,2,3,4]
# print(productinotj(arr))

# # not O(N) 
# def productarr(arr):
#     product=1
#     output=[]
#     for i in range(len(arr)):
#         product*=arr[i]
#     for i in range(len(arr)):
#         temp=product
#         j=0
#         while temp!=0:
#             temp=temp-arr[i]
#             j+=1
#         output.append(j)
#     print(output)

# arr=[1,2,3,4]
# productarr(arr)


# O(N) time and O(N) space

def product(arr):
    n=len(arr)
    left=[1]*(n)
    right=[1]*(n)
    left[0]=1
    left[1]=1*arr[0]
    right[n-1]=1
    right[n-2]=1*arr[n-1]
    for i in range(2,n):
        left[i]=left[i-1]*arr[i-1]
    print(left)
    end=len(arr)-1
    #print(n)
    for j in range(end-2,-1,-1):
        right[j]=right[j+1]*arr[j+1]
    print(right)
    
    output=[]
    for i in range(0,n):
        product=left[i]*right[i]
        output.append(product)
    print(output)

# arr=[1,2,3,4]
# product(arr)

# O(N) time and O(1) space
def product2(arr):
    n=len(arr)
    left=[1]*len(arr)
    left[0]=1
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]
    r=1
    for i in range(n-1,-1,-1):
        left[i]=left[i]*r
        r=r*arr[i]

    return left

arr=[1,2,3,4]
print(product2(arr))

