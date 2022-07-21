
def missingnum(arr,n):
    d={}
    for i in range(1,n):
        d[i]=-1
    for ele in arr:
        d[ele]=1
    print(d)
    for i in range(1,n):
        if d[i]==-1:
            return i
    
arr=[1,2,4,3,6,7,9,8,10]
n=10
print(missingnum(arr,n))  
   
        
def missing_num(arr,n):
    num1=arr[0]
    for i in range(1,len(arr)):
        num1=num1^arr[i]
    num2=1
    for i in range(2,n+1):
        num2=num2^i
    
    missing=num1^num2
    return missing

arrr=[1,2,4,3,6,7,9,8,10]
n=10
print(missing_num(arrr,n))