
# O(N) time and )(N) space
def oddtimes(arr):
    freq=dict()
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    
    for key,val in freq.items():
        if val%2!=0:
            return key
            
arr=[1,2,3,2,3,1,3]
print(oddtimes(arr))


def oddtimes2(arr):
    num=arr[0]
    for i in range(1,len(arr)):
        num=num^arr[i]
    return num

           
arr=[1,2,3,2,3,1,3,3,5]
print(oddtimes2(arr))

