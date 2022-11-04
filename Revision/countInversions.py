
def inversions(arr,start,end):
    if start>=end:
        return 0
    mid=(start+end)//2
    l=inversions(arr,start,mid)
    r=inversions(arr,mid+1,end)
    m=merge(arr,start,end,mid)
    return l+r+m

def merge(arr,start,end,mid):
    i,k,j=start,start,mid+1
    cnt=0
    temp=[-1]*len(arr)
    print(f"merging:{arr[start:mid+1]},{arr[mid+1:end]}")

    while i<=mid and j<=end:
        if arr[i]>arr[j]:
            cnt+=(mid-i+1)
            temp[k]=arr[j]
            k+=1
            j+=1
        else:
            temp[k]=arr[i]
            k+=1
            i+=1
    
    while i<=mid:
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<=end:
        temp[k]=arr[j]
        k+=1
        j+=1

    for i in range(start,end+1):
        arr[i]=temp[i]
    print(f"for arr:{temp}:cnt:{cnt}")
    return cnt

#arr=[2,5,1,7,9]
arr=[4,3,2,1]
print(inversions(arr,0,len(arr)-1))
print(arr)

