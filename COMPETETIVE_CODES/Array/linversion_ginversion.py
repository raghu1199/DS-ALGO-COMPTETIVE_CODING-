

def inversions(arr,start,end,temp):
    if start>=end :
        return 0
    mid=(start+end)//2
    l=inversions(arr,start,mid,temp)
    r=inversions(arr,mid+1,end,temp)
    m=merge(arr,start,mid,end,temp)

    return l+r+m

def merge(arr,start,mid,end,temp):
    # k=start
    # i=start
    # j=mid+1
    # count=0
    k,count,i,j=start,0,start,mid+1
    
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
    
    for i in range(start,end+1):
        arr[i]=temp[i]
    #arr=temp[start:end+1]
    return count

def linversion(nums,start,end):
    count=0
    print("arr:",nums)
    print(end)
    if end>=2:
        print("inside end>2")
        for i in range(start,end-1,1):
            print(nums[i],nums[i+1])
            if nums[i]>nums[i+1]:
                count+=1
                print("inside if:",count)
        print("count:",count)
    elif end==2:
        if nums[0]>nums[1]:
            return 1
        else:
            return 0
    elif end==1:
        return 0
        
    return count

arr1=[1,0,2]
n=len(arr1)
temp=[None]*len(arr1)
#print(inversions(arr1,0,n-1,temp))
print(linversion(arr1,0,n))


            