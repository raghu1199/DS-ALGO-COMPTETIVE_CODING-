from re import S


class Heap:
    heapwasbuild=False

    def BuildHeap(self,arr,size):
        #ele stored in ip arr as CBT, start heapify from last internal node to root node
        # O(n)
        for currentEle in range(size//2,-1,-1):
            self.heapify(arr,size,currentEle)

        Heap.heapwasbuild=True

    def heapify(self,arr,size,i):
        # assume largest is given node index
        largest=i
        left=2*i+1
        right=2*i+2

        if left<size and arr[left]>arr[largest]:
            largest=left
        if right <size and arr[right]>arr[largest]:
            largest=right
        
        # swap with index of largest node(parent data goes to index of largest node)
        # largest index data goes to parent) and recursively heapify with swapped index here largest
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,size,largest)
    
    def ExtractMax(self,arr):
        size=len(arr)
        if Heap.heapwasbuild:
            max=arr[0]
            # swap root to last ele
            arr[0],arr[size-1]=arr[size-1],arr[0]
            # heapify considering last ele not partof heap anymore so size=size-1 nd heapify from root node
            arr.pop()
            self.heapify(arr,len(arr),0)
            return max   
        else:
            print("Heap was not build so Building Heap first...")
            self.BuildHeap(arr,len(arr))
            max=arr[0]
            # swap root to last ele
            arr[0],arr[size-1]=arr[size-1],arr[0]
            # heapify considering last ele not partof heap anymore so size=size-1 nd heapify from root node
            self.heapify(arr,size-1,0)
            return max   

    def HeapSort(self,arr):
        
        # first build heap
        if not Heap.heapwasbuild:
            print("Heap was not build so build it first...")
            self.BuildHeap(arr,len(arr))

            # go last index to root index each time decrese size by 1
            for last in range(len(arr)-1,0,-1):
                # swap root with last ele nd decrease arr size by 1 in heapify so that last ele
                # not become part of heapify
                arr[0],arr[last]=arr[last],arr[0]
                self.heapify(arr,last,0)
        else:
            # go last index to root index each time decrese size by 1
            for last in range(len(arr)-1,0,-1):
                # swap root with last ele nd decrease arr size by 1 in heapify so that last ele
                # not become part of heapify
                arr[0],arr[last]=arr[last],arr[0]
                self.heapify(arr,last,0)
        
    

h=Heap()
arr=[4,1,3,2,16,9,10,14,8,7]
print("before build heap:",arr)
h.BuildHeap(arr,len(arr))
print("After build heap:",arr)
# print(h.ExtractMax(arr))
# print("after extracted :",arr)
h.HeapSort(arr)
print(arr)

#print(h.ExtractMax(arr))

