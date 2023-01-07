# Curve Fitting Program
# Developed by Muhammad Hurricane

import numpy as np

xData = np.array([2.16016, 3.24024, 4.32032, 5.4004, 6.48048])
yData = np.array([8.31061, 17.91351, 24.3443, 47.7497, 67.9739])
eqOrder = int(float('Objectives Order : '))
arraySize = 5

Z, ZTr = np.zeros(arraySize, dtype=float)

for i in range(1,arraySize+1):
    for j in range(1,eqOrder+2):
        Z[i][j]=xData[i]^(eqOrder+1-j)
