
def minimizemaxdiff(arr,k):
    n=len(arr)
    arr.sort()
    print("original:",arr)
    mid=len(arr)//2
    
    for i in range(0,mid):
        arr[i]=arr[i]+k
    print("till mid:",arr)
    # if diff becomes negative then after mid only add the k
    # if arr[mid]-k <0:
    #     k=-k

    for i in range(mid,n):
        if arr[i]-k<0:
            arr[i]=arr[i]+k
        else:
            arr[i]=arr[i]-k
    
    print(arr)
    arr.sort()
    max_diff=arr[n-1]-arr[0]
    return max_diff

# arr=[1,5,15,10]
# arr=[4,6]
# arr=[5,6,1,3,2,4]
arr=[2 ,6 ,3, 4, 7, 2, 10, 3, 2, 1] # for this ans is 7 bt it ives 8
print(minimizemaxdiff(arr,5))

import sys
def minidiffone(arr,k):
    n=len(arr)
    arr.sort()
    res=arr[n-1]-arr[0]
    print("original diff:",res)
    tallest=arr[n-1]-k
    shortest=arr[0]+k

    print(f"original maxh:{tallest} minh:{shortest}")
    for i in range(0,n-1):
        maxh=max(tallest,arr[i]+k)
        minh=min(shortest,arr[i+1]-k)
        print(f"maxh:{maxh} minh:{minh},diff:{maxh-minh}")
        res=min(res,maxh-minh)
        
    
    return res


arr=[1,8,5,10]
arr=[1,2,3,4,5]
arr=[1,3,4,7,10]
# arr=[10,20,30,40]
print(minidiffone(arr,3))
            
        
        

