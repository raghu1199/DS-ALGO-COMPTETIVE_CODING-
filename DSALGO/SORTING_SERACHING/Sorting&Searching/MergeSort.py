def merge(arr,left,right):
    i,j,k=0,0,0
    
    while i< len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1

        # for remaining elements of in left subarr ,rightsubarr
    while i < len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1
    while j < len(right):
        arr[k]=right[j]
        j=j+1
        k=k+1



def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)


arr=[6,5,3,2,1,8,7,2,4]
mergeSort(arr)
print(arr)