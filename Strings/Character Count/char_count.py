s=input().strip()
                
from itertools import groupby
key=[]
group=[]  

for x,y in  groupby(s):
    key.append(x)
    group.append(list(y))

for i in range(len(group)):
     count=len(group[i])
     element=int(key[i])
     print(tuple((count,element)), end=" ")                 
                    
                    