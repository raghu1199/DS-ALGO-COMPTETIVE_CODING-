
def uniquefreqcounter(arr):
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    s=set()
    for k,v in freq.items():
        if v in s:
            return False
        else:
            s.add(v)
        
    return True

arr=[1,2,2,3,3]
print(uniquefreqcounter(arr))