from copy import deepcopy



class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def pathsum2(root,csum,arr,path):
    if root is None:
        return False
    csum+=root.data
    path.append(root.data)
    if root.left==None and root.right==None:
        cpath=deepcopy(path)
        arr.append([csum,cpath])

    goleft=pathsum(root.left,csum,arr,path)
    goright=pathsum(root.right,csum,arr,path)
    if goleft or goright:
        return True
    csum-=root.data
    path.pop()
    return False

def pathsum(root,csum):
    global maxsum
    if root is None:
        return False
    csum+=root.data
    if root.left==None and root.right==None:
        maxsum=max(csum,maxsum)
        print("maxsum is:",maxsum)
    
    goleft=pathsum(root.left,csum)
    goright=pathsum(root.right,csum)
    # if goleft or goright:
    #     return True
    csum-=root.data
    return False


a=Node(120)
a.left=Node(40)
a.left.left=Node(15)
a.left.right=Node(25)
a.right=Node(20)
a.right.right=Node(20)
path=[]
arr=[]
global maxsum
maxsum=0
csum=0
pathsum(a,csum)
print(maxsum)
# print(arr)
# arr.sort(key=lambda x:x[0])
# print(max(arr))