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
while True:
    ch=int(input("1)push\t2)pop\t3)peek\n"))
    if ch==1:
        ele=int(input("Enter ele to be pushed on stack:"))
        s.push(ele)
    elif ch==2:
        ele=s.pop()
        if ele==-1:
            print("stack is empty")
        else:
            print("deleted ele from stack is:{}".format(ele))
    elif ch==3:
        ele=s.peek()
        if ele==-1:
            print("stack is empty")
        else:
            print("top of stack is:{}".format(ele))
    else:
        break
        
