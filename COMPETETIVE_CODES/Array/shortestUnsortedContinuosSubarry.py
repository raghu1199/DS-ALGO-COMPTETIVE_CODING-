

# Given an integer array, you need to find one continuous subarray that if you only s
# sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# selection sort based O(N^2)
def shortestUnsortedSubarr(arr):
    start=len(arr)
    end=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                start=min(start,i)
                end=max(end,j)
    # if all sorted then not updation in end 
    if end-1<0:
        return 0
    else:
        return end-start+1

# o(nlogn) time and o(n) space

def shortestUnsortedarr(arr):
    start=len(arr)
    end=0
    sortedarr=arr[:]  # copy all ele start to end
    sortedarr.sort()
    for i in range(len(arr)):
        if sortedarr[i]!=arr[i]:
            start=min(start,i)
            end=max(end,i)
    
    if end-1<0:
        return 0
    else:
        return end-start+1


    
arr=[2,6,4,8,10,9,15]
print(shortestUnsortedarr(arr))

# o(n)
def findUnsortedSubarray(self, arr: List[int]) -> int:
        start=len(arr)
        end=0
        stack=[]

        for i in range(len(arr)):
            # if top 2 nd arr[i]=6t hen top<arr[i] simply push
            while stack and arr[stack[-1]]>arr[i]:
                poped=stack.pop()
                start=min(start,poped)
            stack.append(i)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            # if top 15 nd arr[i] 9 top> arr[i] so simply push
            while stack and arr[stack[-1]]<arr[i]:
                poped=stack.pop()
                end=max(end,poped)
            stack.append(i)
        if end-1<0:
            return 0
        else:
            return end-start+1
                
                