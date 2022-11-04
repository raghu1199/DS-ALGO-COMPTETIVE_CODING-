
from re import A


def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def reverse(arr,start,end):
    while start<=end:
        swap(arr,start,end)
        start+=1
        end-=1


def nextPermutation(arr):
    k,l=-1,-1
    n=len(arr)
    # if all desce order then make them sorted (all ascend order)
    descend=True
    for i in range(0,n-1):
        if arr[i]<arr[i+1]:
            descend=False
            break
    if descend==True:
        reverse(arr,0,n-1)
        return arr

    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            k=i
            break
    for j in range(n-1,-1,-1):
        if arr[j]>arr[k]:
            l=j
            break
    
    swap(arr,k,l)
    reverse(arr,k+1,n-1)
    return arr

# arr=[4,1,3,2]
# print(nextPermutation(arr))


def commoninThreeSortedarr(a,b,c):
    d={}
    for ele in a:
        d[ele]=-1
    
    for ele in b:
        if ele in d:
            d[ele]=2
    
    for ele in c:
        if ele in d:
            if d[ele]==2:
                d[ele]=3
    
    res=[]
    for k,v in d.items():
        if v==3:
            res.append(k)
    return res

# a=[1,5,10,20,40,80]
# b=[6,7,20,80,100]
# c=[3,4,15,20,30,70,80,120]
# print(commoninThreeSortedarr(a,b,c))

def alteranatenegativePositive(arr):
    neg=[]
    pos=[]
    for ele in arr:
        if ele<0:
            neg.append(ele)
        else:
            pos.append(ele)
    out=[-1]*len(arr)
    flag=False
    k,l,r=0,0,0
    while l<len(neg) and r<len(pos):
        if flag==False:
            out[k]=neg[l]
            l+=1
            flag=True
        elif flag==True:
            out[k]=pos[r]
            r+=1
            flag=False
        k+=1
    
    while l<len(neg):
        out[k]=neg[l]
        l+=1
        k+=1
    while r<len(pos):
        out[k]=pos[r]
        r+=1
        k+=1

    return out

# arr=[-5,-2,5,2,4,7,1,8,0,-8]
# print(alteranatenegativePositive(arr))

# O(1) space O(NlogN) original order of ele not maintained
def rearrnageAlternate(arr):
    arr.sort()
    l,r=0,0
    flag=True
    for i in range(len(arr)):
        if arr[i]>0:
            r=i
            break
    
    while l<len(arr):
        if arr[l]<0 and flag==True:
            l+=1
            flag=False
        elif arr[l]<0 and flag==False:
            swap(arr,l,r)
            l+=1
            r+=1
            flag=True
        else:
            break
    print(arr)

# arr=[1,2,3,-1,-4,-2,4]
# rearrnageAlternate(arr)

#O(N) time nd O(1) space
def rearrangeeffiecient(arr):
    n=len(arr)
    i=-1
    pivot=0
    for j in range(0,len(arr)):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)

    print("after partion:",arr)
    pos=i+1
    neg=0
    while pos<n and neg<pos:
        if arr[neg]<0:
            swap(arr,neg,pos)
        neg+=2
        pos+=1
    
    return arr

# arr=[-1,2,-3,4,5,6,-7,8,9]
# print(rearrangeeffiecient(arr))

def subarrsumequalZero(arr):
    d={}
    csum=0
    for i in range(len(arr)):
        csum+=arr[i]
        if (csum in d) or (csum==0):
            return True
        d[csum]=True
    return False

# arr=[1,4,-2,-1,5,-4,3]
# print(subarrsumequalZero(arr))

def subarrsumEqualsK(arr,k):
    d={}
    csum=0
    for i in range(len(arr)):
        csum+=arr[i]
        if csum-k in d:
            idx=csum-k
            return (d[idx]+1,i)
        d[csum]=i

    return -1

# arr=[3,9,-2,3,1,1,6]
# print(subarrsumEqualsK(arr,5))

def maxproductsubarr(arr):
    res=0
    cprod=1
    for i in range(len(arr)):
        if cprod==0:
            cprod=1
        cprod=cprod*arr[i]
        res=max(res,cprod)
        if arr[i]>cprod:
            cprod=arr[i]

    return res
# arr=[6,-3,-10,0,2]
# print(maxproductsubarr(arr))

# l=[1,2,2,3,4]
# s=set(l)
# l=list(s)
# print(s)
# print(l[3])

def findLongestConseqSubseq(self,arr, N):
        #code here
        
    temp=arr[::1]
    s=set(temp)  # to remove duplicates
    temp=list(s)
    temp.sort()
    res=0
    cnt=0
    prev=True
    #print("temp:",temp)
    for i in range(0,len(temp)-1):
        if (temp[i]+1==temp[i+1]) and prev==True:
            prev=True
            cnt+=1
            #print(cnt)
        elif (temp[i]+1!=temp[i+1]):
            prev=False
        
        if prev==False:
            res=max(res,cnt+1)
            #print("res",res)
            if i!=N-2:
                prev=True
            cnt=0
            
        if i==len(temp)-2:
            res=max(res,cnt+1)
    
    # if len==1 then above for loop not runs so to handle that       
    if prev==True:
        res=max(res,cnt+1)
    
    return res

def longestsubsequence(arr):
    freq={}
    for ele in arr:
        freq[ele]=True
    
    res=0
    for ele in arr:
        take=ele-1
        if take in freq:
            l=0
            while take in freq:
                take+=1
                l+=1
        res=max(res,l)

    return res

