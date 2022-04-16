from collections import defaultdict

def fractinal(W,weight,val):
    vwratio=[]
    n=len(weight)
    for i in range(n):
        v=val[i]
        w=weight[i]
        vwratio.append([v,w,v/w])

    vwratio.sort(key=lambda item:item[2],reverse=True)
    #vwratio=[[val,weight,v/w],...]
    currweight=0
    finalval=0.0
    sol=[]
    for item in vwratio:
        if currweight+item[1]<=W:
            currweight+=item[1]
            finalval+=item[0]
            sol.append(item)
        else:
            remain=W-item[1]
            fraction=remain/item[1]   # fraction=remain/itemweight
            finalval+=item[0]*fraction
            sol.append([item[0]*fraction,item[1]*fraction,item[2]])

    print("solution is:",sol," highestCost:",finalval)  


weight=[10,20,30]
val=[60,100,120]
W=50
fractinal(W,weight,val)

    