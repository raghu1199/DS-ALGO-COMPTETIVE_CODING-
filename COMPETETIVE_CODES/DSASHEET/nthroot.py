

# non int also allowed
# nthroot(m)
def sqrthroot(n,m):
    eps=0.01
    low=1
    high=m
    while((high-low)>eps):
        mid=(low+high)/2
        if mid*mid<m:
            low=mid
        else:
            high=mid
    
    print(high)


def mulitply(x,n):
    res=1
    for i in range(1,n+1):
        res=res*x
    print(res)
    return round(res,3)


def nthroot(n,m):
    eps=0.001
    low=1
    high=m
    while((high-low)>eps):
        mid=(low+high)/2
        res=mulitply(mid,n)
        if res<m:
            low=mid
        else:
            high=mid
    
    return round(high,3)

print(nthroot(3,64))

def nthrootInt(m,n):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        if pow(mid,n)==m:
            return mid
        elif pow(mid,n)<m:
            low=mid+1
        else:
            high=mid-1
    
    return -1

# print(nthrootInt(15,2))

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partitionarrAroundThreepoint(arr,low,high):
    n=len(arr)
    l=c=0
    h=n-1
    while c<=h:
        if arr[c]<low:
            swap(arr,l,c)
            l+=1
            c+=1
        elif arr[c]>=low and arr[c]<=high:
            c+=1
        elif arr[c]>high:
            swap(arr,c,h)
            h-=1

    return arr

arr=[1,14,5,20,4,2,54,20,22,87,15,98,3,1,32]
print(partitionarrAroundThreepoint(arr,14,20))