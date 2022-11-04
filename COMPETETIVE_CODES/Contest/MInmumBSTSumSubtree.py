import sys


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# a=Node(10)
# b=Node(20)
# c=Node(50)
# a.left=c
# b.right=Node(40)
# hm={}
# hm[a]=a.data
# hm[c]=c.data

# print(hm[a.left])
# stores min val of curr node's subtreem

def dfs(curr:Node):
    
    if curr==None:
        return 0
    if curr.left==None and curr.right==None:
        subSize[curr]=1
        subSum[curr]=curr.data
        maxVal[curr]=curr.data
        minVal[curr]=curr.data
        return
    # curr have only right child
    elif curr.left==None:
        if curr==None:
            return 0
        dfs(curr.right)     # first traverse right subtree
        subSize[curr]=1+subSize[curr.right]
        subSum[curr]=curr.data+subSum[curr.right]
        maxVal[curr]=max(curr.data,maxVal[curr.right])
        minVal[curr]=min(curr.data,minVal[curr.right])
    # curr have only left child
    elif curr.right==None:
        dfs(curr.left)    # first traverse left subtree of curr
        subSize[curr]=1+subSize[curr.left]
        subSum[curr]=curr.data+subSum[curr.left]
        maxVal[curr]=max(curr.data,maxVal[curr.left])
        minVal[curr]=min(curr.data,minVal[curr.left])
    # curr have both left nd right child
    else:
        dfs(curr.left)     # go left nd compute all values  for curr.left
        dfs(curr.right)    # go right nd computer all values for curr.right
        subSize[curr]=1+subSize[curr.left]+subSize[curr.right]
        subSum[curr]=curr.data+subSum[curr.left]+subSum[curr.right]
        maxVal[curr]=max(curr.data,max(maxVal[curr.left],maxVal[curr.right]))
        minVal[curr]=min(curr.data,min(minVal[curr.left],minVal[curr.right]))
    


def isBst(curr:Node,requiredsum):
    global minSize
    if curr.left==None and curr.right==None:
        if curr.data==requiredsum:
            minSize=1
        return True
    # only have right child
    elif curr.left==None:
        isRightbst=isBst(curr.right,requiredsum)
        if isRightbst and minVal[curr.right]>curr.data:
            if subSum[curr]==requiredsum:
                minSize=min(minSize,subSize[curr])
            return True
        else:
            return False
    # only have left child
    elif curr.right==None:
        isLeftbst=isBst(curr.left,requiredsum)
        if isLeftbst and maxVal[curr.left]<curr.data:
            if subSum[curr]==requiredsum:
                minSize=min(minSize,subSize[curr])
            return True
        else:
            return False
    # have both child
    else:
        isLeftbst=isBst(curr.left,requiredsum)
        isRightbst=isBst(curr.right,requiredsum)
        if (isLeftbst and isRightbst) and (maxVal[curr.left]<curr.data and minVal[curr.right]>curr.data):
            if subSum[curr]==requiredsum:
                minSize=min(minSize,subSize[curr])
            return True
        else:
            return False


a=Node(13)
a.left=Node(5)
a.left.left=None
a.left.right=Node(17)
a.left.right.left=Node(16)
a.right=Node(23)


subSize={}
subSum={}
maxVal={} # stores max val of curr node's subtrree
minVal={} 
minSize=sys.maxsize
dfs(a)
isBst(a,38)
print(minSize)
#print(subSize)
print(subSum)







