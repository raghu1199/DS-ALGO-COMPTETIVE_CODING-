
# O(N^2)
def sortedtriplet(arr):
    result=[None]*3
    first,second,third=None,None,None
    n=len(arr)
    for i in range(0,len(arr)):
        if i==0:
            first=arr[i]
            index=0
            for j in range(i+1,n):
                if arr[j]>first:
                    second=arr[j]
                    index=j
                    break
            if second:
                for k in range(index+1,n):
                    if arr[k]>second:
                        third=arr[k]
                        return (first,second,third)
        else:
            print("Inside 2nd option")
            for j in range(0,i):
                if arr[j]<arr[i]:
                    first=arr[j]
            for k in range(i+1,n):
                if arr[k]>arr[i]:
                    third=arr[k]
            if first and third:
                return (first,arr[i],third)

# O(N)    
def sortedtriplet2(arr):
    min=0
    first,second=-1,-1
    for i in range(1,len(arr)):
        if arr[i]<arr[min]:
            min=i
        elif second==-1:   # means if arr[i]!<arr[min] so arr[i]>arr[min] we found second
            second=i
            first=min
        elif arr[i]<arr[second]:
            second=i
            first=min
        else:   # means arr[i]> arr[second] so we found third which is arr[i]
            return (arr[first],arr[second],arr[i])

#arr=[5,4,3,7,6,1,9]
#arr=[1,2,3,6,5,0,9]
arr=[9,8,7,1,2,10]
#arr=[1,2,3]
print(sortedtriplet2(arr))







