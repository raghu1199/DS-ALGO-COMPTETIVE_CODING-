
def solve(i,ans,csum):
    if i>n-1 or csum>target:
        return
    if csum==target:
        res.append(ans.copy())
        return
    
    ans.append(arr[i])
    solve(i,ans,csum+arr[i])
    ans.pop()

    solve(i+1,ans,csum)

# target=8
# res=[]
# arr=[2,3,5]
# n=len(arr)
# solve(0,[],0)
# print(res)

def solve2(l,ans,csum):
    if csum==target:
        res.append(ans.copy())
        return
    if l==n or csum>target:
        return
    
    prev=-1
    for i in range(l,n):
        print("l:",l," prev:",prev)
        if arr[i]==prev:
            continue
        ans.append(arr[i])
        print("ans:",ans)
        solve2(i+1,ans,csum+arr[i])
        ans.pop()
        prev=arr[i]



target=4
res=[]
arr=[1,1,1,2,2]
n=len(arr)
solve2(0,[],0)
print(res)