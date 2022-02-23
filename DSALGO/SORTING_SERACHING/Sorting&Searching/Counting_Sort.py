def countingSort(arr):
    n=len(arr)
    max_ele=max(arr)
    count=[0 for _ in range(max_ele+1)]  # count of size k(max_ele) alternate count=[0]*(max_ele+1)
    result=[0 for _ in range(n)] # result arr
    print(count,result)

    # store freq of each elemnt of inp in count arr
    for i in range(max_ele+1):
        count[arr[i]]+=1
    # store cumulative sum of count arr
    for i in range(0,max_ele+1):
        count[i]=count[i]+count[i-1]
    
    i=n-1
    while i>=0:
        result[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
        i=i-1

    return result

arr=[4,2,2,5,3,3,1]
print(countingSort(arr))