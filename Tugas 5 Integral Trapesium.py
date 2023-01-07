print("METODE NUMERIK-01")
print("INTEGRAL PANJANG")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import math
import matplotlib.pyplot as plt
import numpy as np
a = float(input('\nBatas x1: '))
b = float(input('Batas x2: '))
seg = int(input('Banyak segmen: '))
interval = float(abs((b-a)/seg))
Xo = float(a)

def f(x):
    #return 3*x**2
    #return math.sqrt(1+(-0.0095679012345678*x + 0.1638888888888889)**2)
    return x**9 + 3*x**5 + 15*x

def operationTrapezoid(a,b,seg,interval,Xo):
    sumLength = float(0)
    step = 1
    opState = True
    while opState:
        Xi = float((interval*step) + a)
        length = float(((f(Xo)+f(Xi))/2)*interval)
        sumLength = float(sumLength + length)
        print('i= %d, Xo= %0.8f, Xi= %0.8f, f(Xo)= %0.8f, f(Xi)= %0.8f, AREA= %0.8f, SUM= %0.8f' % (step,Xo,Xi,f(Xo),f(Xi),length,sumLength))
        opState = Xi < b and step < seg
        Xo = Xi
        step = step + 1
    return sumLength


panjang = operationTrapezoid(a,b,seg,interval,Xo)
surfaceArea = float(3.1415926535897932384*(b/2)*panjang)
totalSurface = surfaceArea + (3.1415926535897932384*(a/2)**2)
print('Panjang grafik : %0.15f' %(panjang))
print('Luas Permukaan Tangki Anggur :%0.15f' %(totalSurface), "in2")
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")




