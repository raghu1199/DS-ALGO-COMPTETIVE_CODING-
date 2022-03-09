class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class stack:
    def __init__(self):
        self.top=None

    def push(self,ele):
        newNode=Node(ele)

        if self.top==None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
    
    def pop(self):
        if self.top!=None:
            temp=self.top
            self.top=temp.next
            ele=temp.data
            temp=None
            return ele
        else:
            return "Stack is empty"
    
s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
