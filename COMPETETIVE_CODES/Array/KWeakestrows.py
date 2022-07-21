

# A row i is weaker than row j, if the number of soldiers in row i is less than the 
# number of soldiers in row j, or they have the same number of soldiers but i is less than j. 
# Soldiers are 
# always stand in the frontier of a row, that is, always ones may appear first and then zeros.
from collections import deque

def kweakest(arr,k):
    N=len(arr)
    M=len(arr[0])
    weakkest=deque()
    for i in range(N):
        count=0
        for j in range(M):
            if arr[i][j]==1:
                count+=1
            else:
                break   # if not 1 then break inner loop go to next row bcz first 1 comes then all 0
        weakkest.append([i,count])
    
    sol=list(weakkest)
    sol.sort(key=lambda x:x[1])
    weakkest=[]
    for i in range(0,k):
        weakkest.append(sol[i][0])

    return weakkest

arr=[
    [1,1,0,0,0],

    [1,1,1,1,0],

    [1,0,0,0,0],

    [1,1,0,0,0],

    [1,1,1,1,1]
 ]
k=3
print(kweakest(arr,k))




     
        
