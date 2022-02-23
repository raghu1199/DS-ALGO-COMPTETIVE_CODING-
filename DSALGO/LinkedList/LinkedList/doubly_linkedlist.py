class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode # declare new Node as head
    
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head!=None:
            current=self.head
            while current.next !=None:
                current=current.next
                
            current.next=newNode
            newNode.prev=current
        #if list is empty
        else:
            self.head=newNode
    
    def insert_at_position(self,data,position):
        newNode=Node(data)
        # first know th len of LL
        temp=self.head
        length=0
        while temp !=None:
            length+=1
            temp=temp.next
        if self.head!=None:
            if position!=1 and position<=length:
                index=1
                temp=current=self.head
                while index!=position:
                    index+=1
                    temp=current
                    current=current.next  # required postion element 
                
                newNode.next=current
                current.prev=newNode
                temp.next=newNode
                newNode.prev=temp
            elif position==1:
                # insert at begin
                self.insert_at_begining(data)
        else:
            self.head=newNode

    def reverse_traverse(self):
        current=self.head
        while current.next!=None:
            current=current.next
        # now currrent pointing to last node

        while current !=None:
            print(f"{current.data}-> ",end="")
            current=current.prev    
        #3-> 5-> 7-> 10-> 15-> so when at 5.prev!=None so cur=5.prev=3
        # now 3.prev ==none so while not executes then it not prints 3 so change while condi to current!=None
        # from checking current.prev!=None

        print()

    def delete(self,ele):
        if self.head.next==None:
            if self.head.data==ele:
                self.head=None
                print("Only 1 ele was there and it was deleted")
                return
        elif (self.head.data==ele and self.head.next!=None):
            temp=self.head
            self.head=temp.next
            self.head.prev=None
            temp=None # delete first node(prev head) 
            print("deleted head node(first node) in presence of other nodes")
            return
        # delete in between 
        else:
            temp=self.head
            while temp.next!=None:
                if temp.data==ele:
                    (temp.prev).next=temp.next
                    (temp.next).prev=temp.prev
                    temp=None
                    print("deleted in between node")
                    return
                temp=temp.next
            # if node not found in while traverssal means it is last node
            if(temp.data==ele):
                (temp.prev).next=None # update last node's next as None
                temp=None
                print("deleted last node")
                return
            else:
                print("given ele not found in list.")



    def display(self):
        current=self.head
        while current!=None:
            print(f"{current.data}-> ",end="")
            current=current.next
        
        print()

        
dll=DoublyLinkedList()
dll.insert_at_begining(10)
dll.insert_at_begining(5)
dll.insert_at_end(15)
dll.display()
dll.insert_at_position(7,2)
dll.display()
dll.insert_at_position(3,1)
dll.display()
#dll.insert_at_position(10,1)
#dll.display()
#dll.reverse_traverse()
#dll.delete(3)
#dll.delete(15)
dll.delete(7)
dll.display()
