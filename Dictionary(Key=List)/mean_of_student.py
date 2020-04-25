from statistics import mean
n=int(input())
student=dict()
for _ in range(n):
    name=input()
    math,phy,chem=(float(input()) for _ in range(3))
    student[name]=[math,phy,chem]

take=input()
ans=mean(student[take])
print('{:.2f}'.format(ans))

