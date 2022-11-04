from collections import OrderedDict, deque

q=deque()
q.append([4,5])
q.append([3,6])
print(q[0][1])


l=[3,4,5]
q=deque(l)
print(q)

email={}
        name={}
        prev=0
        #print("details:",details)
        for item in details:
            rno=-1
            for i in range(1,len(item)):
                em=item[i]
                if already(em):
                    rno=email[em]
                    break
            if rno==-1:
                rno=prev+1
                prev=rno
                for i in range(1,len(item)):
                    em=item[i]
                    email[em]=rno
                name[rno]=item[0]
                
            elif rno!=-1:
                for i in range(1,len(item)):
                    em=item[i]
                    email[em]=rno
                name[rno]=item[0]
            
        d=defaultdict(set)
            
        for k,v in email.items():
            d[v].add(k)
        
        res=[]
        out=deque()
        for k,v in d.items():
            r=list(v)
            if r[0]!='None':
                l=sorted(r)
                q=deque(l)
                n=name[k]
                q.appendleft(n)
                #print("q:",list(q))
                res.append(list(q))
                
                
        #res.sort(reverse=True)
        return sorted(res,key=lambda x:x[0],reverse=True)
