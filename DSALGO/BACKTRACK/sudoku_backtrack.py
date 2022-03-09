board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    
    for i in range(len(board)):
        # on evry 3rd line going top to down print the line
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            # print separator bt do not go to new line
            if j%3==0 and j!=0:
                print(" | ",end="")
            # if it is last ele then print it nd go to new line
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end="")

# go to board's each location if it is empty return that location (row,col) format
# here 0 indiactes empty place
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)

    return None # if no any empty location it returns None indiacting board is solved

# pos[0]->row nd pos[1]->col ,pos is location where our num is inserted in board
def valid(board,insertedNum,pos):
    fixedrow=pos[0]
    fixedcol=pos[1]

    # check row-> row is const ,col will vary so that it can compare with all ele of given row of pos
    # except pos at our fixedcol
    for col in range(len(board[0])):
        if board[fixedrow][col]==insertedNum and fixedcol!=col:
            return False

    # check col -> col is const ,row will vary so that it can compare with all ele of given col of pos
    # except pos at our fixedrow
    for row in range(len(board[0])):
        if board[row][fixedcol]==insertedNum and fixedrow!=row:
            return False
    
    # check boxes identify first given pos is in which box by box_x=pos[0]//3, box_y=pos[1]//3
    # first box 00,01,02 go down 10,11,12 go down 20,21,22 if pos(7,4) box_x=7//3=>2 nd box_y=4//3=>1
    # starting loca of box for x:box_x*3 to end box_x*3+3 means here  2*3=6 to 9
    # for y :box_y*3 to box_y*3+3 here 1*3=3 to 6 location (6,3) to (8,5) [9 nd 6 ar exclusive for end]
    box_x=pos[0]//3
    box_y=pos[1]//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if board[i][j]==insertedNum and (i,j)!=(fixedrow,fixedcol):
                return False
    
    # if not returned yet means it is valid insertion at this location
    return True

def solve(board):
    # get emply cell loaction
    find=find_empty(board)
    # if cant find empty cell  means board is fully solved
    if not find:
        return True
    else:
        row,col=find
    # try to insert num in empty place ranging 1 to 9 nd validate
    for num in range(1,10):
        if valid(board,num,(row,col)):
            board[row][col]=num
            # succesulfuly num is inserted so go to fill next cell(as child) recursively
            #  given that current num is filled in parent
            if solve(board):
                return True
            # if cant fill nums in child node meaning parent filled num was incorrect so backtrack here nd reset it
            # go to next iteration try next num nd then go recursively to solve further
            board[row][col]=0
    
    # if all nums(1 to 9) tried bt none of are valid so return false indicate we have to backtrack
    return False

print("*****Initialll Board is gievn as*****")
print_board(board)
print(valid(board,3,(0,2)))
solve(board)
print("********After solving sudoku board is:**********")
print_board(board)
