
# transpose matrix rotate by 90 clockwise
#A= n*m so transpose(A)-> B= m*n
# def transpose(A,N,M):
#     B=[[0 for j in range(N)] for i in range(M)]

#     for i in range(M):
#         for j in range(N):
#             B[i][j]=A[j][i]
#     print("Transposeed:")
#     for i in range(M):
#         print(B[i])
    
# A=[
#     [1,2],
#     [3,4],
#     [5,6],
# ]
# transpose(A,3,2)

# # n*n rotate by 90 anticlock
# def transpose2(A,N,M):
#     B=[[0 for j in range(N)] for i in range(M)]

#     for i in range(M):
#         for j in range(N-1,-1,-1):
#             B[i][j]=A[j][M-i-1]
#     print("Transposeed:")
#     for i in range(M):
#         print(B[i])


  
# A=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# transpose2(A,3,3)

# # in place
def transpose2(A,N,M):
    #B=[[0 for j in range(N)] for i in range(M)]
    # transpose the matrix then reverse each col
    for i in range(N):
        for j in range(i+1,N):
            # temp=A[i][j]
            # A[i][j]=A[j][i]
            # A[j][i]=temp
            A[i][j],A[j][i]=A[j][i],A[i][j]

    print("Transposeed:")
    for i in range(M):
       print(A[i])
    # revere each col
    for j in range(0,N):
        for i in range(0,N//2):
            A[i][j],A[N-1-i][j]=A[N-1-i][j],A[i][j]

    print("After revere each col:")
    for i in range(N):
       print(A[i])


    
    
    
 
A=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
transpose2(A,3,3)