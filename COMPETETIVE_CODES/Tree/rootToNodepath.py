


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def haspath(root,path,key):
    if root is  None:
        return False
    
    # push current node to path
    path.append(root.data)
    if root.data==key:
        return True
    
    # check if it lie in left or right if anyone side then return True 
    elif (haspath(root.left,path,key) or haspath(root.right,path,key)):
        return True
    
    # if not lies in left and right then pop current node which we have added recently
    path.pop(-1)
    return False


a=Node(3)
a.left=Node(5)
a.right=Node(1)
a.left.left=Node(6)
a.left.right=Node(2)
a.right.left=Node(0)
a.right.right=Node(8)
a.left.left.left=None
a.left.left.right=None
a.left.right.left=Node(7)
a.left.right.right=Node(4)

arr=[]
print(haspath(a,arr,7))
print(arr)