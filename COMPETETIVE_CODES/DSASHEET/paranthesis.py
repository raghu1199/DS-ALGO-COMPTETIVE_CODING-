
# generate all valid paranthiss
from fileinput import close


def solve(openc,closec,ans,n):
    if openc==closec and openc==n:
        res.append("".join(ans))
        return
    if openc<n:
        ans.append("(")
        solve(openc+1,closec,ans,n)
        ans.pop()
    if closec<openc:
        ans.append(")")
        solve(openc,closec+1,ans,n)
        ans.pop()

res=[]
solve(0,0,[],3)
print(res)

# min no of swap to make string balanced (you can swap any two ele)
def minSwapAnySwap(Str):
    stack=[]
    cnt=0
    for ele in Str:
        if ele=='[':
            stack.append(ele)
        else:
            if len(stack)>0 and ele==']':
                stack.pop()
            else:
                cnt+=1
    
    return (cnt+1)//2

# Str="]]][[["
# Str="][]["
# print(minSwapAnySwap(Str))

def minSwapAdjacent(Str):
    openc=0
    closec=0
    unbalanced=0
    swap=0
    for c in Str:
        if c=='[':
            openc+=1
            if unbalanced!=0:
                swap+=unbalanced
                unbalanced-=1
        elif c==']':
            closec+=1
            unbalanced=closec-openc
    return swap

Str="[]]]][[][["
print(minSwapAdjacent(Str))