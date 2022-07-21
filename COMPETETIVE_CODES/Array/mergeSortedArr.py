# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# The final sorted array should not be returned by the function, but instead be stored i
# nside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


from copy import deepcopy


# O(M+N) space
def merge1(left,right):
    s1,s2=len(left),len(right)
    print(s1,s2)
    for i in range(len(left)-1,-1,-1):
        if left[i]==0:
            s1-=1
        if left[i]!=0:
            break
    print("after ignor 0:",s1,s2)
    out=[0]*(s1+s2)
    

    i,j,k=0,0,0
    while i< s1 and j<s2:
        print(i,j,k)
        if left[i]<=right[j]:
            print("move left")
            out[k]=left[i]
            i+=1
            k+=1
            print(i,j,k)
        elif right[j]<left[i]:
            print("move right:")
            out[k]=right[j]
            j+=1
            k+=1
            print(i,j,k)
        
    while i<s1:
        out[k]=left[i]
        i+=1
        k+=1
    while j<s2:
        out[k]=right[j]
        j+=1
        k+=1

    # for i in range(0,len(out)):
    #     left[i]=out[i]
    left=deepcopy(out)

    print(left)

# left=[-1,0,0,2,3,0,0,0]  # only ignore zeros from last inbteween 0 are important
# right=[5,6,7]
# merge1(left,right)

# O(1 space)
# i denote no of elements in left that should be merged same for j
def merge(left,right,m,n):
    # index 0 based so 
    i=m-1
    j=n-1
    k=m+n-1  # to indicate last ele position in left
    while i>=0 and j>=0:
        if left[i]>=right[j]:
            left[k]=left[i]
            i-=1
            k-=1
        elif right[j]>left[i]:
            left[k]=right[j]
            j-=1
            k-=1
    # if reamining ele in right
    while j>=0:
        left[k]=right[j]
        j-=1
        k-=1
    print(left)




# left=[-1,0,0,2,3,0,0,0]  # only ignore zeros from last inbteween 0 are important
# right=[5,6,7]
left=[2,2,3,0,0,0,0]
right=[0,1,5,6]
merge(left,right,3,4)
