class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class BST:
    
    def insert(self,root,ele):
        newNode=Node(ele)
        if root is None:
            return newNode
        
        current=root
        parent=None
        while True:
            parent=current
            if current is not None:
                if ele < current.data:
                    current=current.left
                elif ele>= current.data:
                    current=current.right
            if current is None :
                break

        # compare with parent to make sure whether it go as left child or right child
        if ele<parent.data:
            parent.left=Node(ele)
        elif ele>=parent.data:
            parent.right=Node(ele)
        
        return root

    # root-left-right
    def preorder(self,root):
        if root is None:
            return
        stack=[]
        current=root
        stack.append(current)
        while stack:
            current=stack.pop()
            print(current.data,end=" ")
            # first push right then left so that next time in pop left come first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    # ROOT-LEFT-RIGHT 
    def postorder(self,root):
        if root is None:
            []
        current=root
        stack,result=[],[]
        stack.append(root)
        # root always printed last so put it first in stack so that it comes last
        while stack:
            current=stack.pop()
            result.append(current.data)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        return result[::-1]  # print top to bottom (reverse order)
    
    # LEFT-ROOT-RIGHT ( )
    def inorder(self,root):
        if root is None:
            return
        current=root
        stack=[]
        # first 1)go leftmost nd then if (2)no left print it then go right and  go (1) nd check 
        while True:
            # go leftmost
            if current is not None:
                stack.append(current)
                current=current.left
            # no more left so print root nd go right
            elif stack:
                current=stack.pop()
                print(current.data,end=" ")
                current=current.right
            else:
                break
    
    # LEFT=RIGHT-ROOT using (1 stack)
    def postorder2(self,root):
        if root is None:
            return
        stack=[]
        prev=None
        stack.append(root)
        while stack:
            current=stack[-1] # points to top of stack

            # case1 :if node's left subtree or right subtrree not have been visied
            if prev==None or prev.left==current or prev.right==current:
                # we have to go leftmost first so if else (either one case excuted)
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    # no left no right so process this data pop out from stack
                    print(current.data,end=" ")
                    stack.pop()

            # case 2:left subtree of current node has been processed
            elif prev==current.left:
                if current.right:
                    stack.append(current.right)
        
            # case 3:right subtree of current node has been processed (prev==current.right) means left nd 
            # right subtree both processed at his point so process the current node
            else:
                print(current.data,end=" ")
                stack.pop()

            prev=current






b=BST()
root =None
for key in [10,5,25,3,4,7,6,30]:
    root=b.insert(root,key)

#       10
#       /  \
#      5    25
#     /  \     \
#    3    7     30
#    \    /
#     4   6



#b.preorder(root)
# print()
print(b.postorder(root))
print()
# b.inorder(root)
# print()
b.postorder2(root)
print()


            

