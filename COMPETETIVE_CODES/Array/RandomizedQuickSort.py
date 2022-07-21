import random

def randompivotPartition(arr,start,end):
    randompivot=random.randrange(start,end)
    print("pivot index is:",randompivot)
    # swap to randompivot to start position
    arr[start],arr[randompivot]=arr[randompivot],arr[start]
    return partition(arr,start,end)

def partition(arr,start,end):
    pivot=arr[start]
    i=start
    for j in range(start+1,end+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    # swap pivot to middle(appropriate location)
    arr[start],arr[i]=arr[i],arr[start]
    return i


def QuickSort(arr,start,end):
    if start<end:
        pindex=randompivotPartition(arr,start,end)
        QuickSort(arr,start,pindex-1)
        QuickSort(arr,pindex+1,end)

arr=[6,10,13,5,8,3,2,11]
QuickSort(arr,0,len(arr)-1)
print(arr)



