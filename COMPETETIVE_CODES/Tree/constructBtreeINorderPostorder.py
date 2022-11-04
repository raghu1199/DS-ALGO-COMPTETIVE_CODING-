
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

def construct(ino,post,sin,endin):
    global endp,hm
    # base case for making none child
    if sin > endin:
        return None
    node=Node(post[endp])
    idx=hm[post[endp]] 
    endp-=1
    # base case if only 1 node in this case global endp must be reduce first then 1 node returned
    if sin==endin:
        return node
    
    # postorder so first go right nd then go left
    node.right=construct(ino,post,idx+1,endin)
    node.left=construct(ino,post,sin,idx-1)
    

    return node

# def search(ino,startin,endin,val):
#     print(f"searching {val}:",startin,endin)
#     i=0
#     for i in range(startin,endin+1):
#         if ino[i]==val:
#             break
#     return i
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

# ino=[4,8,2,5,1,6,3,7]
# post=[8,4,5,2,6,7,3,1]
ino=[2,1,8,5,9,4,7,6,10,3]
post=[2,8,9,5,7,10,6,4,3,1]
n=len(ino)
endp=n-1
hm={}
for i in range(len(ino)):
    hm[ino[i]]=i

root=construct(ino,post,0,n-1)

inorder(root)
