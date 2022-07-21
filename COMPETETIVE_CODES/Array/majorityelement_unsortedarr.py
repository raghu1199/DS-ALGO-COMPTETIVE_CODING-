
# O(N) time ans O(N) space
def findmajority(arr):
    freq=dict()
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    for key,val in freq.items():
        if val > len(arr)//2:
            return key

    return "No majority ele"

arr=[8,7,2,1,2]
print(findmajority(arr))

# O(N) time and O(1) space Boyer-moore algo fist find potential majority ele and then check for majority

def findmajority2(arr):
    count=0
    m=0
    for i in range(len(arr)):
        if count==0:
            m=arr[i]
            count+=1
        else:
            if arr[i]==m:
                count+=1
            else:
                count-=1
    mcount=0
    for num in arr:
        if m==num:
            mcount+=1
    if mcount>len(arr)//2:
        return m
    else:
        return "No majority ele"


arr=[8,7,2,1,2,2,2]
print(findmajority2(arr))
    
        

