


def Twosum(arr,target):
    temp=[-1]*len(arr)
    for i in range(len(arr)):
        temp[i]=arr[i]
    temp.sort()
    l=0
    r=len(arr)-1
    while l<r:
        if temp[l]+temp[r]==target:
            f=temp[l]
            s=temp[r]
            break
        elif temp[l]+temp[r]<target:
            l=l+1
        elif temp[l]+temp[r]>target:
            r=r-1
    print(f,s)
    i=arr.index(f)

    for k in range(len(arr)):
        if arr[k]==s and k!=i:
            return [i,k]

def Twosum2(arr,target):
    d={}
    for i in range(len(arr)):
        temp=target-arr[i]
        if temp in d:
            return (i,d[temp])
        else:
            d[arr[i]]=i

# arr=[1,7,4,45,6,-8,10,12]
# print(Twosum(arr,4))
# print(Twosum2(arr,4))

def threesum(arr,target):
    arr.sort()
    l,r=0,0
    sol=set()
    for i in range(len(arr)):
        l=i+1
        r=len(arr)-1
        while l<r:
            sum=arr[i]+arr[l]+arr[r]
            if sum==target:
                sol.add((arr[i],arr[l],arr[r]))
                l+=1
                r-=1
            if sum>target:
                r-=1
            if sum<target:
                l+=1
    return sol

# arr=[-1,0,1,2,-1,-4]
# print(threesum(arr,0))


def sortbyevenodd(arr):
    even=[]
    odd=[]
    for ele in arr:
        if ele%2==0:
            even.append(ele)
        elif ele%2!=0:
            odd.append(ele)
    arr=even+odd
    return arr

# arr=[3,1,2,5,4]
# print(sortbyevenodd(arr))

# using two pointer inplace o(1) space
def sortevenoddTwopointer(arr):
    l,r=0,len(arr)-1
    while l<r:
        if arr[l]%2!=0:
            arr[l],arr[r]=arr[r],arr[l]
            r=r-1
        elif arr[l]%2==0:
            l=l+1
    return arr

def sortbyevenodd(arr):
    even=[]
    odd=[]
    for ele in arr:
        if ele%2==0:
            even.append(ele)
        elif ele%2!=0:
            odd.append(ele)
    arr=even+odd
    return arr

# arr=[3,1,2,5,4]
# print(sortbyevenodd(arr))
# arr=[3,1,2,5,4]
# print(sortevenoddTwopointer(arr))

def rotateright(arr,k):
    n=len(arr)
    temp=[-1]*n
    for i in range(n):
        temp[(i+k)%n]=arr[i]

    return temp

    # for i in range(n):
    #     arr[i]=temp[i]

def twosuminRotatedSortedArr(arr,target):
    #find rotation point
    # first rotate it to make it full sorted arr
    rpoint=-1
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            rpoint=i
    k=len(arr)-rpoint

    temp=rotateright(arr,k)
    print("after rotation:",temp)
    l,r=0,len(temp)-1
    fele,sele=0,0
    while l<r:
        sum=temp[l]+temp[r]
        if sum==target:
            fele=temp[l]
            sele=temp[r]
            break
        if sum>target:
            r-=1
        if sum<target:
            l+=1

    print(fele,sele)
    findex=arr.index(fele)
    sindex=-1
    for i in range(len(arr)):
        if arr[i]==sele and i!=findex:
            sindex=i
    return (findex,sindex)

# arr=[11,15,6,8,9,10]
# print(twosuminRotatedSortedArr(arr,20))

def searchInrotatedsortedarr(arr,target):
    l,r=0,0
    n=len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            r=i-1
            l=i
    print(l,r)
    while l!=r:
        if arr[l]==target:
            return l
        elif arr[r]==target:
            return r
        if arr[l]<target:
            print("l incremed",l)
            l=(l+1)%n
        else:
            print("r decre",r)
            r=(n+r-1)%n
    return -1

# arr=[11,15,6,8,9,10]
# print(searchInrotatedsortedarr(arr,15))

def Partitionequalsumsubset(arr):
    n=len(arr)
    totalsum=sum(arr[::1])
    if totalsum%2!=0:
        return False
    return isSubsetSum(arr,n,totalsum//2)

def isSubsetSum(arr,n,target):
    if target==0:
        return True
    if n==0 and target!=0:
        return False
    # item val greater than target skip item
    if target<arr[n-1]:
        return isSubsetSum(arr,n-1,target)
    else:
        include=isSubsetSum(arr,n-1,target-arr[n-1])
        exclude=isSubsetSum(arr,n-1,target)
        return include or exclude

# arr=[1,5,12,4]
# print(Partitionequalsumsubset(arr))


def Partitionequalsumsubset2(arr):
    n=len(arr)
    totalsum=sum(arr[::1])
    if totalsum%2!=0:
        return False
    return issubsetsumdp(arr,n,totalsum//2)


def issubsetsumdp(arr,n,target):
    s=[[False for i  in range(target+1)] for i in range(n+1)]
    for i in range(0,n+1):
        s[i][0]=True
    for j in range(1,target+1):
        s[0][j]=False
    
    for i in range(1,n+1):
        for j in range(1,target+1):
            if j<arr[i-1]:
                s[i][j]=s[i-1][j]
            if j>=arr[i-1]:
                s[i][j]=(s[i-1][j] or s[i-1][j-arr[i-1]])
    return s[n][target]


# arr=[1,5,11,5]
# print(Partitionequalsumsubset2(arr))

def containerWithMostWater(arr):
    l,r=0,len(arr)-1
    res=0
    while l<r:
        length=r-l
        if arr[l]<arr[r]:
            height=arr[l]
            l+=1
        elif arr[r]<arr[l]:
            height=arr[r]
            r-=1
        area=height*length
        res=max(area,res)

    return res

# arr=[1,8,6,2,5,7,3,4]
# print(containerWithMostWater(arr))

def bestTimetobuysellstock(arr):
    n=len(arr)
    l,r=0,1
    maxprofit=0
    while r<=n-1:
        profit=arr[r]-arr[l]
        maxprofit=max(profit,maxprofit)
        if profit<=0:
            l=r
            r+=1
        else:
            r+=1
    return maxprofit

# arr=[2,1,2,1,0,1,2]
# arr=[7,1,5,3,6,4]
# print(bestTimetobuysellstock(arr))

def minNoofJumps(arr):
    n=len(arr)
    l=0
    cnt=0
    while l<=n-1:
        jumps=arr[l]
        if jumps==1:
            l+=1
            cnt+=1
            if l>=n-1:
                return cnt
            continue
        maxjump=max(arr[l+1:l+jumps+1])
        l+=maxjump
        cnt+=1
        if l>=n-1:
            return cnt+1
    return cnt

arr=[1,3,5,8,9,2,6,7,6,8,9]
arr=[1,1,1,1,1]
print(minNoofJumps(arr))




        
        





    
    




    


