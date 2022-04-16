import sys
maxint=int(1e9+7)

def matrixchain(p,n):
    m=[[0 for col in range(n)] for row in range(n)]
    # m[1][1] m[2][2] cost is 0
    for i in range(1,n):
        m[i][i]=0

    # l is chain length
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=maxint
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q

    return m[1][n-1]  # A1..to An cost


p=[5,4,6,2,7]
n=len(p)
print(matrixchain(p,n))
