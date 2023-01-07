# Developed by Muhammad Hurricane
# Finalized in Sept 04, 2021

import matplotlib.pyplot as plt
import numpy as np

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
x = float(input('x3: '))

m = (y2-y1)/(x2-x1)

def y(x,x1,y1,m):
    return m*(x-x1)+y1

y(x,x1,y1,m)
res = y(x,x1,y1,m)
print('y3 = %0.1f' %(res))

xMat = np.array([x1,x2,x]) # di-list dulu
yMat = np.array([y1,y2,res]) # di-list dulu
plt.plot(xMat,yMat,color='r')
plt.show()
