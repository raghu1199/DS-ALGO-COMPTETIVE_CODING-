
# M rows N colms An*m -> Bm*n
def transpose(a,r,c):
    B=[[ 0 for j in range(r)] for i in range(c)] # Bc*r
    for i in range(c):
        for j in range(r):
            B[i][j]=a[j][i]
    return B

def reverseEachCol(arr,r,c):
    for j in range(c):  # for each col go to till 0 to row//2 to reverse elements of each col
        for i in range(0,r//2):
            arr[i][j],arr[r-1-i][j]=arr[r-1-i][j],arr[i][j]

def reverseEachRow(arr,r,c):
    for i in range(r):
        for j in range(0,c//2):
            arr[i][j],arr[i][c-1-j]=arr[i][c-1-j],arr[i][j]


def printMatrix(arr,r,c):
    for i in range(r):
        for j in range(c):
            print(arr[i][j],end=" ")
        print()

    


def rotateAnitcloack(arr,r,c):
    print("Original Matrix:")
    printMatrix(arr,r,c)
    B=[[0 for j in range(r)] for i in range(c)] # A(r*c) sot AT-> B(c*r)
    B=transpose(arr,r,c)
    print("after transpose")
    printMatrix(B,c,r)
    reverseEachCol(B,c,r)
    print("after 90 anticlock:")
    printMatrix(B,c,r)


def rotateCloack(arr,r,c):
    print("Original Matrix:")
    printMatrix(arr,r,c)
    B=[[0 for j in range(r)] for i in range(c)] # A(r*c) sot AT-> B(c*r)
    B=transpose(arr,r,c)
    print("after transpose")
    printMatrix(B,c,r)
    reverseEachCol(B,c,r)
    print("after 90 ClockWise:")
    printMatrix(B,c,r)
    



# arr=[
#     [1,2],
#     [4,5],
#     [7,8],
# ]
# rotateAnitcloack(arr,3,2)
# rotateCloack(arr,3,2)

def setrowcolzeros(arr,row,col,r,c):
    # make rows zeros
    for i in range(r):
        if arr[i][col]!=-9999:
            arr[i][col]=0

    # make elements of col zeros
    for j in range(c):
        if arr[row][j]!=-9999:
            arr[row][j]=0
    #pos itself
    arr[row][col]=0

def setmatrixZeros(arr,r,c):
    # replace 0 to -9999 to handle 0 of another row,col
    # and whenever u find -9999 make rowCol zeros if arr[i][j]!=-9999
    print("Original:")
    printMatrix(arr,r,c)
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                arr[i][j]=-9999
    for i in range(r):
        for j in range(c):
            if arr[i][j]==-9999:
                setrowcolzeros(arr,i,j,r,c)
    print("after:")
    printMatrix(arr,r,c)

arr=[
    [0,1,2,3],
    [3,4,5,0],
    [1,3,1,5]
]
setmatrixZeros(arr,3,4)

#O(N*N)
def countNegative(arr):
    r=len(arr)
    c=len(arr[0])
    cnt=0
    for i in range(r-1,-1,-1):
        for j in range(0,c,1):
            if arr[i][j]<0:
                cnt+=c-j
                break
    return cnt

# o(n+m)
def countnegative2(arr):
    r=len(arr)
    c=len(arr[0])
    cnt=0
    i=r-1
    j=0
    while i>=0 and j<c:
        if arr[i][j]<0:
            cnt+=(c-j)
            i=i-1
            continue
        else:
            j=j+1
    return cnt



# arr=[
#     [4,3,2,-1],
#     [3,2,1,-1],
#     [1,1,-1,-2],
#     [-1,-1,-2,-3]
# ]
# arr2=[
#     [3,2],
#     [1,0]
# ]
# print(countnegative2(arr2))

# O
def kWeakestRows(arr,k):
    r=len(arr)
    out=[]
    for i,row in enumerate(arr):
        out.append([i,sum(row)])
    out.sort(key=lambda x:x[1])
    sol=[]
    for i in range(k):
        sol.append(out[i][0])
    return sol

# arr=[
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [1,1,1,0,0],
#     [1,1,1,1,1],
# ]
# print(kWeakestRows(arr,2))

def BS(arr):
    l=0
    h=len(arr)-1
    while l<h:
        mid=l+(h-l)//2
        if arr[mid]==1:
            l=mid+1
        else:
            h=mid
    return l


def kweakestRows2(arr,k):
    out=[]
    for i,row in enumerate(arr):
        out.append([BS(row),i])
    out.sort()

    return [out[i][1] for i in range(k)]


arr=[
    [1,1,1,1,0],
    [1,1,0,0,0],
    [1,1,1,0,0],
    [1,1,1,1,1],
]
print(kweakestRows2(arr,2))


