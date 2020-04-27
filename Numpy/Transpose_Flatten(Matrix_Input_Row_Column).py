#Take input for Row and Column and make a Numpy array
#perfom transpose , flatten

import numpy
row,column=map(int,input().split())
resh_arr=numpy.array([input().strip().split() for _ in range(row)],int)
print(resh_arr.transpose())
print(resh_arr.flatten())

****************************************************


#Alternative Solution

import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)

np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())
