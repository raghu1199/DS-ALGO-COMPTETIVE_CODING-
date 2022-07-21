
def kmostfrequent(arr,t):
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    # l=[]
    # for k,v in freq.items():
    #     l.append([k,v])
    # l.sort(key=lambda x:x[1],reverse=True)
    l=sorted(freq.items(),key=lambda item:item[1],reverse=True)
    print(l)
    output=[]
    for i in range(0,t):
        output.append(l[i][0])
    #print(output)
    return output

arr=[1,1,1,2,2,3]
#arr=[1]
print(kmostfrequent(arr,2))

# O(N)
from collections import defaultdict
def kmostfrequesnt2(arr,t):
    bucket=[[-1]]*(len(arr)+1)
    #bucket=defaultdict(list)
    freq={}
    for ele in arr:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1


    for k,v in freq.items():
        if bucket[v]==[-1]:
            bucket[v]=[k]
        else:
            bucket[v]=bucket[v]+[k]
    print(bucket)
    # get top k elements
    
    out=[]
    for i in range(len(bucket)-1,-1,-1):
        if bucket[i]!=[-1] and t>0:
            out+=bucket[i]
            t=t-len(bucket[i])
    print(out)

arr=[1,1,2,2,3]
#arr=[1]
kmostfrequesnt2(arr,1)
