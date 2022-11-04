
def kmostfrequent(arr,k):
    bucket=[[]for i in range(len(arr)+1)]
    freq={}
    for ele in arr:
        freq[ele]=1+freq.get(ele,0)
    
    for ele,count in freq.items():
        bucket[count].append(ele)
    
    print(bucket)
    res=[]
    # need k most frequent
    for cnt in range(len(bucket)-1,-1,-1):
        if bucket[cnt]!=[] and k!=0:
            bucket[cnt].sort()
            for ele in bucket[cnt]:
                res.append(ele)
                k-=1
                if k==0:
                    return res

# arr=[8,1,1,4,4,4,4,2,2,2,2,5,5,5]
# #arr.sort()
# print(kmostfrequent(arr,2))

def canureachtoend(arr):
    maxreachable=0
    for i in range(len(arr)):
        if i>maxreachable:
            return False
        maxreachable=max(maxreachable,i+arr[i])
    return True

# arr=[1,1,2,3,2,1,0,0,1,3]
# arr=[1,1,2,5,2,1,0,0,1,3]
# print(canureachtoend(arr))

from random import random

def minNoofJumpsDp(arr):
    dp=[sys.maxsize]*len(arr)
    dp[0]=0
    for i in range(0,len(arr)):
        for j in range(0,i):
            if i<=j+arr[j]:
                dp[i]=min(dp[i],dp[j]+1)
    print(dp)
    return dp[len(arr)-1]

# arr=[2,1,3,2,3]
# print(minNoofJumpsDp(arr))

def minNoofJumps(arr):
    n=len(arr)
    maxreach=0
    currend=0
    jumps=0
    for i in range(0,n):
        maxreach=max(maxreach,i+arr[i])
        if maxreach>=n-1:
            return jumps+1
        # if i==maxreach so our maxreachable is this i only we cant go further now nd we havnt reached end
        if i==maxreach:
            return -1
        # if our ladder end reaches we need to switch ladder
        if i==currend:
            jumps+=1
            currend=maxreach
    

# arr=[1,2,5,2,1,2,1,0]
# arr=[2,0,1,0,5]
# print(minNoofJumps(arr))
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]


import random
def partition(arr,start,end):
    rndm_idx=random.randrange(start,end)
    arr[start],arr[rndm_idx]=arr[rndm_idx],arr[start]
    pivot=arr[start]
    print("pivot:",pivot)
    i=start
    for j in range(start+1,end+1):
        if arr[j]<=pivot:
            i+=1
            swap(arr,i,j)
    
    swap(arr,i,start)
    return i

def kthsmallest(arr,start,end,k):
    print("start,end:",start,end)
    if start==end:
        return arr[start]
    pindx=partition(arr,start,end)
    print("pindx is:",pindx)
    lcount=pindx-start+1
    print("lclount:",lcount," k:",k)
    if k==lcount:
        return arr[pindx]
    elif k<lcount:
        print("going left:")
        return kthsmallest(arr,start,pindx,k)
    print("going right..to find:",k-lcount," th smallest")
    return kthsmallest(arr,pindx+1,end,k-lcount)

# arr=[9,1,0,2,3,4,6,8,7,10,5]
# print(kthsmallest(arr,0,len(arr)-1,6))

#a[i-1]<=a[i]=>a[i+1]
def wigglesort1(arr):
    n=len(arr)
    arr.sort()
    for i in range(1,n-1,2):
        swap(arr,i,i+1)
    # i=1
    # while i<=len(arr)-2:
    #     swap(arr,i,i+1)
    #     i+=2
    print(arr)

# arr=[3,5,1,6,2,4]
# wigglesort1(arr)

#a[i-1]<a[i]>a[i+1]
def wigglesort2(arr):
    n=len(arr)
    arr.sort()
    temp=[-1]*len(arr)

    i=1
    j=n-1
    while i<=n-1:
        temp[i]=arr[j]
        i+=2
        j-=1
    i=0
    while i<=n-1:
        temp[i]=arr[j]
        i+=2
        j-=1
    
    print(temp)

