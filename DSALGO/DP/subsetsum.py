#sum j 0 1 2 3
#n=1   T F F F
#n=2   T F F F
#n=3   T F F F

from re import T


def isSubsetSum(val,n,sum):
    s=[[False for i in range(sum+1)] for j in range(n+1)]
    # if sum=0 then it is true
    for i in range(n+1):
        s[i][0]=True
    # if no item then any sum =1 ,2 ,3 not possible
    for j in range(1,sum+1):
        s[0][j]=False
    
    #main logic (must start with row =1 and col=1 )
    for i in range(1,n+1):
        for j in range(1,sum+1):
            # itm val more than current sum so cant be included(item val 4 nd cureent sum 1,2,3) so 
            # place prev row val do not include item
            if val[i-1]>j:
                s[i][j]=s[i-1][j]
            # if val itm less or equal than current sum then
            elif val[i-1]<=j:
                s[i][j]=( s[i-1][j] or s[i-1][j-val[i-1]] )# if not include(1stcase) gives true then dont need to include

    # print table
    print()
    for i in range(n+1):
        for j in range(sum+1):
            print(s[i][j],end=" ")
        print()

    return s[n][sum]

# val=[3,4,5,2]
# n=len(val)
# sum=6
# res=isSubsetSum(val,n,sum)
# print(res)
# 
set = [3, 34, 4, 12, 5, 2]
sum = 9
n=len(set)
res=isSubsetSum(set,n,sum)
print(res)