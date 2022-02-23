class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SinlgyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        newNode=Node(data)
        if self.head!=None:
            newNode.next=self.head
            self.head=newNode
        else:
            self.head=newNode
    def display(self):
        if self.head!=None:
            current=self.head
            while current!=None:
                print(f"{current.data}-> ",end="")
                current=current.next
        else:
            print("List is empty")
        print()
    
    def reverse_the_list(self):
        prev=next=None
        if self.head!=None:
            current=self.head
            while current!=None:
                next=current.next
                current.next=prev
                prev=current
                current=next
                
            self.head=prev
        else:
            print("List is empty")


ll=SinlgyLinkedList()
ll.insert_at_begining(40)
ll.insert_at_begining(30)
ll.insert_at_begining(20)
ll.insert_at_begining(10)
ll.display()
ll.reverse_the_list()
ll.display()
