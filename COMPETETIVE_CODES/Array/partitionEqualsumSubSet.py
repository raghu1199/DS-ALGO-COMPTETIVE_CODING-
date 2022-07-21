
def isSubsetSum(val,n,sum):

    s=[[False for j in range(sum+1)] for i in range(n+1) ]

    # if sum =0 then True for all item s[i][0] All true
    for i in range(n+1):
        s[i][0]=True
    # if sum!=0 and n=0 then false
    for i in range(1,sum+1):
        s[0][i]=False
    
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j< val[i-1]:
                s[i][j]=s[i-1][j]
            if val[i-1]<=j:
                s[i][j]=(s[i-1][j] or s[i-1][j-val[i-1]])
    
    return s[n][sum]

def findpartition(arr,n):
    sum=0
    for i in range(n):
        sum+=arr[i]
    if sum%2!=0:
        return False
    return isSubsetSum(arr,n,sum//2)

arr=[1,5,11,5]
print(findpartition(arr,len(arr)))

