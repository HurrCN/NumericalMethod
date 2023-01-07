# TUGAS METNUM-01
# BISECTION METHOD
# Nama   : Muhammad Hurricane
# NPM    : 1906356191

import math
# Penulis menggunakan bantuan library NUMPY Python dalam perhitungan ini
# Loket input data
a = float(input('Tebakan a : '))
b = float(input('Tebakan b : '))
error = float(input('Toleransi Kesalahan : '))

# Definisikan Fungsi yang ingin diiterasi
def f(x):
    return math.pow(x,3) - 7*math.pow(x,2) + 18*x - 11.4

# Merangkai Mekanisme Bisection
def bisection(a, b, error):
    i = 1
    print('\n\n***METODE BISECTION OLEH MUHAMMAD HURRICANE***')
    condition = True
    while condition:
        Xns = (a+b)/2
        print('Iterasi ke-%d, Xns = %0.6f and f(Xns) = %0.6f' % (i,Xns,f(Xns)))
        if f(a) * f(Xns) < 0:
            b = Xns
        else:
            a = Xns
        i = i + 1
        condition = abs(f(Xns)) > error
    print('\nAdapun akar yang memenuhi persamaan dan input tebakan adalah : %0.8f' % Xns)
    print('Tugas Metode Bisection ini dibuat oleh MUHAMMAD HURRICANE 1906356191')

# Mekanisme Persyaratan Bisection
if f(a) * f(b) > 0.0:
    print('Tebakan yang kamu masukkan gagal untuk mencari akarnya.')
    print('Silakan ulangi lagi.')
else: bisection(a, b, error)
