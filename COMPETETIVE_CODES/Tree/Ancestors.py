


from collections import deque


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.pred=None
#         self.left=self.right=None
    
# def insert(root,key):
#     current=root
#     parent=None
#     if root is None:
#         return Node(key)

#     while current!=None:
#         parent=current
#         if key < current.data:
#             current=current.left
#         elif key>=current.data:
#             current=current.right
    
#     if key < parent.data:
#         parent.left=Node(key)
#         parent.left.pred=parent
#     else:
#         parent.right=Node(key)
#         parent.right.pred=parent
    
#     return root

# # serach in tree 0(N) in BST (logN)
# def searchnode(root,key):

#     if root is None:
#         return None
#     q=deque()
#     q.append(root)

#     while True:
#         nodecount=len(q)
#         if nodecount==0:
#             return None

#         while nodecount>0:
#             node=q.popleft()
#             if node is None:
#                 nodecount-=1
#                 continue
#             if node.data==key:
#                 return node
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#             nodecount-=1
    
# def findpred(root,node):
#     current=node.pred
#     if current is None:
#         print("pred not exits")

#     while current!=None:
#         print(current.data)
#         current=current.pred



# root=None
# for key in [10,5,25,2,7,30]:
#     root=insert(root,key)
# node= searchnode(root,7)
# #print(node.data)

# if node is not None:
#     findpred(root,node)
# else:
#     print("Node not exits in tree")



# using dfs
def dfs(root,target,adj):
    N=len(adj)
    pred=[-1]*N   # make nodes from 0 to N (if 1 to N make size N+1)
    visited=[False]*N
    stack=deque()
    stack.append(root)
    visited[root]=True
    out=[]
    while stack:
        u=stack.pop()
        if u==target:
            v=pred[u]
            out.append(v)
            while v!=root:
                v=pred[v]
                out.append(v)
            return out

        for v in adj[u]:
            if visited[v]==False:
                stack.append(v)
                pred[v]=u
                visited[v]=True

adj={0:[1,2],1:[3,4],2:[5,6],3:[],4:[7,8],5:[],6:[],7:[],8:[]}
print(dfs(0,7,adj))





    

        
    
   
