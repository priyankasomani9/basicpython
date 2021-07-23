import numpy as np
x=int(input("enter values of how many rows you want"))
y=int(input("enter values of how many column you want"))
matrix=[]
for i in range(x):
    for j in range(y):
        matrix.append(i*j)
matrix = np.array(matrix).reshape(x, y)
