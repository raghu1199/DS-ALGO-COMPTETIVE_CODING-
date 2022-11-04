
from itertools import count


def subarrsumwithTarget(arr,target):
    n=len(arr)
    l,r=0,0
    csum=0
    while r<=n:
        while csum>target and l<r-1:
            csum-=arr[l]
            print("removing:",arr[l]," l:",l," csum:",csum)
            l+=1
        if csum==target:
            return (l,r-1)
        if r<n:   # bcz r==n is out of bound
            csum+=arr[r]
            print("adding with r:",r," arr[r]:",arr[r]," csum:",csum)
        r+=1

arr=[1,4,20,3,10,5]
print(subarrsumwithTarget(arr,15))

def maxsumsubarrkwindowsize(arr,k):
    wsum,res=0,0
    for i in range(0,k):
        wsum+=arr[i]
    res=max(wsum,res)
    l=0
    for i in range(k,len(arr)):
        wsum-=arr[l]
        l+=1
        wsum+=arr[i]
        res=max(res,wsum)
    print(res)     


arr=[2,1,5,1,3,2]
maxsumsubarrkwindowsize(arr,3)

def countsubarrwithtargetsum(arr,target):
    freq={}
    freq[0]=1
    csum=0
    count=0
    for i in range(len(arr)):
        csum+=arr[i]
        diff=csum-target
        if diff in freq:
            count+=freq[diff]
        freq[csum]=1+freq.get(csum,0)
    return count

arr=[3,9,-2,4,1,-7,2,6,-5,8,-3,11,12]
print(countsubarrwithtargetsum(arr,5))

def twosumwithHash(arr,target):
    d={}
    for i in range(len(arr)):
        diff=target-arr[i]
        if diff in d:
            return f"indices:{d[diff]},{i} ele:{diff}+{arr[i]}={target}"
        d[arr[i]]=i

arr=[1,4,45,6,10,-8]
print(twosumwithHash(arr,37))


        


