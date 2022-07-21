
import random

def partition_random(arr,start,end):
    randompivot=random.randrange(start,end)
    arr[start],arr[randompivot]=arr[randompivot],arr[start]
    pivot=arr[start]
    i=start
    for j in range(start+1,end+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[start],arr[i]=arr[i],arr[start]
    return i

def kthsmallest(arr,start,end,k):
    if start==end:
        return arr[start]
    pos=partition_random(arr,start,end)
    lcount=pos-start+1
    if lcount==k:
        return arr[pos]
    elif k<lcount:
        return kthsmallest(arr,start,pos-1,k)
    elif k>lcount:
        return kthsmallest(arr,pos+1,end,k-lcount)

#arr=[13,12,11,14,15,17,18,20,19,16]
arr=[9,1,0,2,3,4,6,8,7,10,5]
print(kthsmallest(arr,0,len(arr)-1,6))