# arr=[11,10,1,4,12,2,3]    
# print(longestsubsequence(arr))



# only 2 transaction allowed buy-sell buy-sell
def buyndsell2(arr):
    n=len(arr)
    leastbl=arr[0]
    dpl=[-1]*n
    dpl[0]=0
    for i in range(1,n):
        if arr[i]<leastbl:
            leastbl=arr[i]
        profit=arr[i]-leastbl
        dpl[i]=max(dpl[i-1],profit)
    
    maxsellright=arr[n-1]
    dpr=[-1]*n
    dpr[n-1]=0
    for i in range(n-2,-1,-1):
        if arr[i]>maxsellright:
            maxsellright=arr[i]
        profit=maxsellright-arr[i]
        dpr[i]=max(dpr[i+1],profit)
    
    res=0
    for i in range(0,n):
        res=max(res,dpl[i]+dpr[i])
    
    return res

# arr=[30,50,45,20,40,80,30,10,71,50,55]
# print(buyndsell2(arr))

import sys
#[16,21,23,80,79,30,59,41,52,8,35]
# inifnite transaction allowed
def buyndsell3(arr):
    n=len(arr)
    l,r=0,1
    res=[]
    prev=0
    while r<=n-1:
        profit=arr[r]-arr[l]
        print(profit,arr[r],arr[l])
        if profit>prev:
            prev=profit
            if r==n-1:
                res.append(prev)

        elif profit<prev:
            res.append(prev)
            prev=0
            l=r
        r+=1
    
    print(res)
    return sum(res)

# arr=[16,21,23,80,79,30,59,41,52,8,35]
# print(buyndsell3(arr))

def printMatrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()

# k transaction allowed
def ktransaction(arr,k):
    n=len(arr)
    dp=[[0 for j in range(n)] for i in range(k+1)] # k+1 rows nd n days as col

    for t in range(1,k+1):
        for d in range(1,n):
            maxtm1=0
            for vd in range(0,d):
                f=dp[t-1][vd]
                s=arr[d]-arr[vd]
                maxtm1=max(f+s,maxtm1)
            
            dp[t][d]=max(dp[t][d-1],maxtm1)
    
    printMatrix(dp)
    return dp[k][n-1]

# arr=[9,6,7,6,3,8]
# print(ktransaction(arr,3))


# optimized o(n^2)
def ktransactionoptimized(arr,k):
    n=len(arr)
    dp=[[0 for j in range(n)] for i in range(k+1)] # k+1 rows nd n days as col

    for t in range(1,k+1):
        ma=-sys.maxsize
        for d in range(1,n):
            ma=max(ma,dp[t-1][d-1]-arr[d-1])

            dp[t][d]=max(ma+arr[d],dp[t][d-1])
            
    
    printMatrix(dp)
    return dp[k][n-1]

# arr=[9,6,7,6,3,8]
# print(ktransactionoptimized(arr,3))


def goodValBadval(arr,k):
    n=len(arr)
    size=0
    for ele in arr:
        if ele<=k:
            size+=1
    badvalues=0
    for i in range(0,size):
        if arr[i]>k:
            badvalues+=1
    
    res=badvalues
    for i in range(1,n-size+1):
        last=arr[i-1]
        new=arr[i+size-1]
        if last > k:
            badvalues-=1
        if new >k:
            badvalues+=1
        res=min(res,badvalues)
    
    return res

#arr=[2,7,1,5,8,3]
# arr=[2,1,5,6,3]
# print(goodValBadval(arr,3))

def palindromicarr(arr):
    n=len(arr)
    cnt=0
    l=0
    r=n-1
    while l<=r:
        if arr[l]==arr[r]:
            l+=1
            r-=1
        else:
            while arr[l]!=arr[r]:
                if arr[l]<arr[r]:
                    arr[l+1]=arr[l]+arr[l+1]
                    l=l+1
                    cnt+=1
                else:
                    arr[r-1]=arr[r]+arr[r-1]
                    r-=1
                    cnt+=1

    print(arr)
    return cnt


def palindromicarr2(arr):
    n=len(arr)
    cnt=0
    l=0
    r=n-1
    while l<=r:
        if arr[l]==arr[r]:
            l+=1
            r-=1
        elif arr[l]<arr[r]:
            arr[l+1]=arr[l]+arr[l+1]
            l+=1
            cnt+=1
        else:
            arr[r-1]=arr[r]+arr[r-1]
            r-=1
            cnt+=1
        
    print(arr)
    return cnt

# arr=[1,9,5,4,1]
# print(palindromicarr2(arr))
    
    
def minswapstosortarr(arr):
    n=len(arr)
    pair=[]
    for i in range(0,len(arr)):
        pair.append((arr[i],i))

    pair.sort(key=lambda x:x[0])
    print(pair)
    cnt=0
    i=0
    while i<=n-1:
        if i==pair[i][1]:
            i+=1
            continue
        else:
            idx=pair[i][1]
            swap(pair,i,idx)
            cnt+=1
            print("after swap:",i)

    # control over i in for loop is not possible
    # for i in range(0,len(arr)):
    #     print("next initial:",i)
    #     if i==pair[i][1]:
    #         continue
    #     else:
    #         idx=pair[i][1]
    #         swap(pair,i,idx)
    #         cnt+=1
    #         i-=1
    #         print("after swap:",i)
        
    
    print(pair)
    return cnt

arr=[1,5,4,3,2]
arr=[4,1,2,3]
print(minswapstosortarr(arr))

            




        
    

