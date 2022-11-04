# find missing number
def missing(arr,n):
    d={}
    for i in range(1,n+1):
        d[i]=False
    for ele in arr:
        d[ele]=True
    
    res=[]
    for k,v in d.items():
        if v==False:
            res.append(k)
    return res

# arr=[1,2,4,5,6,8,9]
# n=9
# print(missing(arr,n))

def missingxorbased(arr,n):
    n1=1
    for i in range(1,n+1):
        n1=n1^i
    n2=1
    for ele in arr:
        n2=n2^ele
    missing=n1^n2
    return missing

# arr=[1,3,4]
# print(missingxorbased(arr,4))

# unconstrained
def findDuplicates(arr):
    d={}
    res=[]
    for ele in arr:
        if ele in d:
            res.append(ele)
        else:
            d[ele]=True
    return res

# arr=[1,5,6,7,8,5,9,7,6]
# print(findDuplicates(arr))

# arr ele value <=n
def duplicatesconstrained(arr):

    res=[]
    for ele in arr:
        idx=abs(ele)-1
        if arr[idx]<0:
            res.append(abs(ele))
        else:
            arr[idx]=-1*arr[idx]
    return res

# arr=[4,3,2,7,8,2,3,1]
# print(duplicatesconstrained(arr))

# remove duplicates
def removeduplicates(arr):
    d={}
    for ele in arr:
        d[ele]=False
    i=0
    for ele in arr:
        if d[ele]==False:
            arr[i]=ele
            i+=1
            d[ele]=True
        else:
            continue
    return i
# arr=[4,3,2,7,8,2,1,3]
# print(removeduplicates(arr))
# print(arr)

#[1,1,2,2,3,3,3] here 1 and 2 have same freq count so return false
#[1,2,2,3,3,3] all have distict count so return true
def uniqueFreq(arr):
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    s=set()
    for k,cnt in freq.items():
        if cnt in s:
            return False
        else:
            s.add(cnt)
    return True

# arr=[1,2,2,3,3]
# print(uniqueFreq(arr))

def majorityele(arr):
    n=len(arr)
    freq={}
    for ele in arr:
        freq[ele]=1+freq.get(ele,0)

    for k,v in freq.items():
        if v>=n//2:
            return k
    return -1

# arr=[2,8,7,3,2,3,3,3]
# print(majorityele(arr))

# O(n) O(1) space
def majorityele2(arr):
    m,cnt=0,0
    for i in range(len(arr)):
        if cnt==0:
            m=arr[i]
            cnt+=1
        else:
            if m==arr[i]:
                cnt+=1
            else:
                cnt-=1
    mcount=0
    print(m)
    for i in range(len(arr)):
        if arr[i]==m:
            mcount+=1
    n=len(arr)
    if mcount>=n//2:
        return m
    else:
        return -1
    
# arr=[2,8,7,3,2,3,3,3]
# print(majorityele2(arr))

def smallerthanCurrent(arr):
    temp=arr[::1]
    temp.sort()
    freq={}
    for i in range(len(arr)):
        if temp[i] not in freq:
            freq[temp[i]]=i
    out=[]
    for ele in arr:  # original arr
        count=freq[ele]
        out.append(count)
    return out

# arr=[8,1,2,2,3]
# print(smallerthanCurrent(arr))

def findTwomissingNums(arr,n):
    d={}
    for i in range(1,n+1):
        d[i]=False
    for ele in arr:
        if d[ele]==False:
            d[ele]=True
    out=[]
    for k,v in d.items():
        if v==False:
            out.append(k)
    return out

arr=[1,3,5,6]
print(findTwomissingNums(arr,6))

# O(nlogn)
def kmostfrequent(arr,k):
    freq={}
    for ele in arr:
        freq[ele]=1+freq.get(ele,0)
    l=[]
    for ele,count in freq.items():
        l.append([ele,count])
    l.sort(key=lambda x:x[0],reverse=True)
    print(l)
    l.sort(key=lambda x:x[1],reverse=True)
    print(l)
    out=[]
    for i in range(k):
        out.append(l[i][0])
    return out

# if same count then give large no first
arr=[8,1,1,2,2,3,3,3,4]
print(kmostfrequent(arr,2))
    
def kmostfrequent2(arr,k):
    bucket=[[] for i in range(len(arr)+1)]  # [[]]*len(arr)+1
    freq={}
    for ele in arr:
        freq[ele]=1+freq.get(ele,0)

    for ele,count in freq.items():
        bucket[count].append(ele)
    
    n=len(bucket)
    out=[]
    for count in range(n-1,-1,-1):
        if bucket[count]!=[] and k>0:
            out+=bucket[count]
            k=k-len(bucket[count])

    return out

# arr=[1,1,2,2,2,3,3,5,5,5,5]
# print(kmostfrequent2(arr,3))







