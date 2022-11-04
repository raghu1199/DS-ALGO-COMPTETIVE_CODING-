

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

def preorder(root):
    if root is None:
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def preorderIterative(root):
    stack=[]
    current=root
    stack.append(current)
    while stack:
        current=stack.pop()
        print(current.data,end=" ")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)




root=None
for key in [10,5,25,2,7,30]:
    root=insert(root,key)

preorderIterative(root)
print()
preorder(root)
