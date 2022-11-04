from collections import deque
from email.errors import NonPrintableDefect
from os import preadv


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None

# data lost when you modify prev.right first then orignal right was gone
# def preorder(root,f):
#     global head,prev
#     if root is None:
#         return
#     if f==0:
#         f=1
#         print("first time")
#         head=root
#         prev=root
#     else:
#         temp=prev.right
#         prev.right=root
#         prev.left=None
#         prev=prev.right
        
#     preorder(root.left,f)
#     preorder(root.right,f)

# def solve(root):
#     global head,prev
#     head=None
#     prev=None
#     f=0
#     preorder(root,f)
#     return head

def binarytoll(root):
    if root is None:
        return
    q=deque()
    q.append(root)
    head=prev=None

    while True:
        nodecount=len(q)

        if nodecount==0:
            return head

        while nodecount>0:
            node=q.popleft()
            # if node is None:
            #     nodecount-=1
            #     continue
            if prev is None:
                head=prev=node
            else:
                prev.right=node
                prev.left=None
                prev=prev.right
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodecount-=1
    

        



def traverseLL(head):
    current=head
    while current!=None:
        print(current.data,end=" ")
        current=current.right


a=Node(10)
a.left=Node(12)
a.right=Node(14)
a.right.left=None
a.right.right=Node(15)
head=binarytoll(a)
traverseLL(head)