
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

s=stack()
ch=input("push\tpop\tpeek\texit\n")

while ch!='exit':
    if ch=='push':
        ele=int(input("enter ele"))
        s.push(ele)
    elif ch=='pop':
        ele=s.pop()
        if ele==-1:
            print("stack is empty")
        else:
            print(f"Deleted ele from stack is:{ele}")
    elif ch=='peek':
        ele=s.peek()
        if ele==-1:
            print("stack is empty")
        else:
            print("top of stack is {}".format(ele))
    else:
        print("Bad choice try again")
    ch=input("push\tpop\tpeek\texit\n")
