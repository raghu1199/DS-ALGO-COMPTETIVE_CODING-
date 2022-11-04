
def mergeoverlapinterval(arr):
    stack=[]
    for i in range(len(arr)):
        s2,e2=arr[i]
        if not stack:
            stack.append(arr[i])
        else:
            s1,e1=stack.pop(0)
            if s2<e1:
                e1=max(e1,e2)
                stack.append([s1,e1])
            else:
                stack.append([s1,e1])
                stack.append([s2,e2])
    print(stack)


arr=[[1,3],[8,10],[2,6],[15,18]]
mergeoverlapinterval(arr)
