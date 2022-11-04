

def generateMask(S):
    n=len(S)
    mask=0
    for i in range(0,n):
        idx=ord(S[i])-ord('a')
        mask=mask^(1<<idx)
    
    return mask

def getNoGoodpais(arr):
    res=0
    hm={}
    # update hash map on the way to avoid calculating (i,j) nd (j,i)
    for item in arr:
        mask=generateMask(item)
        if mask in hm:
            res+=hm[mask]
        
        for j in range(0,26):
            new_mask=mask ^(1<<j)
            if new_mask in hm:
                res+=hm[new_mask]

        hm[mask]=1+hm.get(mask,0)  # update the mask count

    return res

arr=["abc","bac","ab","ad"]
arr=["abc","bac","ad"]
print(getNoGoodpais(arr))

        
