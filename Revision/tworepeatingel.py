

def tworepeat(arr):
    n=len(arr)
    m=n-2
    x,y=0,0
    for i in range(1,m+1):
        x=x^i
    for i in range(n):
        y=y^arr[i]

    xor=x^y
    rightsetbit=xor & (~xor+1)

    x,y=0,0
    for i in range(n):
        if arr[i] & rightsetbit:
            x=x^arr[i]
        else:
            y=y^arr[i]

    for i in range(m+1):
        if i & rightsetbit:
            x=x^i
        else:
            y=y^i
    return (x,y)

arr=[2,4,1,3,2,5,4]
print(tworepeat(arr))

    
        

    

