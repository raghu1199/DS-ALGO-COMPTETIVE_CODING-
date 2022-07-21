
def isanagram(s,t):
    freq={}
    for c in s:
        if c in freq:
            freq[c]+=1
        else:
            freq[c]=1
    for c in t:
        if c in freq:
            freq[c]-=1
        else:
            return False
    for k,v in freq.items():
        if v!=0:
            return False
    return True

print(isanagram("anagram","nagrama"))
print(isanagram("rat","car"))
    
def isanagram2(s,t):
    freqS,freqT={},{}
    for i in range(len(s)):
        freqS[s[i]]=1+freqS.get(s[i],0)
        freqT[t[i]]=1+freqT.get(t[i],0)

    for k in freqS:
        if freqS[k]!=freqT.get(k,0):
            return False
    return True


print(isanagram2("anagram","nagrama"))
print(isanagram2("rat","car"))