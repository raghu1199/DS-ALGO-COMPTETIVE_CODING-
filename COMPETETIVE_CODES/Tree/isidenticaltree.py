
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



# not works for [1,2] and [1,None,2] list will have same data [1,2] so it will return true

# def inorder(root,tree):
#     if root is None:
#         return
#     inorder(root.left,tree)
#     tree.append(root.data)
#     inorder(root.right,tree)
    


# def isidentical(root1,root2):
#     tree1=[]
#     tree2=[]
#     inorder(root1,tree1)
#     inorder(root2,tree2)
#     if tree1==tree2:
#         print("identical..")
#     else:
#         print("diff")

from collections import deque
def same(r1,r2):
    if r1 is None and r2 is None:
        return True
    if r1 is not None and r2 is not None:
        issamedata=(r1.data==r2.data)
        issameleft=same(r1.left,r2.left)
        issameright=same(r1.right,r2.right)
        return issamedata and issameleft and issameright
    
    return False

def sametree(r1,r2):
    if r1==None and r2==None:
        return True
    if (r1==None and r2!=None ) or (r1!=None and r2==None):
        return False
    q1=deque()
    q2=deque()
    q1.append(r1)
    q2.append(r2)

    while (len(q1)>0 and len(q2)>0):
        n1=q1.popleft()
        n2=q2.popleft()
        if (n1.data!=n2.data):
            return False
        # enque left of both
        if (n1.left and n2.left):
            q1.append(n1.left)
            q2.append(n2.left)
        elif (n1.left or n2.left):  # if both not true means if one of is true so structure diff or both not
            return False               # if both not have left child none of case execute go to check right
        
        if (n1.right and n2.right):
            q1.append(n1.right)
            q2.append(n2.right)
        elif (n1.right or n2.right):
            return False
    
    return True


#[1,2] [1,None,2]
a=Node(1)
a.left=Node(2)
b=Node(1)
b.left=None
b.right=Node(2)
print(sametree(a,b))

# root1=None
# for key in [1,2]:
#     root1=insert(root1,key)

# root2=None
# for key in [1,2]:
#     root2=insert(root2,key)


