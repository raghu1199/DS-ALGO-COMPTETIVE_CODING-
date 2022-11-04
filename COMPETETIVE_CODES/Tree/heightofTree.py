

from collections import deque


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


def height(root):
    if root is None:return 0
    else:
        return 1+max(height(root.left),height(root.right))

def heightIterative(root):
    if root is None:return 0

    q=deque()    # append right & pop from left for Queue, for stack appendleft and popleft
    q.append(root)
    height=0 
    while True:
        nodecount=len(q)   # if not 0 means we have another level to traverse
        if nodecount ==0:
            return height
        height+=1  # each level incre height by 1
        while nodecount>0:
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1
    






root=None
for key in [10,11,12,13,14]:
    root=insert(root,key)
print(height(root))
print(heightIterative(root))