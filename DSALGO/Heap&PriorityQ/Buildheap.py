
def heapify(arr,size,i):
    # arr is index -0 based
    left=2*i+1
    right=2*i+2
    largest=i  # assume given node at ith index is largest initially

    if left<size and arr[left]>arr[largest]:
        largest=left
    if right<size and arr[right]>arr[largest]:
        largest=right
    
    if largest!=i: # if change in largest node index
        arr[i],arr[largest]=arr[largest],arr[i]  # after swap call heapify on swpped node here at index largest
        heapify(arr,size,largest)

def builMaxheap(arr,size):
    for i in range(size//2,-1,-1):
        heapify(arr,size,i)

def heapsort(arr):

    size=len(arr)
    builMaxheap(arr,size)

    for last in range(size-1,0,-1):
        # swap root with last
        arr[last],arr[0]=arr[0],arr[last]
        # here last as arrsize =size-1 now next time also its size decreased by 1,heapify 
        # on root index 0 everytime
        heapify(arr,last,0)

def heapifyBottomUp(arr,size,i):
    parent=(i-1)//2
    # arr start index is 0 if parent <0 then do not execute terminate
    if parent>=0:
        if arr[i]>arr[parent]:
            arr[i],arr[parent]=arr[parent],arr[i]
            heapifyBottomUp(arr,size,parent)

def insert(arr,ele):
    # inserts at next (last) avail place
    arr.append(ele)
    size=len(arr)
    heapifyBottomUp(arr,size,size-1)  # heapify at index last inserted ele

def ExtractMax(arr):
    size=len(arr)
    max=arr[0]
    # swap root (max ele) to last to remove it from heap
    arr[size-1],arr[0]=arr[0],arr[size-1]
    arr.pop()  # removes last ele from heap
    heapify(arr,size-1,0)  # heapify on root
    return max







arr=[4,1,3,2,16,9,10,14,8,7]
print("before build heap:",arr)
builMaxheap(arr,len(arr))
print("After build heap:",arr)
insert(arr,17)
print("After insert 17 arr:",arr)
print(ExtractMax(arr))
print(arr)
# heapsort(arr)
# print("After heap sort:",arr)