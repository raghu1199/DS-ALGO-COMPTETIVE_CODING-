def kthsmallest(arr,left,right,k):
    if left==right:
        return arr[left]
    pindex=partition(arr,left,right)

    count=pindex-left+1  # left=0 pindex 4 then current element count 4-0+1 =5th
    print(f"pindex:{pindex} left:{left} count={count}")
    print(f"pindex is:{pindex} ,count of left subarry elements {count}")
    if count==k:
        return arr[pindex]
    # if k=3rd and count 5 then our 3rd smallest will be in left subarryy
    # if k=4th and count 2 then our 4th smallest will be in right suarr and i will be 4-len(left) 4-2=2nd smallest 
    elif k<count:
        print(f'{k}th is smaller than leftarr elements count {count} so goin left')
        return kthsmallest(arr,left,pindex-1,k)
    else:
        print(f'{k}th is greater than leftarr elements count {count} so goin right')
        print(f"lookin for k-len(left): {k-count}th smallest")
        return kthsmallest(arr,pindex+1,right,k-count)

def partition(arr,start,end):
    pivot=arr[start]
    i=start
    for j in range(start+1,end+1):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
        
    # at end swap pivot with start
    arr[i],arr[start]=arr[start],arr[i]
    print(arr)
    return i

arr=[6,1,0,2,3,4,9,8,7,10,5]
print(kthsmallest(arr,0,10,9))