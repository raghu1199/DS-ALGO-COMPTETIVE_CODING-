from collections import deque

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

def levelorder(root):
    q=deque()
    q.append(root)
    res=[]
    while True:
        nodecount=len(q)

        if nodecount==0:
            return res
            
        clevelorder=list(q)
        out=[]
        for node in clevelorder:
            out.append(node.data)
        res.append(out)

        while nodecount >0:
            node=q.popleft()
            # binary tree can have null nodes
            if node is None:
                nodecount-=1
                continue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1

root=None
for key in [2,1,3]:
    root=insert(root,key)

print(levelorder(root))
        

            

    