
from audioop import reverse
from functools import cmp_to_key
from os import remove

# def mycmp(a,b):
#     print("a:",a," > ","b:",b)
#     if a>b:
#         return 1
#     elif a<b:
#         return -1
#     else:
#         print("both equal:")
#         return 0

# arr=[1,5,3,4,2]
# arr.sort(key=cmp_to_key(mycmp))
# print(arr)

def mycmp(x,y):
    xy=x+y
    yx=y+x
    if int(xy)>int(yx):
        return 1
    elif int(xy)<int(yx):
        return -1
    else:
        return 0

def formlargest(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    arr.sort(key=cmp_to_key(mycmp),reverse=True)
    #arr.reverse()
    print("".join(arr))

# arr=[3,30,34,9]
# formlargest(arr)

def removeKsmallestpossible(num,k):
    stack=[]
    # to handle 12405 k=5
    if len(num)==k:
        return '0'
    for c in num:
        while len(stack)>0 and (c < stack[-1] and k!=0):
            stack.pop()
            k-=1
            
        if c=='0' and k!=0:
            continue
        else:
            # not add leading zeros
            if c=='0' and len(stack)==0:
                continue
            stack.append(c)

    # to handle 1173 k=2 after remove 7 stack 113 so it will append 3 bt k!=0 yet so  
    # or to handle 1234 all asceding k=1 so above will not remove so this will remove 
    # nd delete last k digits      
    while len(stack)>0 and k!=0:
        stack.pop()
        k-=1
    
    if len(stack)==0:
        return '0'
    else:
        return "".join(stack)

# num=143016320
# print(removeKsmallestpossible(num,4))

from collections import defaultdict
def combinationSum(arr,target):
    hm={}
    #d=defaultdict(list)
    d={}
    for ele in arr:
        hm[ele]=True
    
    
    res=[]
    for ele in arr:
        k=target//ele
        while k!=0:
            a=ele*k
            diff=target-a
            
            #print("a:",a," diff:",diff)
            if diff==0:
                #print("appending:",[ele]*k)
                t=tuple([ele]*k)
                res.append(t)
                
            elif diff in hm:
                #print("appending hm:",([ele]*k)+[diff])
                t=tuple(([ele]*k)+[diff])
                res.append(t)
                d[ele]=diff
            k-=1
    
    #print(res)
    ans=set()
    for item in res:
        ans.add(item)
    print(ans)

#arr=[2,3,6,7]
#arr=[2,3,5]
arr=[2,7,6,3,5,1]

# combinationSum(arr,9)

# [[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2],[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],
# [1,1,1,6],
# [1,1,2,2,3],[1,1,2,5],[1,1,7],
# [1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]

# modify inplace
def removedupli(A):
    hm={}
    for ele in A:
        hm[ele]=False
    
    l=0
    for ele in A:
        if hm[ele]==False:
            A[l]=ele
            l+=1
            hm[ele]=True
    print(A)
    return l

# A=input().split(" ")
# print(len(A))
# print(removedupli(A))

# combination sum 1 all distict ele in input arr
# return all unique combination
def solve1(i,ans,csum,target,arr):
    if csum==target:
        res.append(ans.copy())
        return
    if i==len(arr) or csum>target:
        return
    
    ans.append(arr[i])
    solve(i+1,ans,csum+arr[i],target,arr)
    ans.pop()
    solve(i+1,ans,csum,target,arr)

# res=[]
# arr=[10,1,2,7,6,1,5]
# solve(0,[],0,8,arr)
# print(res)

# combination sum 2 ele of arr may not unique it contains repeated ele
# need all unique combinations

def solve(l,ans,csum,arr,target):
    if csum==target:
        res.append(ans.copy())
        return
    if l==len(arr) or csum>target:
        return
    
    prev=-1
    for i in range(l,len(arr)):
        if arr[i]==prev:
            continue
        ans.append(arr[i])
        solve(i+1,ans,csum+arr[i],arr,target)
        ans.pop()
        prev=arr[i]


    if csum==target:
        res.append(ans.copy())
        return
    if i==len(arr) or csum>target:
        return

    prev=-1
    for l in range(i,len(arr)):
        if arr[l]==prev:
            continue
        ans.append(arr[l])
        solve(l+1,ans,csum+arr[l],arr,target)
        ans.pop
        prev=arr[l]

# res=[]
# arr=[10,1,6,2,7,1]
# arr.sort()
# solve(0,[],0,arr,8)
# print(res)

# no f ways to delete 1 item to make arr sort

def makeArrsortByremoveOne(arr):
    n=len(arr)
    cnt=0
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            # cnt already 1 or 2 means 1 item alreday deleted so now impossible to make arr sort 
            # bcz we only have to delete 1 item
            if cnt!=0:
                return 0
            # try to remove left of i arr(i-1) or if i==1 and 9 5 8 so in this 9 must removed
            # 1 3 8 5 9
            if i==1 or arr[i-2]<=arr[i]:
                cnt+=1
            # try to delete ele itself 3 4 5 2 6
            if i==n-1 or arr[i-1]<=arr[i+1]:
                cnt+=1
            if cnt==0: #if sucjh pair exit nd we cant remove then impossile 2 2 1 1
                return 0
    # if no such pair exist means it already sorted order so u can remove any 1 item
    if cnt==0:
        return len(arr)
    else:
        return cnt

a=[3,4,5,4]
a=[1,2,3,4,5]
a=[2,2,1,1]
print(makeArrsortByremoveOne(a))