#arr=[1,5,1,2,6,4]
# wigglesort2(arr)
def wigglesort2Efficeient(arr):
    for i in range(0,len(arr)-1):
        if i%2==0 and not(arr[i]<arr[i+1]):
            swap(arr,i,i+1)
        if i%2!=0 and not (arr[i]>arr[i+1]):
            swap(arr,i,i+1)
    print(arr)

# arr=[1,5,1,2,6,4]
# arr=[3,5,1,6,4,2]
# wigglesort2Efficeient(arr)

def maxsumSubarr(arr):
    csum=arr[0]
    res=csum
    for i in range(1,len(arr)):
        csum+=arr[i]
        print(csum,arr[i])
        if arr[i]>csum:
            csum=arr[i]
        res=max(res,csum)
        
    return res

# arr=[-2,1,-3,4,-1,2,1,-5,4]
# print(maxsumSubarr(arr))
        

def maxProductsubarr(arr):
    ma=mi=arr[0]
    res=ma
    for i in range(1,len(arr)):
        if arr[i]<0:
            ma,mi=mi,ma
        ma=max(arr[i],ma*arr[i])
        mi=min(arr[i],mi*arr[i])
        res=max(res,ma)
    return res

# arr=[6,-3,-10,-2,2]
# print(maxProductsubarr(arr))
def nextgap(gap):
    if gap<=1:
        return 0
    return (gap//2)+(gap%2)

def swap(a,b,i,j):
    a[i],b[j]=b[j],a[i]

def mergeTwoSorted(a,b):
    n=len(a)
    m=len(b)
    gap=nextgap(m+n)
    while gap>0:

        # only in array a
        i=0
        print("gap is:",gap)
        while i+gap<n:
            if a[i]>a[i+gap]:
                swap(a,a,i,i+gap)
            i+=1
        # i+gap out of araay a, and goes to arr b
        # inside arr1 nd arr2
        j= gap-n if gap>n else 0
        while i<n and j<m:
            if a[i]>b[j]:
                swap(a,b,i,j)
            i+=1
            j+=1
        # arr1 ended now only elements in arr2
        if j<m:
            j=0
            while j+gap<m:
                if b[j]>b[j+gap]:
                    swap(b,b,j,j+gap)
                j+=1
        
        gap=nextgap(gap)
    print(a,b)

# a=[1,4,7,8,10]
# b=[2,3,9]
# mergeTwoSorted(a,b)

def buyndsellMultipleTimes(arr):
    n=len(arr)
    l,r=0,1
    res=[]
    prev=0
    while r<=n-1:
        profit=arr[r]-arr[l]
        if profit>prev:
            prev=profit
            if r==n-1:
                res.append([l,r])
        elif r-1!=l:
            res.append([l,r-1])
            prev=0
            l=r
        if profit<=0:
            prev=0
            l=r
        r+=1

    return res


# arr=[11,42,49,96,23,20,49,26,26,18,73,2]
# #arr=[1,2,3,4,5]
# print(buyndsellMultipleTimes(arr))

def allpairs(a,b,target):
    hm={}
    for ele in a:
        hm[ele]=True
    
    res=[]
    for ele in b:
        diff=target-ele
        if diff in hm:
            res.append([diff,ele])
    return res

# a=[1,2,4,7,5]
# b=[5,6,3,4,8]
# print(allpairs(a,b,9))


def findcommonin3(a,b,c):
    hm1={}
    for ele in a:
        hm1[ele]=False
    for ele in b:
        if ele in hm1:
            hm1[ele]=True
    res=[]
    for ele in c:
        if ele in hm1 and hm1[ele]==True:
            res.append(ele)
    return res

# a=[1,5,10,20,40,80]
# b=[6,7,20,80,100]
# c=[3,4,15,5,20,30,70,80,120]
# print(findcommonin3(a,b,c))

def alteranative(arr):
    neg=[]
    pos=[]
    for ele in arr:
        if ele<0:
            neg.append(ele)
        else:
            pos.append(ele)

    k,i,j=0,0,0
    waspos=False
    temp=[-1]*len(arr)
    while i<len(neg) and j <len(pos):
        if waspos==False:
            temp[k]=pos[j]
            j+=1
            k+=1
            waspos=True
        elif waspos==True:
            temp[k]=neg[i]
            i+=1
            k+=1
            waspos=False

    while i<len(neg):
        temp[k]=neg[i]
        i+=1
        k+=1
    while j <len(pos):
        temp[k]=pos[j]
        j+=1
        k+=1
    print(temp)

# a=[-5,5,2,4,-2,3,7,0,8,-9]
# alteranative(a)

def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

# o(NLOGN) O(1) space
def alternate(arr):
    arr.sort()
    pos=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos=i
            break
    neg=0
    wasPos=False
    while pos<=len(arr)-1:
        if wasPos==False:
            swap(arr,neg,pos)
            neg+=1
            pos+=1
            wasPos=True
        elif wasPos==True and arr[neg]<0:
            neg+=1
            wasPos=False
        else:
            break
    print(arr)

a=[-5,3,8,-2,4,9]
a=[2,-5,-2,-2,-1,3]
alternate(a)

def alternatEfficeint(arr):
    pivot=0
    i=-1
    for j in range(0,len(arr)):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)
    print("after partition:",arr)

    pos=i+1
    neg=0
    while pos<len(arr) and neg<pos:
        if arr[neg]<0:
            swap(arr,neg,pos)
        neg+=2
        pos+=1
    print(arr)

