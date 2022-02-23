
def CountingSort(arr,place):
    n=len(arr)
    count=[0]*10
    result=[0]*n

    for i in range(n):
        index=arr[i]//place
        count[index%10]+=1
    # cumulative sum
    for i in range(1,10):
        count[i]+=count[i-1]
    # place elements in sorted oreder
    i=n-1
    while i>=0:
        index=arr[i]//place
        result[count[index%10]-1]=arr[i]
        count[index%10]-=1
        i-=1
    
    for i in range(n):
        arr[i]=result[i]
    print("Based on ",place ," digit:",arr)


def radixSort(arr):
    max_element=max(arr)
    place=1
    while max_element //place >0:
        CountingSort(arr,place)
        place*=10

arr=[121,432,564,23,1,45,788]
radixSort(arr)
print(arr)