class Node:
    def __init__(self,key):
        self.key=key
        self.left=self.right=None

class BST:
    
    def insert(self,root,key):
        newNode=Node(key)
        # base case
        if root is None:
            return newNode
        if key < root.key:
            root.left=self.insert(root.left,key)
        elif key>=root.key:
            root.right=self.insert(root.right,key)

        return root  # maintain links recursively
    
    def minvalue(self,root):
        current=root
        while current.left!=None:
            current=current.left
        return current

    # min ele in root.right subtree
    def inorderSuccessor(self,root):
        return self.minvalue(root.right)


    
    def delete(self,root,key):
        if root is None:
            print("Bst is empty .")
            return
        # find the given key if key==root.key it will go to else
        if key<root.key:
            root.left=self.delete(root.left,key)
        elif key> root.key:
            root.right=self.delete(root.right,key)
        else:
            # case 1 if node is leaf node 
            if not root.left and not root.right:
                print("Deleting leaf node")
                del root
                return None
            # case 2 A:if node dont have right child(only have left )
            if not root.right:
                print("deleting node having left child only")
                temp=root.left
                del root
                return temp

            # case 2 B:if node dont have left child (only have right)
            elif not root.left:
                print("deleting node having RIght child only")
                temp=root.right
                del root
                return temp
            
            # case 3 if node have both left nd right child (1)find inorder succesor(node)->(2) replace with node
            # (3)del inorder succesor key in node's right subrree which results in eithr above case(one child or leaf node)
            else:
                print("Deleting node having 2 child")
                temp=self.inorderSuccessor(root)
                root.key=temp.key
                root.right=self.delete(root.right,temp.key)
        
        return root  # maintain links

    # left-root-right
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key,end=" ")
        self.inorder(root.right)

    # root-left-right
    def preorder(self,root):
        if root is None:
            return
        print(root.key,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # left-right-root
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key,end=" ")


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

b.inorder(root)
print()
b.delete(root,10)
print("**** after delete**")
b.inorder(root)
print()

    
    




