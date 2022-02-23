def partition(arr,start,end):
    pivot=arr[start]
    i=start
    for j in range(start+1,end+1):
        if arr[j] < pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    
    # at end
    arr[i],arr[start]=arr[start],arr[i]
    return i

def Quicksort(arr,start,end):
    if start<end:
        pindex=partition(arr,start,end)
        Quicksort(arr,start,pindex-1)
        Quicksort(arr,pindex+1,end)

arr=[6,10,13,5,8,3,2,11]
# as end give len(arr)-1 total len show 8 bt we need end index so give 7 
Quicksort(arr,0,7)
print(arr)