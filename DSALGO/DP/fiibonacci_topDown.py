
# recursive O(2^n) fibo
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(4))

# top down dp 
F=[None]*100
F[0]=0
F[1]=1
def fibTpDown(n):
    if F[n]==None:
        print("calculating fib..",n)
        F[n]=fibTpDown(n-1)+fibTpDown(n-2)
    return F[n]

print(fibTpDown(4))

# bottomup dp
Fib=[None]*20
Fib[0],Fib[1]=0,1
def fibBtUp(n):
    for i in range(2,n+1):
        print("calculating fib..",i)
        Fib[i]=Fib[i-1]+Fib[i-2]
    return Fib[n]
print(fibBtUp(4))



