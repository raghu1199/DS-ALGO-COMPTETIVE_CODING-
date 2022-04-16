class Node:
    # node with rooted height
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
        self.height=1

class AVLTREE:
    
    #      5(h=2) 1+max(1,1) , bal: (height(l)=1-height(r)=1) -> 1
    #     /       \
    #    4(h=1)    7(h=1) bal:(height(l)=0-height(r)=0)=0
    #   /           \
    #   None(h=0)    None(h=0)
        
    def getHeight(self,node):
        if node is None:
            return 0
        return node.height

    # get balance of node
    def getBalance(self,node):
        if node is None:
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)
    
    def rightRotate(self,node):
        t1=node.left
        t2=t1.right  # when t1 is root it's right child must go node.left
        # do right rotate
        t1.right=node
        node.left=t2
        # update heights
        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        t1.height=1+max(self.getHeight(t1.left),self.getHeight(t1.right))
        return t1
    
    def leftRotate(self,node):
        t1=node.right  # it is going to be root after rotate
        t2=t1.left
        # do left rotate
        t1.left=node
        node.right=t2
        # update height of t1(new root) nd node(old root)
        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        t1.height=1+max(self.getHeight(t1.left),self.getHeight(t1.right))
        return t1      # maintain link with parent node (return new root as t1)

        
    # time O(logN) nd space O(logN) due to recursive calls
    def insert(self,root,key):
        if root is None:
            return Node(key)
        
        if key< root.data:
            root.left=self.insert(root.left,key)
        elif key> root.data:
            root.right=self.insert(root.right,key)
        # from here it differs from normal BST
        # 1) for each time insert node find its height and update recursively after update height go (2)
        # (2) for each time you insert check balance nd do it recursively
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))

        # balance=hight(lst)-hieght(rst)
        balance=self.getBalance(root)

        # case 1: LL insertion(insertion on root's left child's left subtree) 
        # ->do right rotate  bal(3-1)=2 ,if current root is unbalanced
        if balance > 1 and key < root.left.data :
            return self.rightRotate(root)
        
        # LR insertion -> 1)leftrotate on root.left (2) rightrotate on root
        elif balance > 1 and key > root.left.data:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
            
        # case 2: RR insertion (insertion on root's right child's right subtree)
        # -> do left rotate bal(1-3)=-2 ,if current root is unbalanced
        elif balance < -1 and key > root.right.data:
            return self.leftRotate(root)
        
        # RL insertion (1) rotateright on root.right (2) rotateleft on root
        elif balance <-1 and key < root.right.data:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def minValue(self,root):
        current=root
        while current.left!=None:
            current=current.left
        return current


    
    # time O(logN) nd space O(logN) due to recursive calls
    def delete(self,root,key):
        if root is None:
            return None
        if key < root.data:
            root.left=self.delete(root.left,key)
        elif key > root.data:
            root.right=self.delete(root.right,key)
        # if key==root.data you found it
        else:
            # if it have only right child (no left child)
            if root.left is None:
                temp=root.right
                print("It had only right child")
                del root
                return temp
            # if it have only left child (no right child)
            elif root.right is None:
                temp=root.left
                print("it have only left child")
                del root
                return temp
            # if it have both left nd right child 
            else:
                print("Deleting node having two child")
                # find min ele in right subtree of root -> inorder successor
                temp=self.minValue(root.right)
                print("inorder succesor:",temp.data)
                root.data=temp.data
                # delete inorder sucessor ele from right subtree of root
                root.right=self.delete(root.right,temp.data)
        
        # update height nd balance factor of deleted node's parent node
        # if no ele remain so need to update height
        if root is None:
            return None
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)

        # case 1 if parent node unbalanced due to RR or RL case
        # 0-2 =-2 means rst have more ele
        if balance <-1:
            if self.getBalance(root.right)<=0:    # indicate RR case 
                self.leftRotate(root)
            # bala(root.right)>0 means RL case
            else:
                root.right=self.rightRotate(root.right)
                return self.leftRotate(root)
        
        # case 2 if parent node unbalanced due to LL or LR case
        # 2-0=2 means lst have more ele
        if balance > 1:
            if self.getBalance(root.left)>=0:   # indicate LL case
                self.rightRotate(root)
            # balance(root.left )<0 means LR case
            else:
                root.left=self.leftRotate(root.left)
                return self.rightRotate(root)
        
        return root # maintain link with parent nodes



    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    

a=AVLTREE()
root=None
for key in [21,26,30,9,4,14,28,18,15,10,2,3,7]:
    root=a.insert(root,key)

a.inorder(root)
print()
a.delete(root,21)
print("****After Delete 21*****")
a.inorder(root)
print()
        
