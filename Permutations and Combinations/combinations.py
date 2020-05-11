from itertools import combinations
s,n=input().split()
s=sorted(s)

for x in range(1,int(n)+1):
    ans=combinations(s,x)
    for i in list(ans):
        print("".join(i))