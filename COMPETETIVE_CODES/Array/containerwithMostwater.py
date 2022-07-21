
def maxarea(arr):
    n=len(arr)
    l,r=0,n-1
    res=0
    while l<r:
        length=r-l 
        if arr[l]<arr[r]:
            height=arr[l]
            l+=1
        else:
            height=arr[r]
            r-=1
        area=length*height
        res=max(area,res)

    return res

#arr=[1,8,6,2,5,4,8,3,7]
arr=[1,1]
print(maxarea(arr))



    
        

