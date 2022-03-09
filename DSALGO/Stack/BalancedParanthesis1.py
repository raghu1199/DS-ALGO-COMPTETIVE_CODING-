
class stack:
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


def checkParanthesis(myexp):
    s=stack()
    balanced=False
    for exp in myexp:
        if exp=='{' or exp=='[' or exp=='(':
            s.push(exp)
        elif exp=='}' or exp==']' or exp==')':
            popped=s.pop()
            if exp=='}' and popped=='{':
                balanced=True
            elif exp==']' and popped=='[':
                balanced=True
            elif exp==')' and popped=='(':
                balanced=True
            else:
                balanced=False
                return False
    
    return True

isbal=checkParanthesis('[({})]')
if isbal:
    print("balanced")
else:
    print("Not balanced")