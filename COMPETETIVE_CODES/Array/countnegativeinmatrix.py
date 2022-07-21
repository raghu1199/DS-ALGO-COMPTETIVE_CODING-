

def countnegative(arr,N,M):
    count=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]<0:
                count+=1
    return count

arr=[
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]
print(countnegative(arr,4,4))

