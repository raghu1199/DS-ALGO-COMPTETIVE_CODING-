def arrbyparity(arr):
    n=len(arr)
    odd=[]
    even=[]
    for i in range(n):
        if arr[i]%2!=0:
            odd.append(arr[i])
        else:
            even.append(arr[i])
    arr=even+odd
    print(arr)

arr=[3,1,2,4]
arrbyparity(arr)

#o(n) time and o(1) space
def sortybyparity(arr):
    n=len(arr)
    i=0
    j=n-1
    while i<j:
        if arr[i]%2!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
        else:
            i+=1
    print(arr)

arr=[3,1,2,4]
sortybyparity(arr)