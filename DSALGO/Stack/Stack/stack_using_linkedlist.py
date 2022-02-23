class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.top=None
    #O(1) insert at begin
    def push(self,ele):
        newNode=Node(ele)
        if self.top == None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
    #(1) delete from begin
    def pop(self):
        if self.top !=None:
            data=self.top.data
            temp=self.top
            self.top=temp.next
            temp=None
            return data
        else:
            return "satck is empty"
    
    def peek(self):
        if self.top!=None:
            data=self.top.data
            return data
        else:
            return "stack is empty"

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.pop())
s.push(50)
print(s.peek())