

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

def shift(arr,n,idx):
    for i in range(n-2,idx-1,-1):
        arr[i+1]=arr[i]
    #arr[idx]=newele
    print("after shift:",arr)
    
def createTargetArr(arr,index):
    target=[-1]*len(arr)
    n=len(arr)
    for i in range(len(arr)):
        idx=index[i]
        if target[idx]!=-1:
            shift(target,n,idx)
            target[idx]=arr[i]
        elif target[idx]==-1:
            target[idx]=arr[i]
    return target

# arr=[0,1,2,3,4]
# index=[0,1,2,2,1]
# print(createTargetArr(arr,index))

def replacewithLargestRight(arr):
    n=len(arr)
    largestright=arr[n-1]
    arr[n-1]=-1
    for i in range(n-2,-1,-1):
        prev=largestright
        if arr[i]>largestright:
            largestright=arr[i]
        arr[i]=prev

    return arr

# arr=[17,18,5,4,6,1]
# print(replacewithLargestRight(arr))

# this will not handle [1,3,3,3,2,4,8,6,12] or [1,3,2,2,2]->op 4, cases
def shortestUnsortedarr(arr):
    start=len(arr)+1
    n=len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            start=min(start,i-1)

    print("start:",start)
    end=0
    for j in range(len(arr)-1,0,-1):
        if arr[j-1]>arr[j]:
            end=max(end,j)
    print("end:",end)
    if end-1<0:
        return 0  # already sorted
    else:
        return end-start+1

# arr=[2,6,4,8,10,9,15]
# arr2=[1,2,3,4]
# arr3=[2,1]
# print(shortestUnsortedarr(arr3))

def shortestUnsorted2(arr):
    start=len(arr)+1
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            popped=stack.pop()
            start=min(start,popped)
        stack.append(i)
    end=0
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]]<arr[i]:
            popped=stack.pop()
            end=max(end,popped)
        stack.append(i)

    if end-1<0:
        return 0
    else:
        return end-start+1

# arr=[1,3,2,2,2]
# print(shortestUnsorted2(arr))
    
def findleaders(arr):
    n=len(arr)
    leaders=[]
    largestright=arr[n-1]
    leaders.append(largestright)
    # for i in range(n-2,-1,-1):
    #     if arr[i]>largestright:
    #         largestright=arr[i]
    #     if arr[i]==largestright:
    #         leaders.append(largestright)
    for i in range(n-2,-1,-1):
        if arr[i]>largestright:
            leaders.append(arr[i])
            largestright=arr[i]
    return leaders[::-1]

# arr=[8,4,2,3,1,5,4,2]
# print(findleaders(arr))

# sort colors(3 colored)
def dutchnationalflag(arr,k):
    bucket=[0]*k
    for ele in arr:
        if ele==0:
            bucket[0]+=1
        if ele==1:
            bucket[1]+=1
        if ele==2:
            bucket[2]+=1
    print(bucket)
    temp=[]
    for i in range(k):
        l=[i]*bucket[i]
        temp.extend(l)
        
    print(temp)

# arr=[0,1,0,1,2,1,2,1]
# dutchnationalflag(arr,3)

def swap(arr,k,l):
    arr[k],arr[l]=arr[l],arr[k]

def dutchnational(arr):
    l,c,h=0,0,len(arr)-1
    while c<=h:
        if arr[c]==0:
            swap(arr,l,c)
            l+=1
            c+=1
        elif arr[c]==1:
            c+=1
        elif arr[c]==2:
            swap(arr,c,h)
            h-=1
    print(arr)

# arr=[1,0,1,1,2,0,0]
# dutchnational(arr)

def reversearr(arr,start,end):
    while start<end:
        swap(arr,start,end)
        start+=1
        end-=1

def nextPermutation(arr):
    isDesc=True
    for i in range(len(arr)-1):
        if not arr[i]>arr[i+1]:
            isDesc=False
            break
    if isDesc:
        reversearr(arr,0,len(arr)-1)
        print(arr)
        return
    k,l=-1,-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]<arr[i+1]:
            k=i
            break
    for j in range(len(arr)-1,-1,-1):
        if arr[j]>arr[k]:
            l=j
            break
    swap(arr,k,l)
    print("after swap:",arr)
    reversearr(arr,k+1,len(arr)-1)
    print(arr)

# arr=[3,2,1]
# arr=[1,3,5,4,2]
# nextPermutation(arr)



def generate(str,l,r):

    if l==len(str):
        print("".join(str),end=" ")
        #print(l,end=" ")
        return

    for i in range(l,r):

        swap(str,l,i)

        generate(str,l+1,r)
        # on backtrack make as prev as it is
        swap(str,l,i)

# str="ABC"
# generate(list(str),0,len(str))
# l="123"
# generate(list(l),0,len(l))


