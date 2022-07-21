
# def find2missingnum(arr,n):
#     missing=[]
#     for i in range(1,n):
#         found=False
#         for j in range(len(arr)):
#             if arr[j]^i==0:
#                 found=True
#                 break
#         if not found:
#             missing.append(i)
#     print(missing)

# arr=[1,3,5,6]
# find2missingnum(arr,6)


# def find2missingnum2(arr,n):
#     missing=[]
#     temp=[-1]*(n+1)
#     for ele in arr:
#         temp[ele]=1
#     missing=[]
#     for i in range(1,n):
#         if temp[i]==-1:
#             missing.append(i)
#     print(missing)

# arr=[1,3,5,6]
# find2missingnum2(arr,6)

def findmissingtwo(arr,n):
    sum=n*(n+1)//2
    for i in range(len(arr)):
        sum=sum-arr[i]
    avg=sum//2
    s1,s2=0,0

    for i in range(1,avg+1):
        s1+=i
    for j in range(0,len(arr)):
        if arr[j]<=avg:
            s2+=arr[j]
        else:
            break

    first=s1-s2
    second=sum-first
    return (first,second)


arr=[1,3,5,6]
print(findmissingtwo(arr,6))



