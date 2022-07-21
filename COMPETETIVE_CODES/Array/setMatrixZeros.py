
def setrowcolzeros(arr,row,col,N):
    # make row wise zero (col zero)
    for i in range(N):
        arr[i][col]=0

    for j in range(N):
        arr[row][j]=0

    #arr[row][col]=0
def setmatrix(arr,N):
    # mark all zeros to -1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                arr[i][j]=-1
    # find -1 make its ro and ol zeros

    for i in range(N):
        for j in range(N):
            if arr[i][j]==-1:
                setrowcolzeros(arr,i,j,N)
    
    for i in range(N):
        print(arr[i])

arr=[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
setmatrix(arr,3)



