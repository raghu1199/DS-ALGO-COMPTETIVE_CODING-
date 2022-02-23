def findMedian(arr,low,size):   # findMedian(arr,0,5)->arr[0:4]
    li=[]
    for i in range(low,low+size):
        li.append(arr[i])
    
    li.sort()
    return li[size//2]  # return 3rd element 

def partition(arr,low,right,x):
    # find  pivot elemnt and place it to start location
    for i in range(low,right+1):
        if arr[i]==x:
            arr[low],arr[i]=arr[i],arr[low]
            break
    pivot=arr[low]
    i=low
    for j in range(low+1,right+1):
        if arr[j]<=x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    # at end
    arr[low],arr[i]=arr[i],arr[low]
    return i

def kthSmallest(arr,low,right,k):
    if k>0 and k <= right-low+1:
        size=right-low+1

        # create chunks of size 5
        print(f"You are in kthsmallest whose arr is: {arr} ")
        median=[]
        i=0
        while(i<size//5):
            gmedain=findMedian(arr,low+i*5,5)
            median.append(gmedain)
            i+=1
        if(i*5<size):
            gmedain=findMedian(arr,low+i*5,n%5)
            median.append(gmedain)
            i+=1
        
        print(f"i:{i} and median arr:{median}")
        # find recursively median from median arr
        if i==1:
            medofMed=median[i-1] 
            print("medofMed in If:",medofMed)
        else:
            print(f"rceursively finding median in median arr looking for {i//2}th smallest in median arr")
            medofMed=kthSmallest(median,0,i-1,i//2)
            print(f"medofMed in else:{medofMed}")
        
        # partition aroun medofMed as pivot
        pindex=partition(arr,low,right,medofMed)
        count=pindex-low+1 # indicates no. of elements in left subarr

        if k==count:
            print(f"we need {k}th smallest and left has {count} elements so return arr[pindex] pivot is elemnt ")
            return arr[pindex]
        elif k < count:
            print(f"left subarr size {count} and we need {k}th smallest so going left..")
            return kthSmallest(arr,low,pindex-1,k)
        
        # if k>count k=5 and left subarr size 3 so recurse on right and look for 5-3(k-len(left))=2nd smallest 
        print(f"left subarr size {count} and we need {k}th smallest so going RIGHT..")
        return kthSmallest(arr,pindex+1,right,k-count)



arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 4
print("K'th smallest element is",
kthSmallest(arr, 0, n - 1, k))