from locale import currency


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CircularQueue:
    def __init__(self):
        self.front=self.rear=None
    
    #insert at rear(end side)
    def enQueue(self,ele):
        newNode=Node(ele)
        #if it is first ele
        if self.front==None:
            self.front=self.rear=newNode
            self.rear.next=self.front # make it circular  
        # if it contains elemts
        else:
            self.rear.next=newNode
            self.rear=newNode
            self.rear.next=self.front
    # delete from begining front
    def deQueue(self):
        #if empty
        if self.front==None:
            print("Q is Empty")
            return 
        temp=self.front
        data=self.front.data
        # if only one ele nd it have to be deleted
        if self.front==self.rear:
            self.front=self.rear=None
            temp=None
            return data
        else:
            self.front=temp.next  # (self.front).next
            self.rear.next=self.front  # make circular link update as front is changed
            temp=None
        return data
    
    def display(self):
        if self.front!=None:
            current=self.front
            print("front->",end="")
            while current.next!=self.front:
                print(current.data,"->",end=" ")
                current=current.next
            print(current.data,"<-rear")
        else:
            print("Q is empty now")

q=CircularQueue()
q.enQueue(5)
q.enQueue(10)
q.display()
q.enQueue(15)
q.display()
print("****")
q.deQueue()
q.display()
q.deQueue()
q.display()
q.deQueue()
q.display()
