
def all9s(num,n):
    for i in range(0,n):
        if num[i]!=9:
            return False
    return True

def nextPalindrom(num,n):
    if all9s(num,n):
        print("1",end=" ")
        for i in range(1,n):
            print("0",end=" ")
        print("1")
        return

    mid=n//2
    i=mid-1
    j=mid+1 if n%2 else mid
    leftsmall=False

    # ignor middle elements which are same 83 4224 69 so i->3 nd j->6
    while i>=0 and num[i]==num[j]:
        i-=1
        j+=1
    
    # check left small or not if not just miror it nd you done otherwise go to incre mid ele
    # like 71 33 22 
    if i<0 or num[i]<num[j]:
        leftsmall=True
    else:
        # only copy mirror of left to right . like 78 33 22 i-> 8 nd j-> 2 like 43 mid is 3 4<3 no so make 44
        while i>=0:
            num[j]=num[i]
            i-=1
            j+=1
    
    if leftsmall==True:
        carry=1
        i=mid-1
        # if n=odd means first only need to incre mid(no need to copy mirror of left to mid)
        #  then after mid+1 onwards copy mirror left .
        # 496 so only incre the mid 9 nd then add 1 to left  4 =5 then copy 5 to right
        if n%2:
            temp=num[mid]+carry
            carry=temp//10
            num[mid]=temp%10
            j=mid+1
        #otherwise if n=even  71 33 22 incre num[i] first 3 nd then copy it to right 71 43 22 -> 71 44 22
        else:
            j=mid
        
        while i>=0:
            temp=num[i]+carry
            carry=temp//10
            num[i]=temp%10
            num[j]=num[i]
            i-=1
            j+=1
    print("ate end:",arr)
    return arr



arr=[9,9,9]
arr=[4,3]
arr=[7,1,3,3,2,2]
arr=[4,9,6]
arr=[7,8,3,3,2]
arr=[1,0,0]
print(nextPalindrom(arr,len(arr)))
l=str(121)
print(l[::1]==l[::-1])
# N=19022
# l=str(N)
# l=list(map(int,(ele for ele in l)))
# print(l)
s="123"
s=int(s)
print(s)
l=[2,3]
s=[]
s.append(str(l[1]))
print(s)
s=100
s=str(100)
l=list(s) 
print(l)