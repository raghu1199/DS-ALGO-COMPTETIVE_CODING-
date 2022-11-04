
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def pathsum(root,target,sum):
    if root is None:
        return False
    sum+=root.data
    if root.left==None and root.right==None:
        if target==sum:
            return True
    goleft=pathsum(root.left,target,sum)
    goright=pathsum(root.right,target,sum)
    if goleft or goright:
        return True
    
    sum-=root.data
    return False

a=Node(3)
a.left=Node(5)
a.left.left=Node(6)
a.left.right=Node(2)
a.left.right.left=Node(7)
a.right=Node(8)

print(pathsum(a,18,0))
