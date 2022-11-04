

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

from collections import deque
from copy import deepcopy


def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    root.left,root.right=root.right,root.left
    

# bfs based (level order)
def mirrorTree(r):
    root=deepcopy(r)
    if root is None:
        return 
    q=deque()
    q.append(root)
    while True:
        nodecount=len(q)
        if nodecount==0:
            return root
        while nodecount>0:

            node=q.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


a=Node(1)
a.left=Node(2)
a.right=Node(3)
a.left.left=Node(4)
a.right.left=Node(5)
a.right.right=Node(6)
a.left.left.left=Node(7)
a.left.left.right=Node(8)
inorder(a)
root=mirrorTree(a)
print()
inorder(root)

mirror(a)
print()
inorder(a)


