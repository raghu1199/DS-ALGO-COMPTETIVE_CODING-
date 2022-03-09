


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:

    def insert(self,root,ele):
        if root==None:
            return Node(ele)
        if ele<root.data:
            root.left=self.insert(root.left,ele)
        elif ele>=root.data:
            root.right=self.insert(root.right,ele)
        
        return root # return current parent node to main caller each time
    
    def search(self,root,key):
        if root==None:
            return "Not Found"
        # if given key is found
        if root.data==key:
            return root.data
        if key<root.data:
            return self.search(root.left,key) # go for easrch in left subtree
        return self.search(root.right,key) # else go to right
    
    
    
    # Left-ROOt-RIGHT
    def inorder(self,root):
        if root==None:
            return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    # Root-left-Right
    def IterativePreorder(self,root):
        if root is None:
            return
        stack=[]
        stack.append(root)
        # push right first then push left so in next time in pop left comes out first root-left-right
        while stack:
            current=stack.pop()
            print(current.data,end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    # Left-Root-Right
    def IterativeInorder(self,root):
        if root is None:
            return
        stack=[]
        current=root
        while True:
            # first go to leftmost of current root, if leftmost is none then goto elif part
            # print root and then go to right side, nd in right side again go to leftmost first
            if current is not None:
                stack.append(current)
                current=current.left
            # print root go to right 
            elif stack:
                current=stack.pop()
                print(current.data,end=" ")
                current=current.right
    # LEFT-RIGHT-ROOT
    
    def IterativePostOrder(self,root):
        if root ==None:
            return []
        stack,result=[],[]
        stack.append(root)
        while stack:
            current=stack.pop()
            result.append(current.data)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        return result[::-1]

    #case1 prev is parent of cureent(prev==current.left or prev =current.right ) means we have not started our journey 
    # towards this node so go check if this node has left? if left push it stack nd keep going left(go leftmost)
    # if leftmost done go right. if no left nd no right then process current node
    #case 2: if current.left ==prev means we have processed left subtree of currrent so now check is any right
    #subtree? if then go 
    # case 3 : if current.right==prev means we have proccessed right cubtree of current means we already processed left
    #subtree so now process this current root
    # current always points to stack top nd prev points to last visited node(poped out from stack)
    def IterativePostOrder2(self,root):
        if root is None:
            return
        stack=[]
        prev=None
        stack.append(root)
        while stack:
            current=stack[-1] # get top of stack
            # case 1 you have to visit leftmost so use if elif case so that either one of is true each tiem
            if prev==None or prev.left==current or prev.right==current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    print(current.data,end=" ")
                    stack.pop()

            # case 2 left subtrre of node proceessed
            elif prev==current.left:
                if current.right:
                    stack.append(current.right)

            # case 3 prev==current.right
            else:
                print(current.data,end=" ")
                stack.pop()

            prev=current

    def minvalue(self,root):
        current=root
        while current.left!=None:
            current=current.left
        return current
    
    # min ele in right subtree of node
    def InorderSuccessor(self,node):
        return self.minvalue(node.right)
    # first find the ele if key<root.data case or elif key>root.data or in else it will go if key==root.data 
    # case 1: deleted node is leaf node
    # case 2: deleted node have one child(A: only leftchild,B:only rightchild)
    #case 3:deleted node have two child(use inorder succesor to replace nd delete inorder succesor in node's right subtrr)

    def delete(self,root,key):
        if root is None:
            print("BST is empty")
            return
        if key<root.data:
            root.left=self.delete(root.left,key)
        elif key>root.data:
            root.right=self.delete(root.right,key)
        # if key==root.data then we have found the key to be delete now go to check cases
        else:
            #case1 if node is leaf node
            if not root.left and not root.right:
                print("Deleting leaf node")
                del root
                return None
            # case 2 A:only have leftchild (no rightchild)
            if not root.right:
                print("deleting node having left child only")
                temp=root.left
                del root
                return temp
            # case 2 B: only have right child(no left)
            elif not root.left:
                print("deleting node having right child only")
                temp=root.right
                del root
                return temp
            # case 3 it have left child nd right child 
            else:
                print("Deleting node with 2 child")
                temp=self.InorderSuccessor(root) # min val in right subtree of root
                root.data=temp.data
                root.right=self.delete(root.right,temp.data) # delete the inorder succesor present in right subtree
                # uses any of above cases leaf node or 1 child node so no need to return here anythingf
        # recursively maintain link
        return root
    # iterative count nodes
    def count(self,root):
        if root is None:
            print("BST is empty")
            return 
        count=0
        current=root
        stack=[]
        while True:
            if current is not None:
                stack.append(current)
                current=current.left
            elif stack:
                current=stack.pop()
                count+=1
                print(current.data,end=" ")
                current=current.right
            else:
                break
        
        return count
    # recursive count
    def count2(self,root):
        # base case
        if root is None:
            return 0
        return 1+self.count2(root.left)+self.count2(root.right)
    # count leafnodes
    def leafcount(self,root):
        if root is None:
            return 0
        # if leaf retrun 1
        if root.left is None and root.right is None:
            return 1
        else:
            return self.leafcount(root.left)+self.leafcount(root.right)
    # get height
    def height(self,root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left),self.height(root.right))+1
    # get height iteratively
    def height2(self,root):
        stack=[]
        if root:
            stack.append((1,root))
        depth=0
        while stack:
            current_depth,root=stack.pop()
            if root is not None:
                depth=max(depth,current_depth)
                stack.append((current_depth+1,root.left))
                stack.append((current_depth+1,root.right))

        return depth
    




            

b=BST()
root=None
for ele in [10,5,25,3,4,7,6,30]:
    root=b.insert(root,ele)


#       10
#       /  \
#      5    25
#     /  \     \
#    3    7     30
#    \    /
#     4   6

b.inorder(root)
print()
print("********")
nodes=b.count(root)
print("Nodes are:",nodes)
print("uing recursive:")
print(b.count2(root))

print("leaf nodes:",b.leafcount(root))
print("height of tree is:",b.height(root))
print("height of tree is iteratively:",b.height2(root))
#b.delete(root,3) delete having right child only
#b.delete(root,7)  delete having left child only
# b.delete(root,10) # having 2 child
# b.inorder(root)
# print()


# print("PostOrder using 1 stack:")
# b.IterativePostOrder2(root)
# print()


# b.inorder(root)
# print()
# print(b.search(root,2))
# print(b.search(root,31))
# print(b.minvalue(root))
# print(b.InorderSuccessor(root))

# print("Preorder:")
# b.IterativePreorder(root)
# print()

# print("Inorder:")
# b.IterativeInorder(root)
# print()

# print("PostOrder using 2 stack:")
# result=b.IterativePostOrder(root)
# print(result)



