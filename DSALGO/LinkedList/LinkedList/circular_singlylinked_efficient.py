class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CircularSLL:
    def __init__(self):
        self.last=None
    
    #O(1)
    def insert_at_begin(self,data):
        newNode=Node(data)
        # if list not empty
        if self.last!=None:
            first=self.last.next
            newNode.next=first
            self.last.next=newNode
        else:
            self.last=newNode
            self.last.next=self.last
    #O(1)
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.last!=None:
            first=self.last.next
            self.last.next=newNode
            newNode.next=first
            self.last=newNode  # update last node
        else:
            self.last=newNode
            self.last.next=self.last
    
    def display(self):
        if self.last!=None:
            current=self.last.next # start from first node
            while current.next!=self.last.next:
                print(f"{current.data}-> ",end="")
                current=current.next
            #print last node

            print(f"{current.data}->")
            print()
        else:
            print("List is empty")


csll=CircularSLL()
csll.insert_at_begin(20)
csll.insert_at_begin(10)
csll.insert_at_end(30)
csll.display()




