class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CircularSLL:
    def __init__(self):
        self.head=None
    
    def insert_at_begin(self,data):
        newNode=Node(data)
        if self.head!=None:
            current=self.head
            while current.next!=self.head:   # dont use current.next!=None use current.next!=head
                current=current.next
            
            newNode.next=self.head
            current.next=newNode
            self.head=newNode
        else:
            print("List is empty inserting at begin")
            self.head=newNode
            self.head.next=self.head
            print(f"Inserted succsefully {self.head.data}")

    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head!=None:
            current=self.head
            while current.next!=self.head:
                current=current.next
            # last node found
            current.next=newNode
            newNode.next=self.head


    def delete(self,ele):
        if self.head!=None:
            if self.head.data==ele:
                current=self.head
                # get the last node pointer to update circular link
                while current.next!=self.head:
                    current=current.next
                temp=current.next # old head
                current.next=temp.next
                self.head=temp.next  # new head
                temp=None
                return
            # if head is not the first item to be deleted
            current=self.head
            while current.next!=self.head:
                if current.next.data==ele:
                    temp=current.next # this item have to be deleted
                    current.next=temp.next
                    temp=None
                    return
                #update current if not found
                current=current.next
            
            print("given ele not found in list")
        else:
            print("list is empty")

    
    def display(self):
        if self.head !=None:
            current=self.head
            while current.next!=self.head:
                print(f"{current.data}-> ",end="")
                current=current.next
            # print last node
            print(f"{current.data}->")
        else:
            print("List is empty")

csll=CircularSLL()
csll.insert_at_begin(30)
csll.insert_at_begin(20)
csll.insert_at_end(50)
csll.display()    
csll.delete(50)
csll.display()
