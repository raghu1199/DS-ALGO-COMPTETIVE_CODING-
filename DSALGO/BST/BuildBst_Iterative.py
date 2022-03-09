
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def insert(root,key):
    current=root
    parent=None
    if root==None:
        return Node(key)
        
    while current!=None:
        parent=current
        if key<current.data:
            current=current.left
        else:
            current=current.right
    # on updatetd parent
    if key<parent.data:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    
    return root

root=None
for key in [10,5,25,2,27,30]:
    root=insert(root,key)

inorder(root)

