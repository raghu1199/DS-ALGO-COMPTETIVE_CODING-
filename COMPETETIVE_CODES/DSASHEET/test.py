

# n=5
# print(round(n,2))
# if n%2==0:
#     print(n//2)
# else:
#     print(n/2)

# r=(5,2,3)
# r2=(5,2,3)
# s=set()
# s.add(r)
# s.add(r2)
# print(s)

# i=ord('c')-ord('a')
# print(i)
arr=[50,10,100,50,200]
temp=arr[::]
temp.sort()
hm={}
cnt=1
for ele in temp:
    hm[ele]=0
print(hm)
cnt=1
for k,v in hm.items():
    hm[k]=cnt
    cnt+=1
print(hm)

for i in range(len(arr)):
    arr[i]=hm[arr[i]]

print(arr)
