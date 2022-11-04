
# str="aabb"
# P=[2,1,3,0]  
# day1 replace s[p[0]]='? aa?b bt str still have consecutive elem same
# day 2 replace s[p[1]]="?" a??b now no consecutive are same so ans 2
def minimumDays(Str,P):
    n=len(Str)
    cnt=0
    for i in range(0,n-1):
        if Str[i]==Str[i+1]:
            cnt+=1
    
    if cnt==0:
        return 0
    
    for i in range(0,n):
        idx=P[i]
        if idx>0 and Str[idx-1]==Str[idx]:
            cnt-=1
        if idx<n-1 and Str[idx]==Str[idx+1]:
            cnt-=1
        Str[idx]='?'
        print(Str)
        if cnt==0:
            return i+1
    
    return -1

#S="aaabb"
#P=[1,4]
S="aabb"
P=[2,1,3,0]
print(minimumDays(list(S),P))
