
def rotateonce(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]                # arr[n-1]=arr[n-2]
    arr[0]=temp

def rotatektimes(arr,k):
    for i in range(k):
        rotateonce(arr)
arr=[1,2,3,4,5,6]
rotatektimes(arr,3)
print(arr)

def rotateEfficient(arr,k):
    n=len(arr)
    temp=[-1]*len(arr)
    for i in range(0,n):
        temp[(i+k)%n]=arr[i]

    for i in range(n):
        arr[i]=temp[i]

arr=[1,2,3,4,5,6]
rotateEfficient(arr,3)
print(arr)



