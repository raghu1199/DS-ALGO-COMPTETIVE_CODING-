
from collections import deque


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def isIdentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1!=None and root2!=None:
        issamedata=(root1.data==root2.data)
        issameleft=isIdentical(root1.left,root2.left)
        issameright=isIdentical(root1.right,root2.right)
        return issamedata and issameleft and issameright
    else:
        return False

def isSame(root1,root2):
    if root1 is None and root2 is None:
        return True
    if (root1!=None and root2==None) or (root1==None and root2!=None):
        return False
    q1=deque()
    q2=deque()
    q1.append(root1)
    q2.append(root2)

    while len(q1)>0 and len(q2)>0:
        n1=q1.popleft()
        n2=q2.popleft()
        if n1.data!=n2.data:
            return False
        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
        elif (n1.left or n2.left):
            return False
        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)
        elif (n1.right or n2.right):
            return False
    return True


a=Node(1)
a.left=Node(2)
b=Node(1)
b.right=Node(2)
#print(isIdentical(a,b))
print(isSame(a,b))