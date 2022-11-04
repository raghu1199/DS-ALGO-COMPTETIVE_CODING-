
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None
    
def isleaf(node):
    if node.left==None and node.right==None:
        return True

def isSumtree(root):
    if root==None or isleaf(root):
        return True
    lsum,rsum=0,0
    if isSumtree(root.left) and isSumtree(root.right):
        if root.left==None:
            lsum=0
        elif isleaf(root.left):
            lsum=root.left.data
        else:
            lsum=2*(root.left.data)
        if root.right==None:
            rsum=0
        elif isleaf(root.right):
            rsum=root.right.data
        else:
            rsum=2*(root.right.data)
        if root.data==(lsum+rsum):
            return True
        else:
            return False
    else:
        return False
        
a=Node(120)
a.left=Node(40)
a.left.left=Node(15)
a.left.right=Node(25)
a.right=Node(19)
a.right.right=Node(20)

print(isSumtree(a))

