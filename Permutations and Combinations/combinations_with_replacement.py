from itertools import combinations_with_replacement
s,n=input().split()
s=sorted(s)
ans=combinations_with_replacement(s,int(n))
for i in list(ans):
    print("".join(i))