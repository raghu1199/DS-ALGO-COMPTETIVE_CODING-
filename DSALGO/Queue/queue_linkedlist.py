


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=self.rear=None
    
    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
    # insert at rear (At end) O(1) delete from begining(front)
    def Enqueue(self,ele):
        newNode=Node(ele)
        if self.rear!=None:
            self.rear.next=newNode
            self.rear=newNode
        else:
            self.rear=self.front=newNode   # queue is empty
    
    def Dequeue(self):
        if not self.isEmpty():
            data=self.front.data
            temp=self.front
            self.front=temp.next
            temp=None
            # only 1 ele 10->None so here after deque front will point to None while rear still points to 10
            #so make rear also point to None indiacting empty queue
            if self.front==None:
                self.rear=None
            return data
        else:
            print("Queue is empty")
            return

    def display(self):
        current=self.front
        print("front->",end="")
        while current!=None:
            print(current.data,"->",end="")
            current=current.next
        print("<-rear")

q=Queue()
q.Enqueue(5)
q.Enqueue(10)
q.display()
q.Enqueue(15)
q.display()
print(q.Dequeue())
q.display()
print(q.Dequeue())
q.display()
print(q.Dequeue())
q.display()
print(q.Dequeue())
q.display()

