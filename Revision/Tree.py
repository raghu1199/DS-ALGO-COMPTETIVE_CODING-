
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def insertLevel(arr,i,n):
    root =None
    if i<=n-1:
        if arr[i]==None:
            root=None
            return root
        else:
            root=Node(arr[i])
        root.left=insertLevel(arr,2*i+1,n)
        
        root.right=insertLevel(arr,2*i+2,n)

    return root

# left root right




def rootToNodePath(root,key,ans):
    if root==None:
        return False
    if root.data==key:
        print("found:",ans)
        for ele in ans:
            res.append(ele)
        return True
    
    ans.append(root.data)
    print("ans",ans)
    isinLeft=rootToNodePath(root.left,key,ans)
    isinRight=rootToNodePath(root.right,key,ans)

    if isinLeft or isinRight:
        return True
    ans.pop()
    print("On BackTrack:",ans)
    return False

def solve(root,ans):
    if root==None:
        return
    if root.left==None and root.right==None:
        ans.append(root.data)
        res.append(ans.copy())
        ans.pop()
        return
    ans.append(root.data)
    solve(root.left,ans)
    solve(root.right,ans)
    ans.pop()

from collections import deque
def levelorder(root):
    if root==None:
        return
    q=deque()
    q.append(root)
    while True:
        nodecount=len(q)
        if nodecount==0:
            return res
        while nodecount>0:
            node=q.popleft()
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1


height={}       
def h(root):
    if root==None:
        return
    elif root.left==None and root.right==None:
        print("its leaf:")
        height[root]=1
        print(root.data," h:",height[root])

    elif root.right==None:
        h(root.left)
        height[root]=height[root.left]+1
    
    elif root.right==None:
        h(root.left)
        height[root]=height[root.left]+1
    else:
        print("have both child or both have None:")
        h(root.left)
        h(root.right)
        height[root]=max(height[root.left],height[root.right])+1
        return
    
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    print("height:",height[root])
    inorder(root.right)


# arr=[1,2,3,4,5 ,8,None,None,None,6,7]
# arr=[1,2,3,4]
# root=insertLevel(arr,0,len(arr))
a=Node(5)
a.left=Node(10)
a.right=Node(30)
#a.left.left=Node(20)
h(a)
if a.right in height:
    print("yes")
else:
    print("no")
#inorder(a)

def maximumwidth(root):

