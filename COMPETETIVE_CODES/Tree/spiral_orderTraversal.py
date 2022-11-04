
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


from collections import deque
def spiraltraversal(root):
    q1=deque()
    q2=deque()
    q1.append(root)
    left=False
    res=[]
    if root is None:
        return res
    while True:
        if len(q1)==0 and len(q2)==0:
            return res
        
        if left==False:
            nodecount=len(q1)
            out=[]
            for node in list(q1):
                out.append(node.data)
            res.append(out)

        elif left==True:
            nodecount=len(q2)
            out=[]
            for node in list(q2):
                out.append(node.data)
            res.append(out)

        
        

        while nodecount>0:
            if left==False:
                node=q1.pop()
                if node is None:
                    nodecount-=1
                    continue
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)    
                nodecount-=1

            if left==True:
                node=q2.pop()
                if node is None:
                    nodecount-=1
                    continue
                if node.right:
                    q1.append(node.right)
                if node.left:
                    q1.append(node.left)
                nodecount-=1

        if left==False:
            left=True
        else:
            left=False

root=None
# for key in [50,20,60,10,40,55,65,5,11,35,42]:
#     root=insert(root,key)
for key in [3,9,20,15,17]:
    root=insert(root,key)

print(spiraltraversal(root))
            


