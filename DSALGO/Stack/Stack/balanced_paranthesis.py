class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return (self.stack==[])
    
    def push(self,ele):
        self.stack.append(ele)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s=Stack()

def checkBalancedParanthesis(myexp):
    balanced=None
    for exp in myexp:
        if exp == '{' or exp=='[' or exp=='(':
            s.push(exp)
            print(exp," pushed")
        elif exp=='}' or exp==']' or exp==')':
            popped=s.pop()
            print("popped ele:",popped)
            if exp=='}' and popped!='{':
                balanced=False
            elif exp==']' and popped!='[':
                balanced=False
            elif exp==')' and popped!=')':
                balanced=False
            else:
                balanced=True
    
    if balanced==True:
        print("It is Balanced")
    else:
        print("Unbalanced")

mystr="{[])}"
checkBalancedParanthesis(mystr)
