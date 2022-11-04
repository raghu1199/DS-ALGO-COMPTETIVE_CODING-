def nextgap(gap):
    if gap<=1:
        return 0
    return (gap//2)+(gap%2)  # ceil function 5//2 -> 2 +(5%2)=3

def mergeTwosortedGapAlgo(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    gap=nextgap(n+m)
    
    while gap>0:
        # when trveersing only in arr1 
        i=0
        while i+gap<n:
            if  (arr[i]>arr[i+gap]):
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
        # i+gap now it reaches to arr2 out of arr1 bound
        j=gap-n if gap>n else 0 # if n=4 and gap 6 then first ptr i=0 nd second j=2 (6-4)
        while i<n and j<m:
            if (arr1[i]>arr2[j]):
                arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            j+=1
        
        # only in arr2 now both ptr in arr2
        if j<m:
            j=0
            while j+gap<m:
                if  (arr2[j]>arr2[j+gap]):
                    arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                j+=1
        
        gap=nextgap(gap)



# arr1=[1,4,7,8,10]
# arr2=[2,3,9]
# mergeTwosortedGapAlgo(arr1,arr2)
# print(arr1,arr2)