l=[]
s=set()
n=int(input())
for _ in range(n):
   a=input()
   b=float(input())
   l.append([a,b])

    
l.sort(key= lambda x:x[1])

for i in l:
   s.add(i[1])

li=list(sorted(s))
rcv=li[1]
f_li=[]    
for j in l:
   if j[1]==rcv:
      f_li.append(j[0])

for x in sorted(f_li):
   print(x)
