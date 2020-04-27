import numpy
row,row2,column=map(int,input().split())
a=list()
for i in range(row):
    l=list(map(int,input().split()))
    a.append(l)

for i in range(row2):
    l=list(map(int,input().split()))
    a.append(l)

print(numpy.array(a))

***********************************************************************

import numpy as np
a, b, c = map(int,input().split())
arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arrA, arrB), axis = 0))