def sortedTriplet(arr):
    first=mid=-1
    minidx=0
    for i in range(1,len(arr)):
        if arr[i]<=arr[minidx]:
            minidx=i
        elif mid==-1:
            first=minidx
            mid=i
        elif arr[i]<arr[mid] and arr[i]!=arr[minidx]:
            mid=i
            first=minidx
        elif arr[i]>arr[mid] and arr[i]!=arr[minidx]:
            return [arr[first],arr[mid],arr[i]]
    return 0

# arr=[5,4,3,7,6,1,9]
# arr=[1,2,1,1,3]
# arr=[1,1,3]
# arr=[3,5,2,3,4]
# print(sortedTriplet(arr))

def partitionEqualSum(arr):
    leftsum=0
    for i in range(len(arr)):
        leftsum+=arr[i]
    rightsum=0
    for i in range(len(arr)-1,-1,-1):
        rightsum+=arr[i]
        leftsum-=arr[i]
        if leftsum==rightsum:
            print(f"left:0 to {i-1} right:{i} to {len(arr)-1}")
            return (i)
# arr=[4,1,2,3]
# arr=[11,9,5,5,4,6]
# print(partitionEqualSum(arr))

# l=sum(arr[:2:1])
# r=sum(arr[3::1])
# print(l,r)

def equlibiriumsum(arr):
    l,r=0,0
    n=len(arr)
    if len(arr)<=2:
        return 'NO'
    totalsum=sum(arr)
    lsum={}
    rsum={}
    csum=totalsum
    for i in range(n-1,0,-1):
        csum-=arr[i]
        lsum[i]=csum
    csum=totalsum
    for j in range(0,n-1,1):
        csum-=arr[j]
        rsum[j]=csum
    print(lsum)
    print()
    print(rsum)
    for i in range(1,n-1):
        l=lsum[i]
        r=rsum[i]
        if l==r:
            print(i)
            return 'YES'

    # for i in range(1,len(arr)-1):
    #     l=sum(arr[:i:1])
    #     r=sum(arr[i+1::1])
    #     print(l,r)
    #     if l==r:
    #         return i
    return 'NO'

# arr=[1,2,3,3]
# arr=[10 ,1, 5, 10, 10, 5, 6, 4, 7, 7, 10,1, 7 ,6, 5, 1, 7, 9, 4, 2, 7, 2, 8]
# print(equlibiriumsum(arr))

def equilibrium(arr): 
    	# code here
    n=len(arr)
    totalsum=sum(arr)
    print("Total:",totalsum)
    if n<=2:
        return 'NO'
    prev=0
    for i in range(0,n-1):
        print(totalsum-arr[i])
        prev+=arr[i]
        diff=totalsum-arr[i]
        if (diff%2==0 )and (diff//2)==(prev-arr[i]):
            return 'YES'
    return 'NO'
# arr=[10 ,1, 5, 10, 10, 5, 6, 4, 7, 7, 10,1, 7 ,6, 5, 1, 7, 9, 4, 2, 7, 2, 8]
# arr=[1,2,3,3]
# print(equilibrium(arr))

# arr=[5,2,3,4]
def arrProductexcepti(arr):
    left=[1]*len(arr)
    n=len(arr)
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]
    r=1
    out=[0]*len(arr)
    for i in range(n-1,-1,-1):
        out[i]=left[i]*r
        r=r*arr[i]
    return out

# arr=[5,2,3,4]
# print(arrProductexcepti(arr))

def arrProduct(arr):
    n=len(arr)
    left=[1]*n
    right=[1]*n
    left[0]=1
    right[n-1]=1
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*arr[i+1]

    out=[1]*len(arr)
    for i in range(0,n):
        out[i]=left[i]*right[i]
    return out

# arr=[5,2,3,4]
# print(arrProduct(arr))

def findDuplicates(arr):
    res=[]
    for i in range(len(arr)):
        idx=abs(arr[i])-1
        if arr[idx]>0:
            arr[idx]*=-1
        else:
            res.append(abs(arr[i]))
    return res

# arr=[4,3,2,7,8,2,3,1]
# print(findDuplicates(arr))

def canJumptoend(arr):
    n=len(arr)
    reachable=0
    for i in range(0,n):
        if reachable<i:
            return False
        reachable=max(reachable,i+arr[i])
    return True

# arr=[1,1,2,3,2,1,0,0,1,3]
# print(canJumptoend(arr))

from copy import deepcopy
import sys
# DP solution O(N^2)
def minNojumstoend(arr):
    n=len(arr)
    dp=[sys.maxsize]*len(arr)
    dp[0]=0
    for i in range(n):
        for j in range(0,i):
            if i<=(j+arr[j]):
                dp[i]=min(dp[i],dp[j]+1)
    return dp[n-1]


# arr=[2,1,3,2,3,4,5,1,2,8]
# print(minNojumstoend(arr))

