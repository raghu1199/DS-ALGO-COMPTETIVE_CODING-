
# o(N^2)
def mergeoverlapInterval(arr:list):
    n=len(arr)
    output=[]
    i,j=0,0
    while i<n:
        s1,e1=arr[i]
        j=i+1
        while j<n:
            s2,e2=arr[j]
            if e1>=s2:
                e1=max(e1,e2)
                arr[i]=[s1,e1]
                arr.remove(arr[j])
                n=n-1
            j+=1
        i+=1

    print(arr)


# arr=[[0,2],[1,5],[6,10],[8,9]]
# mergeoverlapInterval(arr)

from collections import deque

def mergeoverlap2(arr:list):
    arr.sort(key=lambda x:x[0])
    print(arr)
    stack=deque()
    for j in range(len(arr)):
        s2,e2=arr[j]
        if not stack:
            stack.appendleft(arr[j])
        else:
            s1,e1=stack.popleft()
            if e1>=s2:
                e1=max(e1,e2)
                stack.appendleft([s1,e1])
            else:
                stack.appendleft([s1,e1])
                stack.appendleft([s2,e2])
    output=list(stack)
    print(output)
            
            



arr=[[0,2],[6,10],[1,5],[8,9]]
mergeoverlap2(arr)