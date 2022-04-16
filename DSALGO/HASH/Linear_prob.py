

# stores (key,value) pair means if key 'orange' data 50 then if we need data we acces hash['orange]
class HashTable:
    def __init__(self):
        self.size=10
        self.keys=[None]*self.size
        self.values=[None]*self.size
    
    def hash(self,key):
        sum=0
        for i in range(len(key)):
            sum=sum+ord(key[i])
        
        print("Hashed index is:",sum%self.size)
        return sum%self.size
    
    def put(self,key,data):
        index=self.hash(key)
        # if keys[index] is not None means some other key is hashed to this index so go 
        # lineary next index nd check , if keys[index] is none then direct place your given key there
        # nd place data accoring to this key in values on that same index
        while self.keys[index] is not None:
            # if same key given as alredy prev given  in hashtable then insert new data on this key
            if self.keys[index]==key:
                self.values[index]=data
                return
            index=(index+1)%self.size   # linear probe
        
        # if nothing on that index then direct insert key in keys nd data in values
        self.keys[index]=key
        self.values[index]=data

    def get(self,key):
        # get index of hashtable for this given  key
        index=self.hash(key)
        # first check something is there or not on this index ,if something is there then check is that our requested
        # key or not check again by lineraly incrementing index
        while self.keys[index] is not None:
            if self.keys[index]==key:
                return self.values[index]
            else:
                index=(index+1)% self.size
        
        return None  # not found

    
t=HashTable()
t.put("12",1200)
t.put('ab',"Hello")
print(t.get('ab'))


            
