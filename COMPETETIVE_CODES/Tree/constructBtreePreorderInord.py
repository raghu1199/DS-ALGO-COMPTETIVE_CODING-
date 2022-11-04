

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None


def construct(ino,pre,sin,endin):
    global hm,spre
    if sin>endin:
        return
    node=Node(pre[spre])
    idx=hm[pre[spre]]
    spre+=1
    if sin==endin:
        return node
    
    node.left=construct(ino,pre,sin,idx-1)
    node.right=construct(ino,pre,idx+1,endin)
    return node

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def buildTree(ino,pre,n):
    global hm,spre
    spre=0
    hm={}
    for i in range(len(ino)):
        hm[ino[i]]=i
    
    root=construct(ino,pre,0,n-1)
    inorder(root)


inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
buildTree(inOrder,preOrder,6)