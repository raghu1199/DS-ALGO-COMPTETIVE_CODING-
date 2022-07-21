

def countsubarrwithtarget(arr,k):
    n=len(arr)
    freq={}
    freq[0]=1
    currentsum=0
    count=0
    for i in range(0,len(arr)):
        currentsum+=arr[i]
        val=currentsum-k
        if val in freq:
            count+=freq[val]

        freq[currentsum]=1+freq.get(currentsum,0)


    return count
    
arr=[3,4,7,2,-3,1,4,2]
print(countsubarrwithtarget(arr,7))
        