#O(N)
def minjumstoend(arr):
    n=len(arr)
    maxreach=0
    jumps=0
    currentend=0
    for i in range(0,len(arr)):
        maxreach=max(maxreach,i+arr[i])
        if maxreach>=n-1:
            return 1+jumps
        elif maxreach==i:
            return -1
        elif currentend==i:
            jumps+=1
            currentend=maxreach

# arr=[1,2,4,2,1,2,1,0]
# print(minjumstoend(arr))
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

import random
def partition_random(arr,start,end):
    randomidx=random.randrange(start,end)
    #swap to randomidx ele to start
    arr[start],arr[randomidx]=arr[randomidx],arr[start]
    pivot=arr[start]
    print("original arr:",arr," pivot:",pivot)
    i=start
    for j in range(start+1,end+1):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)
    print("i:",i)
    print("before last :",arr)
    swap(arr,start,i)
    print("after partion at pivotidx:",i," arr:",arr)
    return i
    

def kthsmallest(arr,left,right,k):
    print("in arr:",arr," left:",left," right:",right)
    if left==right:
        return arr[left]

    pos=partition_random(arr,left,right)
    print("pivot pos:",pos)

    lcount=pos-left+1
    if lcount==k:
        return arr[pos]
    elif k<lcount:
        return kthsmallest(arr,left,pos,k)
    
    return kthsmallest(arr,pos+1,right,k-lcount)

# arr=[9,1,2,3,4,6,8,7,10,5,11]
# print(kthsmallest(arr,0,len(arr)-1,4))
    

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

# a[0]<=a[1]>=a[2]<=a[3]>=a[4]... 
# gfg
def wigglesort(arr):
    arr.sort()
    n=len(arr)
    if n>=3:
        for i in range(1,n-1,2):
            swap(arr,i,i+1)
    return arr

# arr=[3,5,2,6,1,4]
# arr=[1,1,5,1,1,4,6]  
# arr=[1,5,1,1,6,4]
# print(wigglesort(arr))

# a[0]<a[1]>a[2]<a[3]>a[4]...
def wigglesort2(arr):
    arr.sort()
    n=len(arr)
    temp=[-1]*n
    i=1
    j=n-1
    while True:
        if not i>n-1:
            temp[i]=arr[j]
            i+=2
            j-=1
        else:
            break
    i=0
    while not i>n-1:
        temp[i]=arr[j]
        i+=2
        j-=1
    
    return temp

# arr=[1,5,1,1,6,4]
# print(wigglesort2(arr))

# arr[0]<=arr[1]>=arr[2]<=arr[3]>=arr[4]
def wigglesort1(arr):
    n=len(arr)
    for i in range(0,n-1):
        if i%2==0 and not (arr[i]<=arr[i+1]):
            swap(arr,i,i+1)
        elif i%2!=0 and not (arr[i]>=arr[i+1]):
            swap(arr,i,i+1)

    return arr

# arr=[10,12,15,6,9,8,3,4,11]
# print(wigglesort1(arr))

def findPeak(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return arr[i]
    
    # if not found till end then last ele is peak
    return arr[n-1]

# arr=[1,2,3,6,2]
# print(findPeak(arr))


def bs(arr,start,end,n):
    mid=(start+end)//2

    print("mid:",mid)
    if (mid==0 or arr[mid-1]<arr[mid]) and (mid==n-1 or arr[mid]>arr[mid+1]):
        print("first:",mid)
        return mid
    elif arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
        print("2nd:",mid)
        return mid
    elif mid>0 and  not (arr[mid-1]<arr[mid]):
        print("going left:",mid)
        return bs(arr,start,mid-1,n)
    elif not (arr[mid]>arr[mid+1]):
        print("going right:",mid)
        return bs(arr,mid+1,end,n)

#arr=[1,2,3,6,2]

# arr=[1,13]
# arr=[14, 14, 10, 4 ,13 ,8 ,17]
# print(bs(arr,0,len(arr)-1,len(arr)))

def almostSorted(arr):
    n=len(arr)
    sortarr=deepcopy(arr)
    sortarr.sort()
    if arr==sortarr:
        print("YES")
        return
    l=r=-1
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            l=i
            break
    for j in range(n-2,-1,-1):
        if arr[j]<arr[j+1]:
            r=j
            break
    temp=deepcopy(arr)
    temp[l],temp[r]=temp[r],temp[l]
    if temp==sortarr:
        print("YES")
        print("SWAP",l+1,r+1)
        return
    
    temp=deepcopy(arr)
    temp=temp[:l]+temp[l:r+1][::-1]+temp[r+1::1]
    print(temp)
    if temp==sortarr:
        print("YES")
        print("reverse :",l+1,r+1)
        return
    print("NO")

arr=[4,2]
arr=[1,5,4,3,2,6]
almostSorted(arr)





            
        






    











        



    
        

        