
from dataclasses import dataclass


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def insertIterative(root,key):
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
    # now parent have parent node
    if key < parent.data:
        parent.left=Node(key)
    else:
        parent.right=Node(key)

    return root


def countNodes(root):
    current=root
    stack=[]
    count=0
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            count+=1
            print(current.data,"->",end="")
            current=current.right
        else:
            break # if stack is empty
    print()
    print("Total Nodes:",count)

def count(root):
    if root is None:
        return 0
    return 1+count(root.left)+count(root.right)



root=None
for key in [10,5,25,2,7,30]:
    root=insertIterative(root,key)

#countNodes(root)
print(count(root))


