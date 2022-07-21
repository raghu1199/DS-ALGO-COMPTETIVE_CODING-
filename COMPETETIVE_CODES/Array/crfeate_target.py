

def targetArr(nums,index):
    n=len(nums)
    target=[-1]*n
    for i in range(len(index)):
        if target[index[i]]==-1:
            target[index[i]]=nums[i]
        else:
            j=n-2
            print(j,index[i])
            while index[i]<=j:    # mistake was did j<=index[i] 3<2 never true!
                target[j+1]=target[j]
                print(target)
                j-=1
            j+=1
            target[j]=nums[i]
    print("final:",target)

nums=[0,1,2,3,4]
index=[0,1,2,2,1]
targetArr(nums,index)

        

