

# three sum using 2 sum approach
# given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
#  Find all unique triplets in the array which gives the sum of zero.
from collections import deque


def threesum(arr:list):
    temp=[-1]*len(arr)
    n=len(arr)
    for i in range(n):
        temp[i]=arr[i]
    temp.sort()

    for i in range(0,n-1): # goes till n-2 only
        l=i+1
        r=n-1
        found=False
        while l<r:
            sum=temp[i]+temp[l]+temp[r]
            if sum==0:
                first,second,third=temp[i],temp[l],temp[r]
                found=True
                break
            elif sum<0:
                l=l+1
            elif sum>0:
                r=r-1
        if found:
            break
    
    # get index of a,b,c from original arr

    f=arr.index(first)
    s,t=0,0
    #s=arr.index(second,f) not gives correct ouput
    for i in range(n):
        if arr[i]==second and i!=f:
            s=i
        if arr[i]==third and i!=f and i!=s:
            t=i
    return (f,s,t)


# returns all possible solutions  must not contain duplicate tuples

def threesum2(arr:list):
    temp=[-1]*len(arr)
    n=len(arr)
    for i in range(n):
        temp[i]=arr[i]
    temp.sort()
    sol=set()
    for i in range(0,n-1): # goes till n-2 only
        l=i+1
        r=n-1
        while l<r:
            sum=temp[i]+temp[l]+temp[r]
            if sum==0:
                first,second,third=temp[i],temp[l],temp[r]
                sol.add((first,second,third))
                l=l+1
                r=r-1  # to break while loop indicates that whole arr is traversed so update l and r here
            elif sum<0:
                l=l+1
            elif sum>0:
                r=r-1
        
    return sol

    

arr=[-1,0,1,2,-1,-4]
print(threesum2(arr))


        




