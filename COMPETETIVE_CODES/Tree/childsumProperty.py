
from collections import deque

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def childsum(root):
    q=deque()
    q.append(root)
    while True:
        nodecount=len(q)
        if nodecount==0:
            return True
        while nodecount > 0:
            node=q.popleft()
            sum=0
            if node.left:
                q.append(node.left)
                sum+=node.left.data
            else:
                sum+=0
            if node.right:
                q.append(node.right)
                sum+=node.right.data
            else:
                sum+=0
            if node.left is None and node.right is None:
                nodecount-=1
                continue
            if node.data==sum:
                nodecount-=1
                continue
            else:
                return False

a=Node(20)
a.left=Node(12)
a.right=Node(8)
a.left.left=Node(6)
a.left.right=Node(6)
a.right.left=Node(3)
a.right.right=Node(5)
a.right.right.left=None
a.right.right.right=Node(5)

print(childsum(a))


            