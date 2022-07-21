
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

def singleelement(arr):
    x=0
    for ele in arr:
        x=x^ele
    return x


# start at even index and end at odd index for all twice ele
def single(arr):
    start=0
    end=len(arr)-1
    if end==0:
        return arr[0]
    # boundary cases
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[end]!=arr[end-1]:
        return arr[end]
    
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
            return arr[mid]
        if ((mid%2==0) and arr[mid]==arr[mid+1]) or ((mid%2!=0 and arr[mid]==arr[mid-1])):
            start=mid+1  # go right side bcz left side is perfect single will not be there
        else:
            end=mid-1
    
    return False

arr=[1,1,2,2,3,4,4]
print(single(arr))