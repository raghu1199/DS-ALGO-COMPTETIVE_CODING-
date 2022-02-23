result=[0]*1000
def fib(n):
    if n<=1:
        return 1
    if(result[n]!=0):
        return result[n]
    else:
        result[n]=fib(n-1)+fib(n-2)
        return result[n]

print(fib(3))