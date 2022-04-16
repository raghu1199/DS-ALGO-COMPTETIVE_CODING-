
def lcs(x,y):
    m=len(x)
    n=len(y)
    L=[[None]* (n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif x[i-1]==y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y) )
