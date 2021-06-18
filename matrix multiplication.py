import numpy

a=numpy.array([[2,4],
               [3,4]])
b=numpy.array([[1,2],
               [1,3]])
x=numpy.array([[0,0],
               [0,0]])

for r in range(2): #range of the row of matrix a
    for c in range(2): #range of the column of matrix b
        for i in range(2):
            x[r][c]=x[r][c]+a[r][i]*b[i][c]
print(x)