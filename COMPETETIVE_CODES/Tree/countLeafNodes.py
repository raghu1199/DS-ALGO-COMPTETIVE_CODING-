
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None
    
def insert(root,key):
    current=root
    parent=None
    if root is None:
        return Node(key)

    while current!=None:
        parent=current
        if key < current.data:
            current=current.left
        elif key>=current.data:
            current=current.right
    
    if key < parent.data:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    
    return root




def lcount(root):
    if root is None:return 0
    if root.left==None and root.right==None:
        return 1
    else:
        return lcount(root.left)+lcount(root.right)

def lcountIterative(root):
    if root is None:
        return 0
    lcount=0
    current=root
    stack=[]
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            if current.left==None and current.right==None:
                lcount+=1
                current=None
            else:
                current=current.right
        else:
            break
    return lcount
        

root=None
for key in [10,11,12,13,14]:
    root=insert(root,key)

print(lcount(root))
print(lcountIterative(root))