# how many numbers smaller than current number  for each number of arr
#
#Given the array nums, for each nums[i] find out how many numbers in the array 
#are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

def howmany(arr):
    smaller=[]
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[j]<arr[i]:
                count+=1
        smaller.append(count)
    print(smaller)

arr=[8,1,2,2,3]
#howmany(arr)
        
# o(nlogn) 
def howmany2(arr):
    temp=[]
    for ele in arr:
        temp.append(ele)
    print(temp)
    arr.sort()
    smaller=dict()
    for i in range(len(arr)):
        if arr[i] not in smaller:
            smaller[arr[i]]=i
    output=[]

    for i in range(len(temp)):
        output.append(smaller[temp[i]])
    
    print(output)

arr=[8,1,2,2,3]
howmany2(arr)
        


