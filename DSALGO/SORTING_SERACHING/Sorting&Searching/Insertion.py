def insertionsort(arr):
    for j in range(1,len(arr)): # run till 1 to n-1, arr  starts at 0
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
        
        arr[i+1]=key
        print("swap happened")
    
    print(arr)

insertionsort([1,2,3,4,5])

def insertionsort_Modify(arr):
    for j in range(1,len(arr)): # run till 1 to n-1, arr  starts at 0
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
        if arr[i+1]!=key:
            arr[i+1]=key
            print("swap happened")
    
    print(arr)

insertionsort_Modify([1,2,3,4,5]) 
