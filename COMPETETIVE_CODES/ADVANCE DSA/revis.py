


# def update(idx,val):
#     idx+=1
#     while idx<=N:
#         BIT[idx]+=val
#         idx=idx + (idx & -idx)

# # takes original arr idx  sum 0 to 3 idx in original 1+2+3+4=10 so pass idx 3
# def getsum(idx):
#     ans=0
#     i+=1
#     while idx>0:
#         ans+=BIT[idx]
#         idx=idx-(idx & -idx)
#     return ans


# def createBit(arr):
    
#     for i in range(0,n):
#         update(i,arr[i])



# arr=[1,2,3,4,5,6,7,8]
# n=len(arr)
# N=n+1
# BIT=[0]*(N+1)
# createBit(arr)
# print(BIT)
# print(getsum(3))

def update(idx,val):
    while idx<=MAX:
        BIT[idx]+=val
        idx=idx+(idx & -idx)


def getsum(idx):
    ans=0
    while idx>0:
        ans+=BIT[idx]
        idx=idx-(idx & -idx)
    return ans


def getinversions(arr,MAX):
    ans=[]
    for i in range(0,len(arr)):
        maxsum=getsum(MAX)
        cnt=getsum(arr[i]-1)
        ans.append(cnt)
        update(arr[i],1)
    return ans


arr=[2,3,3,4,6,5]
MAX=max(arr)
BIT=[0]*(MAX+1)
print(getinversions(arr,MAX))
