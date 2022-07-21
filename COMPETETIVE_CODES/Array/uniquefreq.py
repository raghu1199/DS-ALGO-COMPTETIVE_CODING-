# [1,2,2,3,3] returns False bcz 1 appears only once nd rest ele freq is same
# if all ele freq same then return true
#[1,1,2,2,3,3] return True

def uniquefreq(arr):
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    
    
