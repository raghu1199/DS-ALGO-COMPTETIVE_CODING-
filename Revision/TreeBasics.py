
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None


# left root right
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

from collections import deque
from locale import currency
def inorderIterative(root):
    if root is None:
        return
    stack=[]
    current=root
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()

def preorder(root):
    if root is None:
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def preorderIterative(root):
    if root is None:
        return
    stack=[]
    stack.append(root)
    while stack:
        current=stack.pop()
        print(current.data,end=" ")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print()

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

# left right root
def postorderIterative(root):
    if root is None:
        return
    stack,result=[],[]
    stack.append(root)
    while stack:
        current=stack.pop()
        result.append(current)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    while result:
        current=result.pop()
        print(current.data,end=" ")

# countNodes
def ncount(root):
    if root is None:
        return 0
    return 1+ncount(root.left)+ncount(root.right)

# count leaf nodes
def lcount(root):
    if root is None:
        return 0
    if root.left==None and root.right==None:
        return 1
    return lcount(root.left)+lcount(root.right)

# height 
def height(root):
    if root is None:
        return 0
    return 1+ max(height(root.left),height(root.right))

from collections import deque
def levelorderTraversal(root):
    if root is None:
        return 
    q=deque()
    q.append(root)
    res=[]
    while True:
        nodecount=len(q)
        if nodecount==0:
            return res
        while nodecount>0:
            node=q.popleft()
            #print(node.data,end=" ")
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1

def heightIterative(root):
    if root is None:
        return
    q=deque()
    q.append(root)
    height=0
    while True:
        nodecount=len(q)
        if nodecount==0:
            return height
        height+=1
        while nodecount>0:
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1
    
def isidentical(a,b):
    if a==None and b==None:
        return True
    if a!=None and b!=None:
        issamedata=(a.data==b.data)
        issameleft=isidentical(a.left,b.left)
        issameright=isidentical(a.right,b.right)
        return issamedata and issameleft and issameright

    return False

def isidentcialIterative(a,b):
    if a==None and b==None:
        return True
    if (a==None and b!=None) and (b==None and a!=None):
        return False
    q1=deque()
    q2=deque()
    q1.append(a)
    q2.append(b)

    while len(q1)>0 and len(q2)>0:
        n1=q1.popleft()
        n2=q2.popleft()
        if n1.data!=n2.data:
            return False
        if (n1.left and n2.left):
            q1.append(n1.left)
            q2.append(n2.left)

        elif (n1.left or n2.left):
            return False
        if (n1.right and n2.right):
            q1.append(n1.right)
            q2.append(n2.right)
        elif (n1.right or n2.right):
            return False
    return True

from copy import deepcopy
def spiralorder(root):
    if root is None:
        return 0
    q1=[]
    q2=[]
    res=[]
    q1.append(root)
    nodecount=0
    left=False

    while True:
        if len(q1)==0 and len(q2)==0:
            return res
        if left==False:
            nodecount=len(q1)
            out=[]
            for ele in q1:
                out.append(ele.data)
            res.append(out)
            #print("in left==False:",res)

        elif left==True:
            nodecount=len(q2)
            out=[]
            for ele in q2:
                out.append(ele.data)
            res.append(out)
            #print("in left==True:",res)
        
        while nodecount>0:
            # enque child left to right
            if left==False:
                node=q1.pop()
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                nodecount-=1

            elif left==True:
                node=q2.pop()
                if node.right:
                    q1.append(node.right)
                if node.left:
                    q1.append(node.left)
                nodecount-=1

        if left==False:
            left=True
        else:
            left=False
    return res










# a=Node(1)
# a.left=Node(2)
# b=Node(1)
# b.right=Node(2)
# print(isidentical(a,b))
# print(isidentcialIterative(a,b))


a=Node(10)
a.left=Node(5)
a.right=Node(30)
a.left.left=Node(40)
a.left.right=Node(50)
a.right.left=Node(60)
a.right.right=Node(70)
a.left.left.left=Node(80)
a.left.left.right=Node(90)
print(spiralorder(a))

# # print(ncount(a))
# # print(lcount(a))
# # print(height(a))
# print(levelorderTraversal(a))
# print(heightIterative(a))
# # inorder(a)
# # print()
# # inorderIterative(a)
# # preorder(a)
# # print()
# # preorderIterative(a)
# # print()
# # postorder(a)
# # print()
# # postorderIterative(a)