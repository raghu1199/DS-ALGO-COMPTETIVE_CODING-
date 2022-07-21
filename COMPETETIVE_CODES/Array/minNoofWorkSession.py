


def getworks(arr,l,sT,checked):
    r=len(arr)-1
    hour=0
    sol=[]
    print("current l nd r:",l,r)
    while l<=r:
        if hour+arr[l]+arr[r]<=sT and l not in checked and r not in checked:
            hour+=arr[l]+arr[r]
            checked+=[l,r]
            sol+=[arr[l],arr[r]]
            l+=1
            r-=1
        # elif hour+arr[l] <= sT and l not in checked:
        #     hour+=arr[l]
        #     checked.append(l)
        #     sol.append(arr[l])
        #     l+=1
        elif hour+arr[l]+arr[r] >sT and l not in checked and r not in checked:
            r-=1
        elif l not in checked and r in checked:
            r-=1
        elif r not in checked and l in checked:
            l+=1
    print(sol,checked)
    return sol
    
    
def trysingle(arr,l,sT,checked):
    print("Inside single")
    r=len(arr)-1
    hour=0
    sol=[]
    while l<=r:
        if hour+arr[l] <=sT and l not in checked:
            hour+=arr[l]
            checked.append(l)
            sol.append(arr[l])
            l+=1
        r-=1
        l+=1
    return sol
    print(sol,checked)
         

def minsession(arr,sT):
    arr.sort()
    s=0
    checked=[]
    for i in range(len(arr)):
       res=getworks(arr,i,sT,checked)
       if res:
           s+=1
       else:
            single=trysingle(arr,i,sT,checked)
            if single:
                s+=1
        
    return s

arr=[9,8,8,4,6]
#arr=[7,4,3,8,10]
#arr=[4,3,2,1]
print(minsession(arr,12))
