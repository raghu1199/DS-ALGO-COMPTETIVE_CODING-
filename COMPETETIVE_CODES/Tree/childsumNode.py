
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def csum(root):
    if root is None:
        return 0
    l=csum(root.left)
    r=csum(root.right)
    v=root.data
    if l==0 and r==0:
        root.data=v
    else:
        root.data=l+r
    return l+r+v
    

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

a=Node(10)
a.left=Node(-1)
a.right=Node(3)
a.left.left=Node(4)
a.left.right=Node(5)
a.right.left=Node(-2)
root=csum(a)
inorder(a)
