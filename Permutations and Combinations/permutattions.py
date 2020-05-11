from itertools import permutations
s,n=input().split()
s=sorted(s)
ans=permutations(s,int(n))
for i in list(ans):
    print("".join(i))