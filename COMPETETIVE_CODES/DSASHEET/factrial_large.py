
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
    

def multiply(tail,i):
    prevnode=temp=tail
    carry=0
    while temp!=None:
        data=temp.data*i+carry
        temp.data=data%10
        carry=data//10
        prevnode=temp
        temp=temp.prev
    
    while carry!=0:
        prevnode.prev=Node(carry%10)
        carry=carry//10
        prevnode=prevnode.prev
    
    return tail

def printres(tail):
    if tail is None:
        return
    printres(tail.prev)
    print(tail.data,end=" ")

def largeFact(num):
    tail=Node(1)
    root=None
    for i in range(2,num+1):
        root=multiply(tail,i)
    
    printres(root)

largeFact(5)

def multiply(stack,i):
    temp=stack.popleft()
    carry=0
    while temp!=None:
        data=temp*i+carry
        temp.appendleft(data%10)
        carry=data//10
        



def largefact2(num):

