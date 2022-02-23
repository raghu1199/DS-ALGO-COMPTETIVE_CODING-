
#head recursion after recursive call returns then operation is performed(remining)
#uses more call stack
def fact1(n):
    if n<=1:
        return 1 b
    else:
        return n*fact1(n-1)

# tail recursion after recursive call no more operation is performed
# less call stack uses accumulato to store operation res and then passes to next recursive call

def fact2(n,a):
    if n<=1:
        return a
    else:
        return fact2(n-1,n*a)

print(fact2(5,1))
print(fact1(5))
