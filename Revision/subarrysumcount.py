from itertools import count


def subarrsum(arr,target):
    freq={}
    freq[0]=1
    csum=0
    count=0
    for i in range(len(arr)):
        csum+=arr[i]
        val=csum-target
        if val in freq:
            count+=freq[val]
        freq[csum]=1+freq.get(csum,0)
    return count

arr=[3,9,-2,4,1,-7,2,6,-5]
print(subarrsum(arr,5))