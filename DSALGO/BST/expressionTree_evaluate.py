class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
    
def eval(root):
    # if tree is empty
    if root is None:
        return 0
    # if leaf node then it is operand
    if root.left==None and root.right==None:
        return int(root.data)

    # non leaf node means it will be operator
    else:
        left=eval(root.left)
        right=eval(root.right)
        operator=root.data
        if operator=='+':
            return left + right
        elif operator=='-':
            return left - right
        elif operator=='*':
            return left * right
        elif operator=='/':
            return left / right
        elif operator=='^':
            return left ^ right

root=Node('*')
root.left=Node('+')
root.right=Node('*')
root.left.left=Node('2')
root.left.right=Node('3')

root.right.left=Node('4')
root.right.right=Node('-')
root.right.right.left=Node('6')
root.right.right.right=Node('4')

result=eval(root)
print(result)


            
            
