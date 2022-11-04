class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=self.right=None


def inorder(root):
    global prev,head
    if root is None:
        return 
    inorder(root.left)
    if prev==None:
        head=root
        prev=root
    else:
        prev.right=root
        prev.right.left=prev
        prev=prev.right
    inorder(root.right)

def BinaryToDLL(root):
    global prev,head
    prev=None
    head=None
    inorder(root)
    return head

def traverseDLL(head):
    if head is None:
        return
    current=head
    while current!=None:
        print(current.data,end=" ")
        current=current.right
    

a=Node(10)
a.left=Node(12)
a.right=Node(14)
head=BinaryToDLL(a)
traverseDLL(head)


