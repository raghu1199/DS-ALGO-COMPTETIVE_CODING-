

def allPrimes(N):
    isPrime=[True]*(N+1)
    for i in range(2,N+1):
        if isPrime[i]==True:
            for j in range(i*i,N+1,i):
                isPrime[j]=False

    for i in range(2,N+1):
        if isPrime[i]:
            print(i,end=" ")
    print()

allPrimes(30)


def primefactors(num):
    ans=[]
    while num%2==0:
        ans.append(2)
        num=num//2
    
    for i in range(3,int(num**0.5)+1,2):
        while num%i==0:
            ans.append(i)
            num=num//i
        
    if num>2:
        ans.append(num)
    return ans

def primefactor2(num):
    ans=[]
    for i in range(2,num):
        while num%i==0:
            ans.append(i)
            num=num//2
    
    return ans
N=1000
spf=[i for i in range(N+1)]
def seiveprimefactor():
    for i in range(2,int(N**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,N,i):
                if spf[j]==j:
                    spf[j]=i


num=24
ans=[]
seiveprimefactor()
while num!=1:
    ans.append(spf[num])
    num=num//spf[num]

print(ans)


# ans=primefactors(12)
# res=primefactor2(12)
# print(ans,res)



