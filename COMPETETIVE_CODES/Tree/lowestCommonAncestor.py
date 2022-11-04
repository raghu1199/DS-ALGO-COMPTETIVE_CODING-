


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

# without extra space
def lca(root,x,y):
    if root is None:
        return
    if root.data > x  and root.data > y:
        return lca(root.left,x,y)
    elif root.data <x and root.data < y:
        return lca(root.right,x,y)
    else:
        return root.data  # found the least common ancestor



# def search(root,key,path):
#     if root is None:
#         return
#     if root.data==key:
#         path.append(root.data)
#         return 
#     if key < root.data:
#         path.append(root.data)
#         search(root.left,key,path)
#     elif key> root.data:
#         path.append(root.data)
#         search(root.right,key,path)
    

root=None
for key in [20,8,22,4,12,10,14]:
    root=insert(root,key)
print(lca(root,8,12))
# a=[]
# b=[]
# search(root,8,a)
# search(root,12,b)

# if len(a)>len(b):
#     small=len(b)
# else:
#     small=len(a)
# for i in range(small):
#     if a[i]==b[i]:
#         largest=i
#print(a[largest])







    









