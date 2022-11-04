from collections import deque


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def invertTree(root):
    if root is None:
        return root
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

a=Node(3)
a.left=Node(5)
a.left.left=Node(6)
a.left.right=Node(2)
a.left.right.left=Node(7)
a.right=Node(8)
inorder(a)
invertTree(a)
print()
inorder(a)

