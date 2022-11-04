
# O(N) O(N)
def moveoneside(arr):
    neg=[]
    pos=[]
    for i in range(len(arr)):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    
    return neg+pos

arr=[-12,13,14,-9,20,-10]
print(moveoneside(arr))

def moveoneside2(arr):
    j=0
    for i in range(0,len(arr)):
        if arr[i]<0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1
    return arr


arr=[-12,13,14,-9,20,-10]
print(moveoneside(arr))

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def sort3color(arr):
    l=c=0
    h=len(arr)-1
    while c<=h:
        if arr[c]==0:
            swap(arr,c,l)
            c+=1
            l+=1
        elif arr[c]==1:
            c+=1
        elif arr[c]==2:
            swap(arr,c,h)
            h=h-1
    return arr

arr=[1,0,1,2,0,0]
print(sort3color(arr))

def roatatearrbyone(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr

def roatatearr(arr,k):
    n=len(arr)
    temp=[-1]*len(arr)
    for i in range(0,len(arr)):
        temp[(i+k)%n]=arr[i]
        
    arr=temp[::1]
    return arr

# arr=[1,2,3,4,5]
# #print(roatatearrbyone(arr))
# print(roatatearr(arr,2))

def duplicates(arr, n): 
    # code here
    res=set()
    freq={}
    for ele in arr:
        freq[ele]=1+freq.get(ele,0)
        
    for k,v in freq.items():
        if v>=2:
            res.add(k)
    out=list(res)
    out.sort()
    if len(out)==0:
        return [-1]
    else:
        return out

def mergeTwosortedarr(arr1,arr2):
    n1,n2=len(arr1),len(arr2)
    temp=[-1]*(n1+n2)
    i,j,k=0,0,0
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            temp[k]=arr1[i]
            i+=1
            k+=1
        else:
            temp[k]=arr2[j]
            j+=1
            k+=1
    
    while i<n1:
        temp[k]=arr1[i]
        i+=1
        k+=1
    while j<n2:
        temp[k]=arr2[j]
        j+=1
        k+=1
    print(temp)

# arr2=[2,3,9]
# arr1=[1,4,7,8,10,12]
# mergeTwosortedarr(arr1,arr2)

def swap(x,y,i,j):
    x[i],y[j]=y[j],x[i]

def insert(arr,i):
    key=arr[i]
    i+=1
    while i<len(arr) and arr[i]<key:
        arr[i-1]=arr[i]
        i+=1
    arr[i-1]=key

# using insertion method O(n*m) time and O(1) space
def mergeTwosorted2(arr1,arr2):
    i=0
    while i<len(arr1):
        if arr1[i]<arr2[0]:
            i+=1
        elif arr1[i]>arr2[0]:
            swap(arr1,arr2,i,0)
            insert(arr2,0)
            i+=1
    print(arr1,arr2)

# arr1=[1,4,7,8,10]
# arr2=[2,3,9]
# mergeTwosorted2(arr1,arr2)

# gap algorithm O(N) time and O(1) space

def nextgap(gap):
    if gap<=1:
        return 0
    return (gap//2)+(gap%2)  # ceil function 5//2 -> 2 +(5%2)=3

def mergeTwosortedGapAlgo(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    gap=nextgap(n+m)
    
    while gap>0:
        # when trveersing only in arr1 
        i=0
        while i+gap<n:
            if  (arr[i]>arr[i+gap]):
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
        # i+gap now it reaches to arr2 out of arr1 bound
        j=gap-n if gap>n else 0 # if n=4 and gap 6 then first ptr i=0 nd second j=2 (6-4)
        while i<n and j<m:
            if (arr1[i]>arr2[j]):
                arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            j+=1
        
        # only in arr2 now both ptr in arr2
        if j<m:
            j=0
            while j+gap<m:
                if  (arr2[j]>arr2[j+gap]):
                    arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                j+=1
        
        gap=nextgap(gap)



# arr1=[1,4,7,8,10]
# arr2=[2,3,9]
# mergeTwosortedGapAlgo(arr1,arr2)
# print(arr1,arr2)

# res containes days to buy nd sell 
def stockBuySell(arr):
    #code here
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
            l=r
            prev=0
        r+=1


    return res

arr=[100 ,180, 260, 310, 40, 535, 695]
arr=[11 ,42, 49, 96, 23, 20, 49, 26, 26, 18, 73, 2, 53, 59, 34, 99, 25, 2]
arr=[16, 21, 23, 80, 79, 30 ,59 ,41, 52, 8, 35]
print(stockBuySell(arr))






