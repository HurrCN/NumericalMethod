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

#Definisi fungsi volume terhadap waktu untuk x1
def funcOne(dataXValOne):
    z = dataXValOne
    q = -0.273*z
    volume = -153.8461*math.exp(q) - 563.539*math.exp(q) + ((5*math.sin(2*math.pi*z))/math.pi)+3900
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
    return dataVolume - dataDCrate*dataXValOne

# =================================================================================

#Definisi operasi gradien numerik titik 1
def dTFOne(dataXValOne,dataDCrate):
    z = dataXValOne
    D = dataDCrate
    q = -0.273*z
    dVdt = 42*z*math.exp(q) + 10*math.cos(2*math.pi*z) - D
    return dVdt

#Definisi operasi gradien numerik titik 2
def dTFTwo(dataXValTwo,dataDCrate):
    z = dataXValTwo
    D = dataDCrate
    q = -0.273*z
    dVdt = 42*z*math.exp(q) + 10*math.cos(2*math.pi*z) - D
    return dVdt

# =================================================================================

def main(h,seg,dataXValOne,dataXValTwo,dataVolume,dataDCrate,dataTFOne,dfNumOne,dfNumTwo):
    Y1 = dataTFOne
    step = 1
    condition = True
    while condition:
        Y2 = Y1 + ((dfNumOne+dfNumTwo)/2)*h
        print("\nSTEP : %d" %step)
        print("Domain  x1 = %0.20f | x2 = %0.20f" %(dataXValOne,dataXValTwo))
        #print("Discharge Rate : %0.35f" %(dataDCrate))
        #print("CurrentObservation points  T1 = %0.20f | T2 = %0.20f" %(dataXValOne,dataXValTwo))
        #print("Gradient values  dF1 = %0.35f | dF2 = %0.35f" %(dfNumOne,dfNumTwo))
        print("Function result  y1 = %0.20f | y2 = %0.20f" %(Y1,Y2))
        Y1 = Y2
        step = step + 1
        condition = step <= seg
    return

dataXValOne = xValOne(a, b, h, seg)
dataXValTwo = xValTwo(a, b, h, seg)
dataVolume = funcOne(dataXValOne)
dataDCrate = discharge(dataVolume)
dfNumOne = dTFOne(dataXValOne, h)
dfNumTwo = dTFTwo(dataXValTwo, h)
dataTFOne = tFOne(dataVolume,dataDCrate,dataXValOne)
main(h,seg,dataXValOne,dataXValTwo,dataVolume,dataDCrate,dataTFOne,dfNumOne,dfNumTwo)