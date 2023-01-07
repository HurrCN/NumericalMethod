import math
# Input Data
print("==========PERHITUNGAN NEWTON-RAPHSON==========")
a = float(input('Titik asumsi Xns awal : '))
error = float(input('Besar toleransi : '))
max_iter = float(input('Iterasi Maksimum : '))

# Definisi Fungsi       
def f(x):
    return math.sqrt(x) + x**2 - 7
# Definisi Turunan Fungsi
def df(x):
    return (1/(2*math.sqrt(x))) + 2*x
# Model Operasi Metode Newton-Raphson
def operationNR(a,error):
    step = 1
    opState = True
    while opState:
        c = a - (f(a)/df(a))
        EA = abs((c-a)/c)
        print('i= %d, Xns= %0.6f, f(Xns)= %0.4f, df(Xns)= %0.4f, EA= %0.8f' % (step,a,f(a),df(a),EA))
        opState = EA > error and step <= max_iter
        a = c
        step = step + 1

operationNR(a,error)
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")
