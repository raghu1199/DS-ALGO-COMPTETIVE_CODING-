
# you have to update other nodes as well where ith index included in their sum
def update(i,x):
    i+=1
    while i<=N:
        BIT[i]+=x
        i=i+(i & (-i))

# get val of ith indx nd then get val at parent(i) nd so on till you reach at i=0 
# since at i=0 nothing stored break
def getSum(i):
    ans=0
    i+=1
    while i>0:
        ans+=BIT[i]
        i=i-(i & (-i))
    return ans

def createBIT(arr,N):
    for k in range(0,N):
        update(k,arr[k])



# a=[1,2,3,4,5,6,7,8,9,10]
# N=len(a)
# BIT=[0]*(len(a)+1)
# print(len(BIT))

# createBIT(a,N)
# print(BIT)
# print(getSum(9))


# getinversions
def update(i,x):
    while i<=MAX:
        BIT[i]+=x
        i=i+(i & (-i))

def getSum(i):
    print("BIT in sum:",BIT," for i:",i)
    ans=0
    while i>0:
        ans+=BIT[i]
        print("i:",i," ans:",ans)
        i=i-(i & (-i))
    return ans

def getInversions(arr,MAX):
    cnt=0
    for i in range(0,len(arr)):
        cnt+=getSum(MAX)-getSum(arr[i])
        update(arr[i],1)

    return cnt


arr=[3,4,2,1]
MAX=4
BIT=[0]*(MAX+1)
print(getInversions(arr,MAX))
print(BIT)
