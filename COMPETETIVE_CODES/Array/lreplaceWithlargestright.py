

# Given an array arr, replace every element in that 
# array with the greatest element among the elements to its right, 
# and replace the last element with -1.


#O(N^2)
def largestright(arr):
    for i in range(len(arr)-1):
        largest=i+1
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[largest]:
                largest=j
        arr[i]=arr[largest]
    arr[len(arr)-1]=-1
    
    print(arr)

arr=[17,18,5,4,6,1]
largestright(arr)

def largestright2(arr):
    n=len(arr)
    largest=arr[n-1]
    arr[n-1]=-1
    for i in range(n-2,-1,-1):
        temp=arr[i]
        arr[i]=largest
        if temp>largest:
            largest=temp


arr=[17,18,5,4,6,1]
largestright2(arr)



