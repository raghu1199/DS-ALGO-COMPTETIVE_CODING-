class CircularQueue:
    def __init__(self,size):
        self.N=size
        self.Q=[None]*size
        self.front=self.rear=-1
    
    def Enqueue(self,ele):
        # if first ele to be inserted before this q was empty
        if self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.Q[self.rear]=ele

        # if queue is full
        elif ((self.rear+1)%self.N==self.front):
            print("Queue is full right Now.")
            return
        else:
            self.rear=(self.rear+1)%self.N
            self.Q[self.rear]=ele
    
    def Dequeue(self):
        #if queue is empty
        if self.front==-1 and self.rear==-1:
            print("Queue is Empty. cant deququ anything")
            return
        # last ele of queu is dequing
        elif self.front==self.rear:
            ele=self.Q[self.front]
            self.front=self.rear=-1
            
            print("That was last ele in Queue")
            return ele
        else:
            ele=self.Q[self.front]
            self.front=(self.front+1)%self.N
            return ele

    def display(self):
            for i,ele in enumerate(self.Q):
                if i==self.front:
                    print("front->",i,":",ele)
                elif i==self.rear:
                    print("rear->:",i,":",ele)
                else:
                    print(i,":",ele)
                

q=CircularQueue(6)
q.Enqueue(5)
q.Enqueue(10)
q.display()
# q.Enqueue(10)
# q.Enqueue(15)
# q.Enqueue(20)
# q.Enqueue(25)
# q.Enqueue(30)
# q.display()
# print("After all pos full trying to insert in queu")
# q.Enqueue(35)
# print("****")
# q.Dequeue()
# q.display()
# print("***Enququ after 1 slot empty")
# q.Enqueue(35)
# q.display()
# print("****")
# q.Dequeue()
# q.display()
# print("****")
# q.Dequeue()
# q.display()

# q.Enqueue(50)

# print("****After Enqueu")

# q.display()
# q.Enqueue(55)
# q.display()
