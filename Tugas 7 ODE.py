print("METODE NUMERIK-01")
print("TUGAS 7 ORDINARY DIFFERENTIAL EQUATION")
print("CASE : FLUID MECHANICS PROBLEM")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import matplotlib.pyplot as plt
import numpy as np
import math

# NYATAKAN SEMUA 

#Batas bawah fungsi
a = float(0)
#Batas atas fungsi
b = float(input('Durasi pengamatan sistem (s): '))
#Banyak segmen dan interval
seg = int(input('Banyak segmen : '))
h = abs(b-a)/seg

# =================================================================================

#Definisi pengolahan besar x1
def xValOne(a,b,h,seg):
    step = 1
    X1 = a
    condition = True
    while condition:
        X2 = X1 + h
        step = step + 1
        X1 = X2
        condition = step <= seg
    return X1

#Definisi pengolahan besar x2
def xValTwo(a,b,h,seg):
    step = 1
    X1 = a
    condition = True
    while condition:
        X2 = X1 + h
        step = step + 1
        X1 = X2
        condition = step <= seg
    return X2

# =================================================================================

#Definisi fungsi volume terhadap waktu
def f(x):
    q = -0.273*x
    volume = -153.8461*math.exp(q) - 563.539*math.exp(q) + ((5*math.sin(2*math.pi*x))/math.pi)
    return volume

#Definisi fungsi volume terhadap waktu untuk x1
def funcOne(dataXValOne):
    q = -0.273*x
    volume = -153.8461*math.exp(q) - 563.539*math.exp(q) + ((5*math.sin(2*math.pi*x))/math.pi)
    return volume

#Definisi fungsi discharge terhadap besar volume
def discharge(dataVolume):
    if dataVolume > 4000:
        DCrate = 0.825*0.2*(dataVolume - 4000)**2
    if dataVolume <= 4000:
        DCrate = 0
    return DCrate

#Definisi total function TF untuk besar volume aktual
def tFOne(dataVolume,dataDCrate,dataXValOne):
    return dataVolume - dataDCrate*dataXValOne + 3900

# =================================================================================

#Definisi operasi gradien numerik titik 1
def dTFOne(dataXValOne,h):
    p = dataXValOne
    X1 = float(p-h)
    X2 = float(p+h)
    X3 = float(p-(h/2))
    X4 = float(p+(h/2))
    dfA = (f(X2)-f(X1))/(X2-X1)
    dfB = (f(X4)-f(X3))/(X4-X3)
    dF = (4*dfB - dfA)/3
    return dF

#Definisi operasi gradien numerik titik 2
def dTFTwo(dataXValTwo,h):
    p = dataXValTwo
    X1 = float(p-h)
    X2 = float(p+h)
    X3 = float(p-(h/2))
    X4 = float(p+(h/2))
    dfA = (f(X2)-f(X1))/(X2-X1)
    dfB = (f(X4)-f(X3))/(X4-X3)
    dF = (4*dfB - dfA)/3
    return dF

# =================================================================================

def main(h,dataTF,dfNumOne,dfNumTwo):
    Y1 = dataTF
    step = 1
    condition = True
    while condition:
        Y2 = Y1 + ((dfNumOne+dfNumTwo)/2)*h
        Y1 = Y2
    return

dataXValOne = xValOne(a, b, h, seg)
dataXValTwo = xValTwo(a, b, h, seg)
dataVolume = funcOne(dataXValOne)
dataDCrate = discharge(dataVolume)
dfNumOne = dTFOne(dataXValOne, h)
dfNumTwo = dTFTwo(dataXValTwo, h)
dataTF = tFOne(dataVolume, dataDCrate)

print("Besar gradien numerik : %0.15f" %(df_num), "/s")
print("Besar gradien analitik : %0.15f" %(df_anl(a)), "/s")
#Tegangan geser
t = v*df_num
print("Besar tegangan geser pada ketinggian y terdata adalah : %0.15f" %(t), "Pascal")
#Error
error = abs((df_num-df_anl(a))/df_anl(a))
print("Besar kesalahan relatif : %0.15f" %(error*100),"%")