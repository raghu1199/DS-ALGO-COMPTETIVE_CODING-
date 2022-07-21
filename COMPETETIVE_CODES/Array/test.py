from collections import deque

# l=[1,2,3]
# r=[2,3,4]
# print(l+r)
# l=deque()
# r=deque()
# l.append(1)
# l.append(2)
# r.append(4)
# r.append(5)
# arr=list(l)+list(r)
# print(arr)
# st=[2,3,4,5]
# print(st[-1])

# from collections import deque
# # arr=[[1,2],[2,3]]
# # for i in range(len(arr)):
# #     s,e=arr[i]
# #     print(s,e)
# stack=deque()
# stack.appendleft([1,2])
# stack.appendleft([5,7])

# arr=[-1]*len(stack)
# i=len(arr)-1
# while stack:
#     arr[i]=stack.pop()
#     i-=1
# print(arr)

# arr=[None]*len(stack)
# for i in range(len(stack)-1,-1,-1):
#     arr[i]=stack[i]
# print(arr)


# # set is unmutable while list is mutable so u cant add list to set
# s=set()
# s.add((1,2))
# s.add((1,2))
# print(s)

# freq={1:3,2:2,3:1}
# l=[]
# for k,v in freq.items():
#     l.append([k,v])

# l.sort(key=lambda x:x[1])
# print(l)

# for i in range(0,):
#     print(i)

# l=[[-1]]*1

# print(l)

# s=" RACE A caR "
# s=s.lower()
# l="".join(s.split(" "))
# print(l)

# import random

# n=random.randrange(1,10)
# print(n)
# print(1//2)

# arr=[1,2,3]
# temp=[1,2,1]
# if arr==temp:
#     print("yes")
# else:
#     print("No")

# s="ABC"
# s1="".join(s)
# #s=['A',"B",'Z']
# s1=s.split(" ")
# print(s1)


# print(s)
def abc():
    #min=80
    print(min)

min=90
print(min)
abc()
for i in [1,2,3,4][::-1]:
    print(i)
arr=[1,2,3,4,5,6,7]
print(arr[2:5:1])

class tester:
    id=20
    def __init__(self,id) -> None:
        self.id=id
        id=="adasd"
temp=tester(12)
print(tester.id)