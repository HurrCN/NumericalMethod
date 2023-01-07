# TUGAS METODE NUMERIK-01
# METODE REGULA FALSI
# Nama     : MUHAMMAD HURRICANE
# NPM      : 1906356191

# Saya akan menggunakan library "math" sebagai pembantu dalam math operators
import math

# Berikut adalah kolom input data
def inputData():
    a = float(input('Asumsi A : '))
    b = float(input('Asumsi B : '))
    error = float(input('Besar toleransi : '))
    return (a,b,error)

# Definisi persamaan
def f(x):
    return (15*math.pow(x,4) - 480*math.pow(x,2) + 1792)/266616

# Dibuat pengkondisian sebagai syarat berjalannya program
def kondisi(a,b):
    if(f(a)*f(b)<=0):
        return True
    else : 
        return False

# Untuk update besar a dan b dalam metode Regula Falsi
def updateBoundary(a,b):
    Xns = ((a*f(b) - b*f(a))/(f(b) - f(a)))
    if(f(Xns)*f(a)<0): 
        return (a,Xns)
    else: 
        return(Xns,b)

# Cek konvergensi berdasarkan kedekatan nilai f(x) terhadap sumbu x
# Saya mencoba metode buatan saya pribadi dan hasilnya memiliki akurasi yang sama kuat
def konvergensiHasil(a,b,error):
    while(abs(f(a))>error and abs(f(b))>error):
        a,b = updateBoundary(a,b)
    if(abs(f(a))>abs(f(b))):
        return b
    else :
        return a

# Berikut ini adalah program utamanya yang akan dijalankan
def main():
    a,b,error = inputData()
    if(kondisi(a,b)):
        hasil=konvergensiHasil(a,b,error)
        print("Adapun akar yang memenuhi persamaan yang diujikan adalah X = "+str(hasil))
        print("Tugas Regula Falsi ini dikerjakan oleh MUHAMMAD HURRICANE 1906356191")
    else:
        print("Asumsi A dan B tidak memenuhi operasi Regula Falsi")
main()
