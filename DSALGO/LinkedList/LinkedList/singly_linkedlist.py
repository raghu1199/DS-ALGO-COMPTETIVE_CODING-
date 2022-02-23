class Node:
    def __init__(self,data):
        self.data=data
        self.next=None  # defualt next is nUll

class LinkedList:
    def __init__(self):
        self.head=None
    
    #O(1)
    def insert_at_begining(self,data):
        newNode=Node(data)
        # if list is not empty
        if self.head !=None:
            newNode.next=self.head
            self.head=newNode
        # otherwise if list is empty
        else:
            self.head=newNode
    
    #O(N)
    def insert_at_end(self,data):
        newNode=Node(data)
        if self.head !=None:
            current=self.head
            while current.next!=None:
                current=current.next
            
            current.next=newNode
        else:
            self.head=newNode
    
    def insert_at_position(self,data,position):
        newNode=Node(data)
        #first  know len of LL
        temp=self.head
        length=0
        while temp!=None:
            length+=1
            temp=temp.next
        
        #main logic
        prev=self.head
        current=self.head
        index=1
        if position!=1 and position <= length:
            while index!=position:
                prev=current
                current=current.next
                index+=1

            newNode.next=current
            prev.next=newNode
        elif position==1:
            newNode.next=self.head
            self.head=newNode
        else:
            print(f"Invalid Position beacuse len of LL is {length}")
    
    def delete(self,ele):
        if self.head==None:
            print("List is empty")
        # if first ele to be deleted
        if self.head.data==ele:
            temp=self.head
            self.head=temp.next
            temp=None
            print(f"{ele} deleted succfully from list")
            return  # end the func here bcauze ahead o(n) work happens

        # if ele is not first ele then traverse through list and find it then delete it
        # her 4->5->6 at 5 we can found that 6 have to be deleted
        current=self.head
        while current.next !=None:
            if current.next.data==ele:
                temp=current.next   # this is to be deleted
                current.next=temp.next
                temp=None
                print(f"{ele} deleted succfully from list")
                return
            current=current.next   
        print(f"given element {ele} not present in our list")
    
    def search(self,ele):
        if self.head==None:
            print("List is empty")
        current=self.head
        count=1
        while current!=None:   # dont use current.next!=None cond if last node data then it will fail to search
            if current.data==ele:
                print(f"element found at posi {count} in list")
            count+=1
            current=current.next
    \

    def display(self):
        current=self.head
        # dont miss first node print head node's data also thats why in while current.next not checked bt current is checked
        while current !=None:
            print(f"{current.data} ->",end="")
            current=current.next
        print()

sll=LinkedList()
sll.insert_at_begining(5)
sll.insert_at_begining(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_begining(2)
sll.insert_at_position(7,2)
sll.insert_at_position(100,1)
sll.insert_at_position(200,8)
sll.display()
sll.delete(300)
sll.delete(20)
sll.display()
sll.search(5)
sll.delete(30)
sll.display()
