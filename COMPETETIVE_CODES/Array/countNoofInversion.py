
def inversions(arr,start,end):
    if start>=end :
        return 0
    mid=(start+end)//2
    l=inversions(arr,start,mid)
    r=inversions(arr,mid+1,end)
    m=merge(arr,start,mid,end)

    return l+r+m

def merge(arr,start,mid,end):
    k,count,i,j=0,0,start,mid+1
    temp=arr[start:end+1]

    while i<=mid and j<=end:
        if arr[i]>arr[j]:
            count=count+(mid-i+1)
            temp[k]=arr[j]
            k+=1
            j+=1
        else:
            temp[k]=arr[i]
            i+=1
            k+=1
    
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=end:
        temp[k]=arr[j]
        k+=1
        j+=1

    arr=temp[start:end+1]
    return count

arr=[2,5,1,7,9]
arr1=[4,3,2,1]
arr2=[1,2,3,4]
print(inversions(arr2,0,3))