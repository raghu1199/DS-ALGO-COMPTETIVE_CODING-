
#element is leader if it is greater than all elements of its right side
def findleaders(arr):
    leaders=[]
    for i in range(len(arr)):
        leader=True
        for j in range(i+1,len(arr)-1):
            if arr[i]<arr[j]:
                leader=False
                break
        if leader==True:
            leaders.append(arr[i])

    print(leaders)
arr=[8,4,2,3,1,5,4,2]
findleaders(arr)

def findleaders2(arr):
    leaders=[]
    largest=arr[len(arr)-1]
    leaders.append(largest)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>largest:
            leaders.append(arr[i])
            largest=arr[i]
    print(leaders)

arr=[8,4,2,3,1,5,4,2]
findleaders2(arr)
        
            



