
from heapq import heapify,heappop,heappush

def optimal_merge(files):
    heap=list(files)
    heapify(heap)
    print(heap)
    cost=0
    while len(heap)>1:
        f1=heappop(heap)
        f2=heappop(heap)
        f3=f1+f2
        cost+=f3
        heappush(heap,f3)

    #cost+=heappop(heap)
    return cost


files=[6,2,4,8,10]
print(optimal_merge(files))