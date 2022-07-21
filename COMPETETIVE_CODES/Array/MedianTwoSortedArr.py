
def medianoftwosorted(A,B):
    n=len(A)
    m=len(B)
    if n>m:
        return medianoftwosorted(B,A)
    
    start=0
    end=n
    
    midofmergedArr=(m+n)//2  # 

    while start<=end:

        mid=(start+end)//2
        leftAptr=mid
        leftBptr=midofmergedArr-mid    # leftA+leftB= midofmergedArr
        # acccess element from a and b based on index of leftAptr nd leftBptr
        leftA=A[leftAptr-1] if (leftAptr>0) else float('-inf')
        leftB=B[leftBptr-1] if (leftBptr>0) else float('-inf')
        rightA=A[leftAptr] if (leftAptr<n) else float('inf')
        rightB=B[leftBptr] if (leftBptr<m) else float('inf')

        if leftA<=rightB and leftB<=rightA:
            if ((m+n)%2==0):
                return (max(leftA,leftB)+min(rightA,rightB))/2.0
            else:
                return max(leftA,leftB)
        elif leftA>rightB:
            end=mid-1
        else:
            start=mid+1

# A=[1,3,5,6,7,8,9,11]   
# B=[1,4,6,8,12,14,15,17]
A=[1,2,3,4,5]
B=[1,2,3,4,5,6]
print(medianoftwosorted(A,B))

