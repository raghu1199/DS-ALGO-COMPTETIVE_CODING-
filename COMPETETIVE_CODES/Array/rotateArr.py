#1 O(N*K) times nd O(1) space

# def rotateOnce(arr,n):
#     temp=arr[n-1]
#     for i in range(n-2,-1,-1):
#         arr[i+1]=arr[i]
#     arr[0]=temp

# def rightrotate(arr,k):
#     for i in range(k):
#         rotateOnce(arr,len(arr))
#     print(arr)

# # (N) time bt O(k) space
# def rightrotate(arr,n,k):
#     temp=[]
#     for i in range(n-k,n):
#         temp.append(arr[i])
#     print(temp)

#     for i in range(n-k-1,-1,-1):
#         arr[i+k]=arr[i]
#     for i in range(0,k):
#         arr[i]=temp[i]
#     print(arr)
# arr=[1,2,3,4,5,6,7]
# rightrotate(arr,len(arr),3)


# O(N) time and O(1) space 
def reverse(arr,start,end):
    i=start
    j=end
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1


def rotate(arr,k,n):
    reverse(arr,n-k,n-1)
    print(f"reverse last {k} items",arr)
    reverse(arr,0,n-k-1)
    print(f"reverse 0 to {k-1} items",arr)
    reverse(arr,0,n-1)
    print("after revrse whole arre:",arr)



arr=[1,2,3,4,5,6,7]
rotate(arr,3,len(arr))

def rotateArr(nums,k):
    n=len(nums)
    temp=[-1]*n
    for i in range(n):
        temp[(i+k)%n]=nums[i]
    
    for i in range(n):
        nums[i]=temp[i]
    print(nums)

arr=[1,2,3,4,5,6,7]
rotateArr(arr,3)



