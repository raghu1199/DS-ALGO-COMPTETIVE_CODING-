

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


def predecessor(root,x):
    pred=None
    while root!=None:
        if root.data<x:
            pred=root.data
            root=root.right
        else:
            root=root.left
    return pred


a=Node(10)
a.left=Node(2)
a.right=Node(18)
a.right.left=Node(16)
a.right.left.right=Node(17)
a.right.right=Node(20)
print(predecessor(a,18))
