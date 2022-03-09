
from curses.ascii import isalnum


class Conversion:
    def __init__(self):
        self.stack=[]
        self.postfix=[]
        self.precedence={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}

    def isEmpty(self):
        return True if self.stack==[] else False
    
    def push(self,exp):
        self.stack.append(exp)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

    def isTopGreaterOrEqual(self,exp):
        # if stack is empty nd trying to get self.top gives keyerror so return false so that
        #  while breaks nd just push exp only
        try:
            c=self.precedence[exp]
            stackTop=self.precedence[self.top()]
            return  True if stackTop>=c else False
        except KeyError:
            return False


    def infixTopostfix(self,myexp):
        for exp in myexp:
            if exp.isalnum():
                self.postfix.append(exp)

            elif exp=='(':
                self.push(exp)

            elif exp==')':
                x=self.pop()
                while x!='(':
                    self.postfix.append(x)
                    x=self.pop()
            else:
                while (not self.isEmpty() and self.isTopGreaterOrEqual(exp)):
                    x=self.pop()
                    self.postfix.append(x)
                self.push(exp)

        # if our myexp is ended nd stack still have operators in it
        while not self.isEmpty():
            self.postfix.append(self.pop())

        return "".join(self.postfix)

c=Conversion()
#exp1="(2*3+4*(5-6)"
exp2="a+(b-c)-d*((e-f)/g+h)"

result=c.infixTopostfix(exp2)
print(result)