# a=[2,-5,-3,9,-8,-7]
# alternatEfficeint(a)

def subarrasumZero(arr):
    hm={}
    csum=0
    for i in range(len(arr)):
        csum+=arr[i]
        if csum in hm or csum==0:
            return True
        hm[csum]=True
    return False

# a=[3,2,4,-4]
# print(subarrasumZero(a))


def subarrsumEqualsk(arr,k):
    hm={}
    csum=0
    for i in range(len(arr)):
        csum+=arr[i]
        diff=csum-k
        if diff in hm:
            return (hm[diff]+1,i)
        hm[csum]=i
    
# a=[3,9,-2,2,1,1,1,6]
# print(subarrsumEqualsk(a,5))

def longestConsecutiveSequenc(arr):
    arr=set(arr)
    arr=list(arr)
    arr.sort()
    n=len(arr)
    cnt=0
    prev=True
    res=0
    for i in range(0,n-1):
        if arr[i]+1==arr[i+1] and prev==True:
            cnt+=1
            prev=True
        elif arr[i]+1!=arr[i+1]:
            prev=False
        if prev==False:
            res=max(res,cnt+1)
            cnt=0
            prev=True
    
    if len(arr)!=0:
        res=max(res,cnt+1)
    return res

# arr=[130,156,2,9,5,5,7,10,11,8,131,132,131,133]
# print(longestConsecutiveSequenc(arr))

def longestConsecutiveEfficient(arr):
    hm={}
    for ele in arr:
        hm[ele]=True
    
    res=0
    for ele in arr:
        prev=ele-1
        if prev not in hm:
            cnt=0
            current=ele
            while current in hm:
                cnt+=1
                current+=1
            res=max(res,cnt)
    return res


# arr=[130,156,2,9,5,5,7,10,11,8,131,132,131,133]
# arr=[11,10,1,4,12,2,3]
# print(longestConsecutiveEfficient(arr))

def buyandSellTwice(arr):
    n=len(arr)
    left=[0]*len(arr)
    leastbuyprice=arr[0]
    # best profit if it sold today or till today
    for i in range(1,n):
        if arr[i]<leastbuyprice:
            leastbuyprice=arr[i]
        profit=arr[i]-leastbuyprice
        left[i]=max(left[i-1],profit)
    
    right=[0]*n
    maxsellprice=arr[n-1]
    # best profit if it bought today or after today any day
    for i in range(n-2,-1,-1):
        if arr[i]>maxsellprice:
            maxsellprice=arr[i]
        profit=maxsellprice-arr[i]
        right[i]=max(right[i+1],profit)
    
    res=0
    for i in range(0,n):
        res=max(res,left[i]+right[i])
    
    return res

arr=[2,30,15,10,8,25,80]
arr=[30,50,45,20,80,10,71,55,50]
print(buyandSellTwice(arr))



