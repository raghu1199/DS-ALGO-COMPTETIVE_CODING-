def kthSmallest(arr, l, r, k):
     
    # If k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
         
        # Number of elements in arr[l..r]
        n = r - l + 1
 
        # Divide arr[] in groups of size 5,
        # calculate median of every group
        # and store it in median[] array.
        median = []
 
        i = 0
        print(f"n:{n} n//5:{n//5}:")  # here if n//5 ->0 then 0<0 gives false
        while (i < n // 5):
            print("Inside while...")
            median.append(findMedian(arr, l + i * 5, 5))
            i += 1
 
        # For last group with less than 5 elements
        if (i * 5 < n):
            print("outside while inside if..")
            median.append(findMedian(arr, l + i * 5,
                                              n % 5))
            i += 1
 
        # Find median of all medians using recursive call.
        # If median[] has only one element, then no need
        # of recursive call
        print("i:",i,"median arr:",median)
        if i == 1:
            medOfMed = median[i - 1]
            print("medofMed in if:",medOfMed)
        else:
            print(" inside else finding kth:",i//2," in median arr")
            medOfMed = kthSmallest(median, 0,
                                   i - 1, i // 2)
            print("medofMed in else:",medOfMed)
 
        # Partition the array around a medOfMed
        # element and get position of pivot
        # element in sorted array
        print("before partition arr:",arr)
        pos = partition(arr, l, r, medOfMed)
        print("pindex was:",pos," after partition arr:",arr)
        count=pos-l+1
        # If position is same as k
        if (count==k):
            print(f"pindex-l:{pos-l} k-1:{k-1} so return arr[pindex]")
            return arr[pos]
        if (count > k ): # If position is more,
                              # recur for left subarray
            print(f"we need {k}th smallest and left subarr size:{pos-l+1} so going left")
            return kthSmallest(arr, l, pos - 1, k)
 
        # Else recur for right subarray
        print(f"we need {k}th smallest and left subarr size:{pos-l+1} so going RIGHT.")
        return kthSmallest(arr, pos + 1, r,
                           k - pos + l - 1)
 
    # If k is more than the number of
    # elements in the array
    return 999999999999
 
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
 
# It searches for x in arr[l..r], 
# and partitions the array around x.
def partition(arr, l, r, x):
    print("inside part before:",arr,"pivot:",x)
    for i in range(l, r+1):
        if arr[i] == x:
            arr[l],arr[i]=arr[i],arr[l]
            break
    print("inside parti after placing pivot as start:",arr)
    pivot = arr[l]
    i = l
    for j in range(l+1, r+1):
        if (arr[j] <= pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    # at end
    arr[i],arr[l]=arr[l],arr[i]
    print("inside part after parti:",arr,"pivot:",x)
    return i
 
# A simple function to find
# median of arr[] from index l to l+n
def findMedian(arr, l, n):
    lis = []
    for i in range(l, l + n):
        lis.append(arr[i])
         
    # Sort the array
    lis.sort()
 
    # Return the middle element
    return lis[n // 2]
 
# Driver Code
if __name__ == '__main__':
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 4
    print("K'th smallest element is",
    kthSmallest(arr, 0, n - 1, k))