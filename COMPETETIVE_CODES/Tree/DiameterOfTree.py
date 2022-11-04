
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

# O(N^2)
def diameter(root):
    global maxd
    if root is None:
        return 0
    lst=height(root.left)
    rst=height(root.right)
    maxd=max(maxd,lst+rst)

    diameter(root.left)
    diameter(root.right)

def height2(root):
    global d
    if root is None:
        return 0
    lst=height2(root.left)
    rst=height2(root.right)
    d=max(d,lst+rst)
    return 1+max(lst,rst)


   
a=Node(120)
a.left=Node(40)
a.left.left=Node(15)
a.left.left.left=Node(16)
a.left.left.left.left=Node(18)
a.left.right=Node(25)
a.left.right.left=Node(23)
a.left.right.left.left=Node(24)
a.right=Node(20)

global d,maxd
maxd=0
d=0 
diameter(a)  
print(maxd)
#print(height2(a))
height2(a)
print(d)