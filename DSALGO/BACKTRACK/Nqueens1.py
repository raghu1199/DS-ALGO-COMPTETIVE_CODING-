N=int(input("enter no of queens:"))
board=[[0]*N for _ in range(N)]

def isSafe(i,j):
    fixedrow=i
    fixedcol=j
    # check row and col, is there any queen in given row i or in given col j?
    for k in range(0,N):
        if board[fixedrow][k]==1 or board[k][fixedcol]==1:
            return False
    # check diagonals in scannig entire board if positive diaogonals(r+c) or negative diagonals(r-c)
    # of given pos (i,j) comes it will going to check whether there is queen already placed or not
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return False
    
    return True  # if none above case true means pos (i,j) is safe to place queen  

def Nqueens(n):
    # each time we go to place next queen we decrement n, so if all queens placed means we done solving
    if n==0:
        return True
    
    for i in range(0,N):
        for j in range(0,N):
            if isSafe(i,j) and board[i][j]!=1:
                board[i][j]=1
                # given tha parent queen is placed here go to place next queen
                if Nqueens(n-1):
                    return True
                # if next queen can't be placed anywhere, then backtrack here change parent queen's location
                board[i][j]=0
                # try next location for placing parent queen
    
    return False  # if all position tried bt still queen not placed so return false indicate u have to backtrack


Nqueens(N)
for row in board:
    print(row)