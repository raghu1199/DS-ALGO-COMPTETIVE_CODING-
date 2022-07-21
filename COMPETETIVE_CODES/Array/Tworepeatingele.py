

# def tworepeatingele(arr):
#     d={}
#     for ele in arr:
#         if ele in d:
#             d[ele]+=1
#         else:
#             d[ele]=1
#     print(d)
#     repeat=[]
#     for k,v in d.items():
#         if v>=2:
#             repeat.append(k)
#     return repeat

# arr=[2,4,3,1,5,2,5,4]
# print(tworepeatingele(arr))

def repeat(arr):
    n=len(arr)
    m=n-2
    x,y=0,0
    # find x
    for i in range(1,m+1):
        x=x^i
    # find y
    for i in range(n):
        y=y^arr[i]
    xor=x^y
    rightsetbit=xor & (~xor+1)

    #print(bin(rightsetbit),rightsetbit)
    
    # divide given arr  elements based on rightmostbitset position
    #[2,4,3,1,2,5,4]
    x,y=0,0
    for i in range(n):
        # 2,3,2 have 2nd bit set so x=0 xor 2 xor 3 xor 2
        if arr[i] & rightsetbit:
            x=x^arr[i]
        else:
            y=y^arr[i]   # 4 xor 1 xor 5 xor 4
    # y contains 1 xor 5 and x contains 3
    # now xor x and with 1 to m not with arr elements so 3 will come again and 3 xor 3 gives 0 so
    # x conytinas only 2
    for i in range(1,m+1):
        if i & rightsetbit:
            x=x^i
        else:
            y=y^i
    
    return (x,y)

arr=[2,4,3,1,2,5,4]
print(repeat(arr))












