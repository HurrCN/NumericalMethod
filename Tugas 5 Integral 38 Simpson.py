print("METODE NUMERIK-01")
print("TUGAS 5.4 INTEGRAL NUMERIK METODE SIMPSON 3/8")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import math
a = float(input('\nBatas x1: '))
b = float(input('Batas x2: '))
seg = int(input('Banyak segmen: '))

def f(x):
    return -0.004783950617283948*x**2 + 0.1638888888888889*x + 4.8

def opSimps38(a,b,seg):
    interval = abs((b - a) / seg)
    integrasi = f(a) + f(b)
    
    for i in range(2,(seg-1),3):
        k = a + (i-1)*interval
        h = a + (i)*interval
        integrasi = integrasi + 3 * (f(k)+f(h))
        print('i= %d, f(Xi)= %0.8f, SUM= %0.8f' % (i,(f(k)+f(h)),integrasi))
    for i in range(4,(seg-2),3):
        j = a + (i-1)*interval
        integrasi = integrasi + 2 * f(j)
        print('i= %d, f(Xi)= %0.8f, SUM= %0.8f' % (i,f(j),integrasi))
    luas = 3*integrasi*interval / 8
    return luas


hasil = opSimps38(a, b, seg)
print("Hasil Integrasi: %0.15f" % (hasil) )
