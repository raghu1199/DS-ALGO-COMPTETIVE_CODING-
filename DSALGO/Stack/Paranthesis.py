class Paranthesis:
    def __init__(self):
        self.stack=[]
    
    def check(self,exp):
        for i in range(len(exp)):
            if exp[i]=='{' or exp[i]=='[' or exp[i]=='(':
                self.stack.append(exp[i])
                continue
            if exp[i]==')':
                popped=self.stack.pop()
                if popped!='(':
                    return False
            if exp[i]=='}':
                popped=self.stack.pop()
                if popped!='{':
                    return False
            if exp[i]==']':
                popped=self.stack.pop()
                if popped!='[':
                    return False
        # if stack conatins something then it must be all open paranthesis so not balanced
        if len(self.stack):
            return False
        else:
            return True

p=Paranthesis()
if p.check("[{()}]"):
    print("Balanced")
else:
    print("not balanced")