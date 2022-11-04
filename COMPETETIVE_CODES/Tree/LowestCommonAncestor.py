
from collections import deque
from email.errors import NonPrintableDefect


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None
 

def findnode(root,key,path):
    if root is None:
        return root
    q=deque()
    q.append(root)

    while True:
        nodecount=len(q) 
        if nodecount==0:
            return False

        while nodecount>0:
            node=q.popleft()
            if node is None:
                nodecount-=1
                continue
            if node.data==key:
                path.append(node.data)
                return 
            if node.left:
                path.append(node.data)
                q.append(node.left)
            if node.right:
                path.append(node.data)
                q.append(node.right)
            nodecount-=1

a=Node(3)
a.left=Node(5)
a.right=Node(1)
a.left.left=Node(6)
a.left.right=Node(2)
a.right.left=Node(0)
a.right.right=Node(8)
a.left.left.left=None
a.left.left.right=None
a.left.right.left=Node(7)
a.left.right.right=Node(4)

path=[]
findnode(a,7,path)
print(path)
            

