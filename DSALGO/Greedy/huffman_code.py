from heapq import heappop,heappush

class Node:
    def __init__(self,char,freq,left=None,right=None):
        self.char=char
        self.freq=freq
        self.left=left
        self.right=right
    # give less than ,equals,function support to work with minheap of heapq -> IMP

    def __lt__(self,other):
        return self.freq < other.freq
        
    def __eq__(self,other):
        if other==None:
            return False
        if not isinstance(other,Node):
            return False
        return self.freq==other.freq

def encode_helper(root,currentcode,encoded):
    if root==None:
        return
    if root.char!=None:
        encoded[root.char]=currentcode
        return
    if root.char==None:  # means it is the merged node so it mist have left nd right child
        encode_helper(root.left,currentcode+'0',encoded)
        encode_helper(root.right,currentcode+'1',encoded)


def encode(heap,encoded):
    root=heappop(heap)
    currentcode=''
    encode_helper(root,currentcode,encoded)

def huffman(chars,freq):
    heap=[]
    encoded={}
    for i in range(len(chars)):
        node=Node(chars[i],freq[i])
        heappush(heap,node)
    #print(heap)
    while len(heap)>1:
        left=heappop(heap)  # 1st smallesr
        right=heappop(heap)  # 2nd smallest
        
        mergedNode=Node(None,left.freq+right.freq)
        mergedNode.left=left
        mergedNode.right=right
        heappush(heap,mergedNode)

    encode(heap,encoded)
    print(encoded)
    

chars=['a','b','c','d','e','f']
freq=[5,25,7,15,4,12]
huffman(chars,freq)