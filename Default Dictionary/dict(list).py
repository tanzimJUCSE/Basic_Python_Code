from collections import defaultdict
n,m=map(int,input().split())
l_n=defaultdict(list)
for i in range(n):
    c=input()
    l_n[c].append(str(i+1))
    
for i in range(m):
    c=input()
    print(' '.join(l_n[c]) or -1)
    