



class Heap:
    def __init__(self,size):
        self.heap=[0]*size
        self.heapSize=0
    
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]

    def heapifyBottomUp(self,index):
        parent=(index-1)//2
        # checking we are not comparing root vs root (index =0) then no need to do heapify
        if index>0 and self.heap[index]>self.heap[parent]:
            self.swap(index,parent)
            self.heapifyBottomUp(parent)
                
    def heapifyTopDown(self,index):
        # assume lasrgest is given nodes's index then find left and right child index of given node index
        largest=index
        left=2*index+1
        right=2*index+2

        if left<self.heapSize and self.heap[left]>self.heap[largest]:
            largest=left
        if right<self.heapSize and self.heap[right]>self.heap[largest]:
            largest=right

        if largest!=index:
            self.swap(index,largest)
            self.heapifyTopDown(largest)


    def insert(self,item):
        # insert on next avail place
        self.heap[self.heapSize]=item
        self.heapSize+=1
        # heapify on lastly inserted ele position heapsize-1 
        self.heapifyBottomUp(self.heapSize-1)
        #print(f"Given ele {item} inserted succesully nd BottomUp violation handlend..")
    
    def ExtractMax(self):
        max=self.heap[0]
        # swap root to last index nd reduce heap size by 1 (ignoring last ele= swapped root ele)
        self.swap(0,self.heapSize-1)
        self.heapSize-=1
        self.heap.remove(max)
        # heapify on root bcz we have place new ele at root
        self.heapifyTopDown(0)
        return max
    
    # extract max n times (till size of heap) n*logn
    def heapSort(self):
        result=[]
        for i in range(0,self.heapSize):
            max=self.ExtractMax()
            result.append(max)
        
        print(result[::-1])
    
    def displayHeap(self):
        if self.heapSize>0:
            for i in range(self.heapSize):
                print(self.heap[i],end=" ")
            print()
        else:
            print("Heap is empty")
            



# h=Heap(10)
# for num in [4,1,3,2,16,9,10,14,8]:
#     h.insert(num)
# h.displayHeap()
# print(h.ExtractMax())
# h.displayHeap()
# h.heapSort()
# h.displayHeap()