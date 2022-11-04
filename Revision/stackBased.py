from collections import deque

def mergeOverlap(arr):
    arr.sort(key=lambda x:x[0])
    stack=deque()

    for Tj in arr:
        if not stack:
            stack.appendleft(Tj)
        si,ei=stack.popleft()
        sj,ej=Tj
        if ei>=sj:
            stack.appendleft([si,max(ei,ej)])
        else:
            stack.appendleft([si,ei])
            stack.appendleft(Tj)
    out=list(stack)
    return out[::-1]

arr=[[1,5],[8,9],[0,2],[6,10]]
print(mergeOverlap(arr))


        